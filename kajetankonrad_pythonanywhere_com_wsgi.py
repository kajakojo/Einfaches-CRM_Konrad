# +++++++++++ FLASK +++++++++++
# Flask works like any other WSGI-compatible framework, we just need
# to import the application.  Often Flask apps are called "app" so we
# may need to rename it during the import:

import sys
import os

# ===================================================================
# PFAD-KONFIGURATION
# ===================================================================
# Pfad zu Ihrem Projekt auf PythonAnywhere
# WICHTIG: Passen Sie diesen Pfad an, wo Ihre Dateien tatsächlich liegen!
project_home = '/home/kajetankonrad/Einfaches-CRM_Konrad'

# Debugging: Prüfen ob der Pfad existiert
if not os.path.exists(project_home):
    # Versuche alternative Pfade
    alternative_paths = [
        '/home/kajetankonrad/mysite',
        '/home/kajetankonrad/einfaches-crm_konrad',
        '/home/kajetankonrad',
    ]
    for alt_path in alternative_paths:
        if os.path.exists(alt_path) and os.path.exists(os.path.join(alt_path, 'app')):
            project_home = alt_path
            break

# Fügen Sie das Projektverzeichnis zum Python-Pfad hinzu
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Debugging: Zeige verfügbare Dateien im Error Log
print(f"Project home: {project_home}")
print(f"Project exists: {os.path.exists(project_home)}")
if os.path.exists(project_home):
    print(f"Files in project: {os.listdir(project_home)}")
    app_path = os.path.join(project_home, 'app')
    print(f"App folder exists: {os.path.exists(app_path)}")
    if os.path.exists(app_path):
        print(f"Files in app: {os.listdir(app_path)}")

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
