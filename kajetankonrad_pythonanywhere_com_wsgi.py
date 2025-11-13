# +++++++++++ FLASK +++++++++++
# WSGI Configuration for PythonAnywhere
# This file loads the Flask CRM application

import sys
import os

# ===================================================================
# PATH CONFIGURATION
# ===================================================================
# IMPORTANT: This must point to where your project files are located
project_home = '/home/kajetankonrad/crmproject'

# Add project directory to Python path
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# ===================================================================
# UMGEBUNGSVARIABLEN
# ===================================================================

# Flask Secret Key - Secure random key
os.environ['SECRET_KEY'] = 'k9mP2xL8nQ5vR3wF7tY4uH6jB1dC0eA9sG2iN5oV8pM4qZ7rX3hK6fW1yT0bJ5'

# Flask Environment
os.environ['FLASK_ENV'] = 'production'
os.environ['DEBUG'] = 'False'

# MySQL Database Connection
os.environ['DATABASE_URL'] = 'mysql+pymysql://kajetankonrad:s4L5r7ploz9mt7@kajetankonrad.mysql.pythonanywhere-services.com/kajetankonrad$crm'

# Alternativ können Sie auch einzelne DB-Parameter setzen:
# os.environ['DB_TYPE'] = 'mysql'
# os.environ['DB_USER'] = 'kajetankonrad'
# os.environ['DB_PASSWORD'] = 'IhrMySQLPasswort'
# os.environ['DB_HOST'] = 'kajetankonrad.mysql.pythonanywhere-services.com'
# os.environ['DB_PORT'] = '3306'
# os.environ['DB_NAME'] = 'kajetankonrad$crm'

# ===================================================================
# FLASK APP LADEN
# ===================================================================
from app import create_app

# Erstelle die Flask-Anwendung
application = create_app()

# PythonAnywhere erwartet eine Variable namens 'application'
# Nicht 'app' umbenennen!
