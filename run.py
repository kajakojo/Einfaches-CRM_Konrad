from app import create_app
from app.extensions import db
import os

def init_db(app):
    with app.app_context():
        if not os.path.exists('migrations'):
            os.system('flask db init')
        os.system('flask db migrate -m "Initial migration"')
        os.system('flask db upgrade')

def main():
    app = create_app()
    
    # Initialize the database if it doesn't exist
    if not os.path.exists('app.db'):
        init_db(app)
    
    # Run the application
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()