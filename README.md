# Flask CRM Project

Ein einfaches Customer Relationship Management (CRM) System, entwickelt mit Flask, SQLAlchemy und flexibler Datenbank-Unterstützung.

## Features

- Kundenverwaltung (Erstellen, Lesen, Aktualisieren, Löschen)
- Auftragsverfolgung
- Kontakthistorie
- Flexible Datenbank-Unterstützung (SQLite, MySQL, PostgreSQL)
- Datenbankmigrationen mit Flask-Migrate

## Unterstützte Datenbanken

- **SQLite** (Standard) - Keine zusätzliche Installation erforderlich
- **MySQL / MariaDB** - Für größere Installationen
- **PostgreSQL** - Für Enterprise-Anwendungen

## Installation und Einrichtung

### 1. Repository klonen
```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Virtuelle Umgebung erstellen
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Unix/MacOS:
source venv/bin/activate
```

### 3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 4. Datenbank-Konfiguration

**WICHTIG:** Die Software liest die Datenbankzugangsdaten automatisch aus der `.env`-Datei.

#### Schritt 1: Konfigurationsdatei erstellen
```bash
# Windows:
copy .env.example .env

# Unix/MacOS:
cp .env.example .env
```

#### Schritt 2: Eigene Zugangsdaten eintragen

Öffnen Sie die neu erstellte `.env`-Datei und tragen Sie Ihre Werte ein:

**Option A: SQLite (empfohlen für Entwicklung)**
```env
SECRET_KEY=ihr-sicherer-geheimer-schluessel
DATABASE_URL=sqlite:///app.db
```

**Option B: MySQL/MariaDB**
```env
SECRET_KEY=ihr-sicherer-geheimer-schluessel
DB_TYPE=mysql
DB_USER=ihr_mysql_benutzer
DB_PASSWORD=ihr_mysql_passwort
DB_HOST=localhost
DB_PORT=3306
DB_NAME=crm_datenbank
```

**Option C: PostgreSQL**
```env
SECRET_KEY=ihr-sicherer-geheimer-schluessel
DB_TYPE=postgresql
DB_USER=ihr_postgres_benutzer
DB_PASSWORD=ihr_postgres_passwort
DB_HOST=localhost
DB_PORT=5432
DB_NAME=crm_datenbank
```

#### Beispiel-Werte (für Entwicklung):
```env
SECRET_KEY=dev-secret-key-aenderemich123
DB_TYPE=mysql
DB_USER=crm_user
DB_PASSWORD=sicheres_passwort_123
DB_HOST=localhost
DB_PORT=3306
DB_NAME=einfaches_crm_db
```

**HINWEIS:** 
- Ändern Sie `SECRET_KEY` unbedingt in der Produktion!
- Für SQLite: Keine weiteren Pakete nötig
- Für MySQL: `pip install pymysql` wird automatisch installiert
- Für PostgreSQL: `pip install psycopg2-binary` wird automatisch installiert

### 5. Entwicklungsserver starten

```bash
# Mit run.py (empfohlen):
python run.py

# Oder mit Flask-CLI:
flask run
```

Die Anwendung ist dann verfügbar unter: **http://localhost:5000**

---

## 🚀 Deployment auf PythonAnywhere

Für eine **detaillierte Schritt-für-Schritt-Anleitung** zum Deployment auf PythonAnywhere, siehe:

📄 **[PYTHONANYWHERE_DEPLOYMENT.md](PYTHONANYWHERE_DEPLOYMENT.md)**

### Schnellübersicht:

1. **PythonAnywhere-Account erstellen** (kostenlos möglich)
2. **MySQL-Datenbank einrichten** (Format: `benutzername$crm`)
3. **Code hochladen** (Git oder manuell)
4. **Virtuelle Umgebung erstellen:**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 crm-venv
   pip install -r requirements.txt
   pip install pymysql
   ```
5. **Web-App konfigurieren** (Manual configuration, Python 3.10)
6. **WSGI-Datei anpassen** (siehe `wsgi.py` im Projekt)
7. **Datenbank initialisieren**
8. **Web-App reloaden**

**Wichtig:** Die komplette Anleitung mit allen Details finden Sie in `PYTHONANYWHERE_DEPLOYMENT.md`!

## Deploying to PythonAnywhere

1. Create a PythonAnywhere account at https://www.pythonanywhere.com

2. Upload your code:
   - Use Git to clone your repository, or
   - Upload via PythonAnywhere's web interface

3. Create a virtual environment on PythonAnywhere:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Set up your web app using PythonAnywhere's web interface:
   - Choose Flask as your web framework
   - Set the path to your virtual environment
   - Configure WSGI file to point to `wsgi.py`
   - Set environment variables in the web app configuration

5. Initialize the database:
```bash
flask db upgrade
```

## Database Backup and Restore

To backup your SQLite database:
```bash
sqlite3 app.db .dump > backup.sql
```

To restore from backup:
```bash
sqlite3 app.db < backup.sql
```

## Project Structure

```
.
├── app/
│   ├── __init__.py      # Flask application factory
│   ├── models.py        # Database models
│   ├── routes.py        # View functions and routes
│   └── extensions.py    # Flask extensions
├── migrations/          # Database migrations
├── templates/          # Jinja2 templates
├── static/            # Static files (CSS, JS, images)
├── config.py         # Configuration classes
├── manage.py        # CLI commands
├── wsgi.py         # WSGI entry point
├── requirements.txt # Python dependencies
└── .env.example    # Environment variables template
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.