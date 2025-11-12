"""
WSGI-Konfiguration für PythonAnywhere

Diese Datei wird von PythonAnywhere verwendet, um die Flask-Anwendung zu starten.

WICHTIG FÜR PYTHONANYWHERE:
1. Kopieren Sie diesen Code in Ihre WSGI-Konfigurationsdatei auf PythonAnywhere
2. Passen Sie die Pfade an Ihren Benutzernamen an
3. Setzen Sie die Umgebungsvariablen in der WSGI-Datei
"""

import sys
import os

# ===================================================================
# PFAD-KONFIGURATION (ANPASSEN!)
# ===================================================================
# Ersetzen Sie 'IhrBenutzername' mit Ihrem PythonAnywhere-Benutzernamen
# Beispiel: '/home/johndoe/Einfaches-CRM_Konrad'

project_home = '/home/IhrBenutzername/Einfaches-CRM_Konrad'

# Fügen Sie das Projektverzeichnis zum Python-Pfad hinzu
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# ===================================================================
# UMGEBUNGSVARIABLEN (ANPASSEN!)
# ===================================================================
# Setzen Sie hier Ihre Umgebungsvariablen
# WICHTIG: Verwenden Sie sichere Werte in der Produktion!

os.environ['SECRET_KEY'] = 'ihr-sicherer-geheimer-schluessel-hier-aendern'
os.environ['FLASK_ENV'] = 'production'
os.environ['DEBUG'] = 'False'

# MySQL-Datenbank auf PythonAnywhere
# Format: mysql+pymysql://benutzername:passwort@server/benutzername$datenbankname
os.environ['DATABASE_URL'] = 'mysql+pymysql://IhrBenutzername:IhrMySQLPasswort@IhrBenutzername.mysql.pythonanywhere-services.com/IhrBenutzername$crm'

# Alternativ: Einzelne DB-Parameter (wenn Sie die Config.get_database_uri() Methode nutzen)
# os.environ['DB_TYPE'] = 'mysql'
# os.environ['DB_USER'] = 'IhrBenutzername'
# os.environ['DB_PASSWORD'] = 'IhrMySQLPasswort'
# os.environ['DB_HOST'] = 'IhrBenutzername.mysql.pythonanywhere-services.com'
# os.environ['DB_PORT'] = '3306'
# os.environ['DB_NAME'] = 'IhrBenutzername$crm'

# ===================================================================
# FLASK APP LADEN
# ===================================================================
from app import create_app

application = create_app()

# PythonAnywhere erwartet 'application' als Variable
app = application

if __name__ == '__main__':
    app.run(debug=False)