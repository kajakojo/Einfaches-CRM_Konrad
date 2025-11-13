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

# ===================================================================
# AUTO-DETECT PROJECT PATH (OPTIONAL)
# ===================================================================
# Falls der Standardpfad nicht existiert, versuche automatisch zu finden
if not os.path.exists(project_home):
    print(f"⚠️  Configured project_home '{project_home}' does not exist!")
    print("🔍 Searching for project in alternative locations...")
    
    # Versuche alternative Pfade
    alternative_paths = [
        '/home/kajetankonrad/mysite',
        '/home/kajetankonrad/einfaches-crm_konrad',
        '/home/kajetankonrad/Einfaches-CRM_Konrad',
        '/home/kajetankonrad',
    ]
    
    found = False
    for alt_path in alternative_paths:
        if os.path.exists(alt_path) and os.path.exists(os.path.join(alt_path, 'app')):
            project_home = alt_path
            print(f"✅ Found project at: {project_home}")
            found = True
            break
    
    if not found:
        print("❌ ERROR: Could not find project directory!")
        print("📂 Available directories in /home/kajetankonrad:")
        try:
            for item in os.listdir('/home/kajetankonrad'):
                path = os.path.join('/home/kajetankonrad', item)
                if os.path.isdir(path):
                    print(f"   - {item}")
        except Exception as e:
            print(f"   Could not list directory: {e}")

# Fügen Sie das Projektverzeichnis zum Python-Pfad hinzu
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# ===================================================================
# DIAGNOSTICS - Zeige Debug-Informationen im Error Log
# ===================================================================
print("=" * 70)
print("🔧 PYTHONANYWHERE WSGI DIAGNOSTICS")
print("=" * 70)
print(f"📁 Project home: {project_home}")
print(f"✓  Project exists: {os.path.exists(project_home)}")
print(f"🐍 Python version: {sys.version}")
print(f"📌 Current working directory: {os.getcwd()}")

if os.path.exists(project_home):
    print(f"\n📂 Files in project directory '{project_home}':")
    try:
        items = sorted(os.listdir(project_home))
        for item in items:
            item_path = os.path.join(project_home, item)
            if os.path.isdir(item_path):
                print(f"   [DIR]  {item}/")
            else:
                print(f"   [FILE] {item}")
    except Exception as e:
        print(f"   ❌ Error listing directory: {e}")
    
    # Prüfe app Ordner
    app_path = os.path.join(project_home, 'app')
    print(f"\n📦 App folder check:")
    print(f"   Path: {app_path}")
    print(f"   Exists: {os.path.exists(app_path)}")
    
    if os.path.exists(app_path):
        print(f"   ✅ App folder found!")
        print(f"\n   Files in app folder:")
        try:
            app_files = sorted(os.listdir(app_path))
            for item in app_files:
                print(f"      - {item}")
        except Exception as e:
            print(f"      ❌ Error listing app directory: {e}")
    else:
        print(f"   ❌ ERROR: App folder NOT FOUND!")
        print(f"   🔍 This is the most likely cause of 'ModuleNotFoundError: No module named app'")
        print(f"   💡 Solution: Upload your 'app' folder to {project_home}")
else:
    print(f"\n❌ ERROR: Project directory '{project_home}' does not exist!")
    print(f"💡 Solution: Either upload your project or update 'project_home' variable above")

print(f"\n🔍 Python sys.path (where Python looks for modules):")
for i, path in enumerate(sys.path[:10], 1):
    print(f"   {i}. {path}")
if len(sys.path) > 10:
    print(f"   ... and {len(sys.path) - 10} more paths")

print("=" * 70)

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
print("\n🚀 Attempting to import Flask application...")
try:
    from app import create_app
    print("✅ Successfully imported 'create_app' from 'app' module")
    
    # Erstelle die Flask-Anwendung
    print("🔨 Creating Flask application instance...")
    application = create_app()
    print("✅ Flask application created successfully!")
    print("=" * 70)
    
    # PythonAnywhere erwartet eine Variable namens 'application'
    # Nicht 'app' umbenennen!
    
except ImportError as e:
    print("=" * 70)
    print("❌ IMPORT ERROR - FAILED TO LOAD APPLICATION")
    print("=" * 70)
    print(f"Error details: {e}")
    print("\n🔍 TROUBLESHOOTING STEPS:")
    print("1. Check that the 'app' folder exists in your project directory")
    print("2. Verify that 'app/__init__.py' exists and contains 'create_app' function")
    print("3. Ensure all dependencies are installed: pip install -r requirements.txt")
    print("4. Check the project_home path is correct (see diagnostics above)")
    print("5. Review TROUBLESHOOTING_PYTHONANYWHERE.md in your project")
    print("\n📖 For detailed help, see:")
    print("   - TROUBLESHOOTING_PYTHONANYWHERE.md")
    print("   - PYTHONANYWHERE_DEPLOYMENT.md")
    print("=" * 70)
    raise  # Re-raise the error so PythonAnywhere shows it in error log

except Exception as e:
    print("=" * 70)
    print("❌ UNEXPECTED ERROR - FAILED TO CREATE APPLICATION")
    print("=" * 70)
    print(f"Error type: {type(e).__name__}")
    print(f"Error details: {e}")
    print("\n💡 This error occurred after successfully importing the app module.")
    print("Check your app/__init__.py file for errors in the create_app() function.")
    print("=" * 70)
    raise  # Re-raise the error
