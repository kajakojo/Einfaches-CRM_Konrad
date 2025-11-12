from flask import Flask
from app.extensions import db, migrate
import os

def create_app():
    # Get the base directory (project root)
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    app = Flask(__name__, 
                template_folder=os.path.join(basedir, 'templates'),
                static_folder=os.path.join(basedir, 'static'))
    
    # Load the configuration
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.routes import bp
    app.register_blueprint(bp)

    # Create database tables
    with app.app_context():
        # Import models to ensure they are known to SQLAlchemy
        from app.models import Customer, Order, Contact
        # Create tables
        db.create_all()
        
        # Add some sample data if the database is empty
        if not Customer.query.first():
            sample_customer = Customer(
                name='John Doe',
                email='john@example.com',
                phone='555-0123'
            )
            db.session.add(sample_customer)
            db.session.commit()

    return app