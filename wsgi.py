"""
WSGI-Konfiguration für PythonAnywhere

Diese Datei wird von PythonAnywhere verwendet, um die Flask-Anwendung zu starten.

WICHTIG FÜR PYTHONANYWHERE:
1. Kopieren Sie diesen Code in Ihre WSGI-Konfigurationsdatei auf PythonAnywhere
2. Passen Sie die Pfade an Ihren Benutzernamen an (ersetzen Sie 'IhrBenutzername')
3. Setzen Sie die Umgebungsvariablen in der WSGI-Datei
4. Generieren Sie einen sicheren SECRET_KEY
5. Setzen Sie Ihr MySQL-Passwort

SCHNELL-KONFIGURATION:
- Suchen Sie nach 'IhrBenutzername' und ersetzen Sie es mit Ihrem PythonAnywhere-Benutzernamen
- Suchen Sie nach 'IhrMySQLPasswort' und ersetzen Sie es mit Ihrem MySQL-Passwort
- Suchen Sie nach 'ihr-sicherer-geheimer-schluessel-hier-aendern' und generieren Sie einen neuen Key
"""

import sys
import os

# ===================================================================
# PFAD-KONFIGURATION (ANPASSEN!)
# ===================================================================
# Ersetzen Sie 'IhrBenutzername' mit Ihrem PythonAnywhere-Benutzernamen
# Beispiel: '/home/johndoe/Einfaches-CRM_Konrad'

project_home = '/home/IhrBenutzername/Einfaches-CRM_Konrad'

# ===================================================================
# AUTO-DETECT & DIAGNOSTICS (Optional - kann aktiviert bleiben)
# ===================================================================
# Diese Sektion hilft bei der Fehlersuche
print("=" * 70)
print("🔧 PYTHONANYWHERE WSGI CONFIGURATION")
print("=" * 70)
print(f"📁 Configured project_home: {project_home}")

# Prüfe ob der Pfad existiert
if not os.path.exists(project_home):
    print(f"⚠️  WARNING: Configured path does not exist!")
    print(f"📂 Please check if '{project_home}' is correct")
    print(f"💡 Common locations:")
    print(f"   - /home/IhrBenutzername/Einfaches-CRM_Konrad")
    print(f"   - /home/IhrBenutzername/mysite")
    print(f"   - /home/IhrBenutzername/einfaches-crm_konrad")
else:
    print(f"✅ Project directory exists")
    # Prüfe ob app Ordner existiert
    app_path = os.path.join(project_home, 'app')
    if os.path.exists(app_path):
        print(f"✅ App folder found at: {app_path}")
    else:
        print(f"❌ ERROR: App folder NOT found at: {app_path}")
        print(f"💡 Make sure you've uploaded the 'app' folder to your project")

print("=" * 70)

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
print("\n🚀 Loading Flask application...")

try:
    from app import create_app
    print("✅ Successfully imported Flask app module")
    
    application = create_app()
    print("✅ Flask application created successfully!")
    print("=" * 70)
    
    # PythonAnywhere erwartet 'application' als Variable
    app = application
    
except ImportError as e:
    print("=" * 70)
    print("❌ IMPORT ERROR")
    print("=" * 70)
    print(f"Error: {e}")
    print("\n🔍 TROUBLESHOOTING:")
    print("1. Verify 'app' folder exists in project directory")
    print("2. Check 'app/__init__.py' contains 'create_app' function")
    print("3. Install dependencies: pip install -r requirements.txt")
    print("4. Update 'project_home' path above to match your setup")
    print("=" * 70)
    raise

if __name__ == '__main__':
    app.run(debug=False)