# PythonAnywhere Integration - Übersicht der Änderungen

Dieses Dokument fasst alle Änderungen zusammen, die für die PythonAnywhere-Kompatibilität vorgenommen wurden.

## 📁 Neue Dateien

### 1. `PYTHONANYWHERE_DEPLOYMENT.md`
**Zweck:** Vollständige Schritt-für-Schritt-Anleitung für das Deployment auf PythonAnywhere

**Inhalt:**
- Account-Erstellung
- MySQL-Datenbank-Setup
- Code-Upload (Git & Manual)
- Virtuelle Umgebung
- Web-App-Konfiguration
- WSGI-Datei-Setup
- Datenbank-Initialisierung
- Fehlerbehebung
- Backup-Strategien

**Verwendung:** Hauptdokumentation für Benutzer

---

### 2. `init_db.py`
**Zweck:** Automatisches Datenbank-Initialisierungsskript

**Funktionen:**
- Erstellt alle Tabellen (Customer, Order, Contact)
- Fügt Beispieldaten hinzu (3 Kunden, 2 Aufträge, 1 Kontakt)
- Prüft bestehende Daten
- Fehlerbehandlung

**Verwendung:**
```bash
export DATABASE_URL='mysql+pymysql://user:pass@server/db'
python init_db.py
```

---

### 3. `setup_pythonanywhere.sh`
**Zweck:** Automatisches Setup-Skript für PythonAnywhere

**Funktionen:**
- Erstellt virtuelle Umgebung
- Installiert Abhängigkeiten
- Sammelt Datenbank-Credentials
- Generiert Secret Key
- Erstellt WSGI-Konfiguration
- Initialisiert Datenbank

**Verwendung:**
```bash
bash setup_pythonanywhere.sh
```

---

### 4. `.pythonanywhere`
**Zweck:** Konfigurationsvorlage für PythonAnywhere

**Inhalt:**
- Projekt-Konfiguration
- Pfade
- Datenbank-Settings
- Umgebungsvariablen
- Notizen

**Verwendung:** Referenz für manuelle Konfiguration

---

### 5. `.gitignore`
**Zweck:** Git-Ignore-Datei für sensible und temporäre Dateien

**Ignoriert:**
- Virtuelle Umgebungen
- Datenbank-Dateien
- `.env` Dateien
- Logs
- IDE-Dateien
- Backups

---

## 🔄 Geänderte Dateien

### 1. `wsgi.py`
**Änderungen:**
- Komplette Neugestaltung für PythonAnywhere
- Umgebungsvariablen-Setup
- Pfad-Konfiguration
- Detaillierte Kommentare und Anleitung

**Wichtig:**
- Verwendet `application` als Variable (PythonAnywhere-Standard)
- Setzt DATABASE_URL für MySQL
- Generiert/verwendet SECRET_KEY

**Vorher:**
```python
from app import create_app
app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
```

**Nachher:**
- Umfangreiche Konfiguration mit Kommentaren
- Umgebungsvariablen-Setup
- PythonAnywhere-spezifische Pfade
- Produktions-Settings

---

### 2. `config.py`
**Änderungen:**
- Neue Methode `get_database_uri()` für flexible DB-Konfiguration
- Unterstützung für SQLite, MySQL, PostgreSQL
- Liest aus Umgebungsvariablen
- Fallback-Mechanismen

**Neu:**
```python
@staticmethod
def get_database_uri():
    # Konstruiert DB-URI aus Umgebungsvariablen
    # Unterstützt: DATABASE_URL direkt oder einzelne Parameter
```

---

### 3. `app/__init__.py`
**Änderungen:**
- Template- und Static-Folder-Pfade explizit gesetzt
- Importiert `os` für Pfad-Operationen
- Behebt Template-Not-Found-Fehler

**Neu:**
```python
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
app = Flask(__name__, 
            template_folder=os.path.join(basedir, 'templates'),
            static_folder=os.path.join(basedir, 'static'))
```

---

### 4. `.env`
**Änderungen:**
- Erweiterte Kommentare
- Hinweise für PythonAnywhere
- Lokale vs. Produktions-Settings
- Klare Dokumentation

---

### 5. `.env.example`
**Änderungen:**
- Umfangreiche Datenbank-Optionen
- MySQL/PostgreSQL Beispiele
- PythonAnywhere-spezifische Hinweise
- Detaillierte Kommentare

---

### 6. `requirements.txt`
**Änderungen:**
- `MarkupSafe==2.0.1` hinzugefügt (Kompatibilität)
- `pymysql==1.1.2` aktualisiert
- `psycopg2-binary==2.9.11` aktualisiert
- Ausführliche Kommentare und Hinweise
- Installation für PythonAnywhere dokumentiert

**Wichtig:**
- MarkupSafe 2.0.1 behebt ImportError mit Jinja2 2.11.3
- pymysql ist ERFORDERLICH für PythonAnywhere MySQL

---

### 7. `README.md`
**Änderungen:**
- PythonAnywhere-Sektion hinzugefügt
- Link zu `PYTHONANYWHERE_DEPLOYMENT.md`
- Schnellübersicht für Deployment
- Aktualisierte Datenbank-Konfiguration
- Deutsche Beschreibung

---

### 8. `include.php` (NEU für PHP-Projekte)
**Zweck:** PHP-Datenbank-Konfigurationsdatei

**Für:** Parallele PHP-Projekte oder PHP-Integration

**Inhalt:**
- PythonAnywhere MySQL-Konfiguration
- Beispielwerte
- Ausführliche Kommentare
- Fehlerbehandlung-Hinweise

**Format:**
```php
$dbname = "benutzername$crm";
$dbuser = "benutzername";
$dbpasswort = "passwort";
$dbserver = "benutzername.mysql.pythonanywhere-services.com";
```

---

## 🔑 Wichtige Konfigurationswerte

### Lokale Entwicklung (.env)
```env
SECRET_KEY=dev-secret-key
DATABASE_URL=sqlite:///app.db
DEBUG=True
```

### PythonAnywhere Produktion (wsgi.py)
```python
os.environ['SECRET_KEY'] = 'generierter-sicherer-key'
os.environ['DATABASE_URL'] = 'mysql+pymysql://user:pass@server/user$crm'
os.environ['DEBUG'] = 'False'
os.environ['FLASK_ENV'] = 'production'
```

---

## 📋 Deployment-Checkliste

- [ ] PythonAnywhere-Account erstellt
- [ ] MySQL-Datenbank eingerichtet (`benutzername$crm`)
- [ ] Code hochgeladen (Git oder Upload)
- [ ] Virtuelle Umgebung erstellt (`mkvirtualenv crm-venv`)
- [ ] `requirements.txt` installiert
- [ ] `pymysql` installiert
- [ ] Web-App erstellt (Manual, Python 3.10)
- [ ] WSGI-Datei angepasst
- [ ] Virtualenv-Pfad gesetzt
- [ ] Static files konfiguriert (`/static/`)
- [ ] Datenbank initialisiert (`python init_db.py`)
- [ ] Web-App reloaded
- [ ] Funktionstest durchgeführt

---

## 🚨 Häufige Probleme & Lösungen

### 1. ImportError: cannot import name 'soft_unicode'
**Lösung:** `pip install MarkupSafe==2.0.1`

### 2. TemplateNotFound: index.html
**Lösung:** Bereits in `app/__init__.py` behoben (template_folder gesetzt)

### 3. Access denied for user
**Lösung:** MySQL-Passwort in WSGI-Datei überprüfen

### 4. Unknown database
**Lösung:** Datenbankname muss Format haben: `benutzername$datenbankname`

### 5. No module named 'pymysql'
**Lösung:** `pip install pymysql` in virtueller Umgebung

---

## 🔗 Wichtige Links

- **PythonAnywhere:** https://www.pythonanywhere.com
- **Dokumentation:** https://help.pythonanywhere.com/pages/Flask/
- **Forum:** https://www.pythonanywhere.com/forums/

---

## 📊 Datenbankstruktur (MySQL auf PythonAnywhere)

```
Datenbank: benutzername$crm
├── customers
│   ├── id (INT, PRIMARY KEY, AUTO_INCREMENT)
│   ├── name (VARCHAR)
│   ├── email (VARCHAR, UNIQUE)
│   ├── phone (VARCHAR)
│   └── created_at (DATETIME)
├── orders
│   ├── id (INT, PRIMARY KEY, AUTO_INCREMENT)
│   ├── customer_id (INT, FOREIGN KEY)
│   ├── total (DECIMAL)
│   ├── description (TEXT)
│   ├── status (VARCHAR)
│   └── created_at (DATETIME)
└── contacts
    ├── id (INT, PRIMARY KEY, AUTO_INCREMENT)
    ├── customer_id (INT, FOREIGN KEY)
    ├── subject (VARCHAR)
    ├── notes (TEXT)
    ├── contact_type (VARCHAR)
    └── created_at (DATETIME)
```

---

## ✅ Testing

### Lokal testen:
```bash
python run.py
# Öffnen: http://localhost:5000
```

### PythonAnywhere testen:
```
https://ihrbenutzername.pythonanywhere.com
```

### Datenbank-Verbindung testen:
```bash
export DATABASE_URL='mysql+pymysql://user:pass@server/user$crm'
python -c "from app import create_app; app = create_app(); print('✓ Verbindung OK')"
```

---

## 📝 Notizen

- **Kostenloser Account:** Alle 3 Monate verlängern
- **MySQL:** Nur 1 Datenbank im kostenlosen Plan
- **Reload:** Nach jeder Änderung Web-App reloaden
- **Logs:** Bei Problemen Error Log überprüfen
- **Backups:** Regelmäßige Backups mit `mysqldump` erstellen

---

**Stand:** November 2025
**Version:** 1.0
**Projekt:** Einfaches-CRM_Konrad
