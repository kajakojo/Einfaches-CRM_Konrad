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
# WICHTIG: Ändern Sie diese Werte für die Produktion!

# Flask Secret Key - ÄNDERN SIE DIES IN EINEN SICHEREN WERT!
os.environ['SECRET_KEY'] = 'pythonanywhere-prod-key-BITTE-AENDERN-' + os.urandom(24).hex()

# Flask Environment
os.environ['FLASK_ENV'] = 'production'
os.environ['DEBUG'] = 'False'

# MySQL-Datenbank auf PythonAnywhere
# Format: mysql+pymysql://benutzername:passwort@server/benutzername$datenbankname
# WICHTIG: Ersetzen Sie 'IhrMySQLPasswort' mit Ihrem echten MySQL-Passwort!
os.environ['DATABASE_URL'] = 'mysql+pymysql://kajetankonrad:IhrMySQLPasswort@kajetankonrad.mysql.pythonanywhere-services.com/kajetankonrad$crm'

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
