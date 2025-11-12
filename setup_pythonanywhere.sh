#!/bin/bash
# ===================================================================
# PythonAnywhere Schnell-Setup-Skript
# ===================================================================
# Dieses Skript hilft beim schnellen Setup auf PythonAnywhere
# 
# VERWENDUNG:
#   1. Laden Sie dieses Skript auf PythonAnywhere hoch
#   2. Führen Sie es in einer Bash-Konsole aus:
#      bash setup_pythonanywhere.sh
# ===================================================================

echo "=========================================="
echo "  Flask CRM - PythonAnywhere Setup"
echo "=========================================="
echo ""

# Farbcodes für Ausgabe
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Funktion für Erfolgsmeldungen
success() {
    echo -e "${GREEN}✓${NC} $1"
}

# Funktion für Warnungen
warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Funktion für Fehler
error() {
    echo -e "${RED}✗${NC} $1"
}

# ===================================================================
# SCHRITT 1: Verzeichnis prüfen
# ===================================================================
echo "Schritt 1: Projektverzeichnis prüfen..."

if [ ! -f "requirements.txt" ]; then
    error "requirements.txt nicht gefunden!"
    echo "Bitte führen Sie dieses Skript im Projektverzeichnis aus."
    exit 1
fi

success "Projektverzeichnis gefunden"
echo ""

# ===================================================================
# SCHRITT 2: Virtuelle Umgebung erstellen
# ===================================================================
echo "Schritt 2: Virtuelle Umgebung erstellen..."

read -p "Name der virtuellen Umgebung [crm-venv]: " VENV_NAME
VENV_NAME=${VENV_NAME:-crm-venv}

if [ -d "$HOME/.virtualenvs/$VENV_NAME" ]; then
    warning "Virtuelle Umgebung '$VENV_NAME' existiert bereits"
    read -p "Neu erstellen? (j/n): " RECREATE
    if [ "$RECREATE" = "j" ]; then
        rmvirtualenv $VENV_NAME
        mkvirtualenv --python=/usr/bin/python3.10 $VENV_NAME
        success "Virtuelle Umgebung neu erstellt"
    else
        workon $VENV_NAME
        success "Existierende virtuelle Umgebung aktiviert"
    fi
else
    mkvirtualenv --python=/usr/bin/python3.10 $VENV_NAME
    success "Virtuelle Umgebung '$VENV_NAME' erstellt"
fi

echo ""

# ===================================================================
# SCHRITT 3: Abhängigkeiten installieren
# ===================================================================
echo "Schritt 3: Abhängigkeiten installieren..."

pip install --upgrade pip > /dev/null 2>&1
success "pip aktualisiert"

pip install -r requirements.txt
if [ $? -eq 0 ]; then
    success "Alle Abhängigkeiten installiert"
else
    error "Fehler beim Installieren der Abhängigkeiten"
    exit 1
fi

# Stelle sicher, dass pymysql installiert ist
pip install pymysql > /dev/null 2>&1
success "pymysql installiert (für MySQL)"

echo ""

# ===================================================================
# SCHRITT 4: Datenbank-Konfiguration
# ===================================================================
echo "Schritt 4: Datenbank-Konfiguration..."
echo ""
echo "Bitte geben Sie Ihre MySQL-Datenbank-Details ein:"
echo "(Diese finden Sie unter 'Databases' im PythonAnywhere-Dashboard)"
echo ""

read -p "PythonAnywhere Benutzername: " PA_USERNAME
read -p "MySQL Passwort: " -s MYSQL_PASSWORD
echo ""
read -p "Datenbankname [crm]: " DB_NAME
DB_NAME=${DB_NAME:-crm}

# Konstruiere DATABASE_URL
DB_SERVER="${PA_USERNAME}.mysql.pythonanywhere-services.com"
FULL_DB_NAME="${PA_USERNAME}\$${DB_NAME}"
DATABASE_URL="mysql+pymysql://${PA_USERNAME}:${MYSQL_PASSWORD}@${DB_SERVER}/${FULL_DB_NAME}"

success "Datenbank-Konfiguration erstellt"
echo ""

# ===================================================================
# SCHRITT 5: Secret Key generieren
# ===================================================================
echo "Schritt 5: Secret Key generieren..."

SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
success "Secret Key generiert"
echo ""

# ===================================================================
# SCHRITT 6: WSGI-Konfiguration anzeigen
# ===================================================================
echo "=========================================="
echo "  WSGI-KONFIGURATION"
echo "=========================================="
echo ""
echo "Kopieren Sie den folgenden Code in Ihre WSGI-Datei:"
echo "(Web → WSGI configuration file)"
echo ""
echo "-------------------------------------------------------------------"
cat << EOF
import sys
import os

# Projektpfad
project_home = '$HOME/$(basename $(pwd))'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Umgebungsvariablen
os.environ['SECRET_KEY'] = '$SECRET_KEY'
os.environ['FLASK_ENV'] = 'production'
os.environ['DEBUG'] = 'False'
os.environ['DATABASE_URL'] = '$DATABASE_URL'

# Flask App laden
from app import create_app
application = create_app()
EOF
echo "-------------------------------------------------------------------"
echo ""

# Speichere die Konfiguration auch in eine Datei
cat > wsgi_config.txt << EOF
# WSGI-Konfiguration für PythonAnywhere
# Kopieren Sie diesen Code in Ihre WSGI-Datei

import sys
import os

project_home = '$HOME/$(basename $(pwd))'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['SECRET_KEY'] = '$SECRET_KEY'
os.environ['FLASK_ENV'] = 'production'
os.environ['DEBUG'] = 'False'
os.environ['DATABASE_URL'] = '$DATABASE_URL'

from app import create_app
application = create_app()
EOF

success "WSGI-Konfiguration gespeichert in: wsgi_config.txt"
echo ""

# ===================================================================
# SCHRITT 7: Datenbank initialisieren
# ===================================================================
echo "Schritt 7: Datenbank initialisieren..."
echo ""
read -p "Möchten Sie die Datenbank jetzt initialisieren? (j/n): " INIT_DB

if [ "$INIT_DB" = "j" ]; then
    export DATABASE_URL="$DATABASE_URL"
    export SECRET_KEY="$SECRET_KEY"
    
    python init_db.py
    
    if [ $? -eq 0 ]; then
        success "Datenbank initialisiert"
    else
        warning "Fehler beim Initialisieren der Datenbank"
        echo "Sie können es später manuell versuchen mit:"
        echo "  export DATABASE_URL='$DATABASE_URL'"
        echo "  python init_db.py"
    fi
else
    echo "Datenbank-Initialisierung übersprungen"
    echo "Sie können sie später ausführen mit:"
    echo "  export DATABASE_URL='$DATABASE_URL'"
    echo "  python init_db.py"
fi

echo ""

# ===================================================================
# ZUSAMMENFASSUNG
# ===================================================================
echo "=========================================="
echo "  ✓ SETUP ABGESCHLOSSEN"
echo "=========================================="
echo ""
echo "Nächste Schritte:"
echo ""
echo "1. Gehen Sie zu: Web → Add a new web app"
echo "   - Manual configuration"
echo "   - Python 3.10"
echo ""
echo "2. Virtualenv setzen:"
echo "   $HOME/.virtualenvs/$VENV_NAME"
echo ""
echo "3. WSGI-Datei bearbeiten:"
echo "   - Kopieren Sie den Inhalt aus: wsgi_config.txt"
echo "   - Oder scrollen Sie nach oben für die Ausgabe"
echo ""
echo "4. Static files konfigurieren:"
echo "   URL: /static/"
echo "   Directory: $HOME/$(basename $(pwd))/static"
echo ""
echo "5. Klicken Sie auf 'Reload' für Ihre Web-App"
echo ""
echo "6. Öffnen Sie Ihre Domain:"
echo "   https://${PA_USERNAME}.pythonanywhere.com"
echo ""
echo "=========================================="
echo ""
success "Viel Erfolg mit Ihrem CRM-System!"
echo ""
