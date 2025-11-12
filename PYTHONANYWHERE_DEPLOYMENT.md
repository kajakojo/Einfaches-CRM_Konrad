# PythonAnywhere Deployment Guide für Flask CRM

Diese Anleitung zeigt Schritt-für-Schritt, wie Sie das CRM-System auf PythonAnywhere deployen.

---

## 🚀 Schnellstart-Übersicht

1. PythonAnywhere-Account erstellen
2. MySQL-Datenbank einrichten
3. Code hochladen (Git oder Upload)
4. Virtuelle Umgebung erstellen
5. Web-App konfigurieren
6. WSGI-Datei anpassen
7. Datenbank initialisieren
8. Fertig! 🎉

---

## 📋 Detaillierte Anleitung

### Schritt 1: PythonAnywhere-Account erstellen

1. Gehen Sie zu https://www.pythonanywhere.com
2. Klicken Sie auf "Pricing & signup"
3. Wählen Sie einen Plan:
   - **Beginner** (kostenlos): Perfekt zum Testen
   - **Hacker** ($5/Monat): Empfohlen für Produktion
4. Registrieren Sie sich und bestätigen Sie Ihre E-Mail

---

### Schritt 2: MySQL-Datenbank einrichten

1. Loggen Sie sich in PythonAnywhere ein
2. Klicken Sie auf **"Databases"** im Dashboard
3. **MySQL-Passwort setzen:**
   - Geben Sie ein sicheres Passwort ein
   - Klicken Sie auf "Initialize MySQL"
   - **WICHTIG:** Notieren Sie sich dieses Passwort!

4. **Datenbank erstellen:**
   - Scrollen Sie zu "Create database"
   - Geben Sie einen Namen ein: `crm`
   - Klicken Sie auf "Create"
   - Ihre Datenbank heißt dann: `IhrBenutzername$crm`

**Beispiel:**
- Benutzername: `johndoe`
- Datenbankname: `johndoe$crm`
- Server: `johndoe.mysql.pythonanywhere-services.com`

---

### Schritt 3: Code hochladen

#### Option A: Git (empfohlen)

1. Öffnen Sie eine **Bash-Konsole** auf PythonAnywhere
2. Klonen Sie Ihr Repository:

```bash
cd ~
git clone https://github.com/IhrBenutzername/Einfaches-CRM_Konrad.git
cd Einfaches-CRM_Konrad
```

#### Option B: Manueller Upload

1. Zippen Sie Ihr Projektverzeichnis
2. Gehen Sie zu **"Files"** auf PythonAnywhere
3. Klicken Sie auf "Upload a file"
4. Entpacken Sie die ZIP-Datei:

```bash
cd ~
unzip Einfaches-CRM_Konrad.zip
cd Einfaches-CRM_Konrad
```

---

### Schritt 4: Virtuelle Umgebung erstellen

Öffnen Sie eine Bash-Konsole und führen Sie aus:

```bash
# Navigieren Sie zu Ihrem Projekt
cd ~/Einfaches-CRM_Konrad

# Erstellen Sie eine virtuelle Umgebung mit Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 crm-venv

# Aktivieren Sie die virtuelle Umgebung (falls nicht automatisch)
workon crm-venv

# Installieren Sie die Abhängigkeiten
pip install -r requirements.txt

# WICHTIG: Installieren Sie pymysql für MySQL-Unterstützung
pip install pymysql
```

**Hinweis:** Die virtuelle Umgebung wird automatisch unter `~/.virtualenvs/crm-venv` erstellt.

---

### Schritt 5: Web-App konfigurieren

1. Gehen Sie zur Seite **"Web"** im Dashboard
2. Klicken Sie auf **"Add a new web app"**
3. Wählen Sie Ihren Domain-Namen (z.B. `ihrbenutzername.pythonanywhere.com`)
4. Wählen Sie **"Manual configuration"** (NICHT Flask!)
5. Wählen Sie **Python 3.10**

---

### Schritt 6: WSGI-Datei anpassen

1. Auf der "Web"-Seite, scrollen Sie zu **"Code"**
2. Klicken Sie auf den Link zur WSGI-Datei (z.B. `/var/www/ihrbenutzername_pythonanywhere_com_wsgi.py`)
3. **LÖSCHEN** Sie den gesamten Inhalt
4. **KOPIEREN** Sie folgenden Code und **PASSEN SIE IHN AN:**

```python
import sys
import os

# ===================================================================
# PFAD-KONFIGURATION - ANPASSEN!
# ===================================================================
# Ersetzen Sie 'johndoe' mit Ihrem Benutzernamen
project_home = '/home/johndoe/Einfaches-CRM_Konrad'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

# ===================================================================
# UMGEBUNGSVARIABLEN - ANPASSEN!
# ===================================================================
# Generieren Sie einen sicheren Secret Key mit:
# python -c "import secrets; print(secrets.token_hex(32))"

os.environ['SECRET_KEY'] = 'generieren-sie-einen-sicheren-key'
os.environ['FLASK_ENV'] = 'production'
os.environ['DEBUG'] = 'False'

# MySQL-Datenbank - ANPASSEN!
# Format: mysql+pymysql://user:password@server/database
os.environ['DATABASE_URL'] = 'mysql+pymysql://johndoe:IhrMySQLPasswort@johndoe.mysql.pythonanywhere-services.com/johndoe$crm'

# ===================================================================
# FLASK APP LADEN
# ===================================================================
from app import create_app

application = create_app()
```

**WICHTIG - Diese Werte anpassen:**
- `johndoe` → Ihr PythonAnywhere-Benutzername (3x)
- `IhrMySQLPasswort` → Ihr MySQL-Passwort (aus Schritt 2)
- `generieren-sie-einen-sicheren-key` → Sicherer Secret Key

**Secret Key generieren:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

5. Klicken Sie auf **"Save"**

---

### Schritt 7: Virtuelle Umgebung verlinken

1. Scrollen Sie auf der "Web"-Seite zu **"Virtualenv"**
2. Geben Sie den Pfad ein: `/home/IhrBenutzername/.virtualenvs/crm-venv`
3. Beispiel: `/home/johndoe/.virtualenvs/crm-venv`

---

### Schritt 8: Statische Dateien konfigurieren

1. Scrollen Sie zu **"Static files"**
2. Fügen Sie hinzu:
   - **URL:** `/static/`
   - **Directory:** `/home/IhrBenutzername/Einfaches-CRM_Konrad/static`

---

### Schritt 9: Datenbank initialisieren

Öffnen Sie eine Bash-Konsole:

```bash
# Aktivieren Sie die virtuelle Umgebung
workon crm-venv

# Navigieren Sie zum Projekt
cd ~/Einfaches-CRM_Konrad

# Setzen Sie Umgebungsvariablen (temporär für diese Sitzung)
export DATABASE_URL='mysql+pymysql://johndoe:IhrPasswort@johndoe.mysql.pythonanywhere-services.com/johndoe$crm'
export SECRET_KEY='ihr-secret-key'

# Initialisieren Sie die Datenbank
python -c "from app import create_app; from app.extensions import db; app = create_app(); app.app_context().push(); db.create_all(); print('Datenbank erfolgreich erstellt!')"
```

**Alternativ: Mit Flask-Migrate (empfohlen):**

```bash
export FLASK_APP=run.py
export DATABASE_URL='mysql+pymysql://johndoe:IhrPasswort@johndoe.mysql.pythonanywhere-services.com/johndoe$crm'

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---

### Schritt 10: Web-App starten

1. Gehen Sie zurück zur **"Web"**-Seite
2. Klicken Sie auf den grünen Button **"Reload"**
3. Warten Sie ~10 Sekunden
4. Klicken Sie auf Ihren Domain-Link (z.B. `johndoe.pythonanywhere.com`)

🎉 **Ihre CRM-Anwendung läuft jetzt auf PythonAnywhere!**

---

## 🔧 Fehlerbehebung

### Problem: "Internal Server Error"

1. Gehen Sie zu **"Web"** → **"Log files"**
2. Öffnen Sie die **Error log**
3. Suchen Sie nach der letzten Fehlermeldung

**Häufige Fehler:**

#### Fehler: "Access denied for user"
- ❌ MySQL-Passwort falsch
- ✅ Überprüfen Sie das Passwort in der WSGI-Datei

#### Fehler: "Unknown database"
- ❌ Datenbankname falsch formatiert
- ✅ Format muss sein: `benutzername$datenbankname` (mit `$`!)

#### Fehler: "No module named 'app'"
- ❌ Projekt-Pfad falsch in WSGI
- ✅ Überprüfen Sie `project_home` in der WSGI-Datei

#### Fehler: "No module named 'pymysql'"
- ❌ pymysql nicht installiert
- ✅ `workon crm-venv && pip install pymysql`

### Problem: Änderungen werden nicht übernommen

1. Gehen Sie zu **"Web"**
2. Klicken Sie auf **"Reload"**
3. Warten Sie 10 Sekunden
4. Leeren Sie den Browser-Cache (Strg + Shift + R)

### Problem: Datenbank-Tabellen fehlen

```bash
workon crm-venv
cd ~/Einfaches-CRM_Konrad
export DATABASE_URL='mysql+pymysql://benutzername:passwort@server/database'
python -c "from app import create_app; from app.extensions import db; app = create_app(); app.app_context().push(); db.create_all()"
```

---

## 📊 Datenbank verwalten

### Mit MySQL-Konsole verbinden

```bash
mysql -u IhrBenutzername -h IhrBenutzername.mysql.pythonanywhere-services.com -p
```

Passwort eingeben → Enter

```sql
USE IhrBenutzername$crm;
SHOW TABLES;
SELECT * FROM customer;
```

### Datenbank-Backup erstellen

```bash
mysqldump -u IhrBenutzername -h IhrBenutzername.mysql.pythonanywhere-services.com -p IhrBenutzername$crm > backup.sql
```

### Datenbank wiederherstellen

```bash
mysql -u IhrBenutzername -h IhrBenutzername.mysql.pythonanywhere-services.com -p IhrBenutzername$crm < backup.sql
```

---

## 🔄 Code-Updates deployen

### Mit Git:

```bash
cd ~/Einfaches-CRM_Konrad
git pull origin main
workon crm-venv
pip install -r requirements.txt
# Gehen Sie zur "Web"-Seite und klicken Sie "Reload"
```

### Manuelle Dateien:

1. Laden Sie die geänderten Dateien über "Files" hoch
2. Überschreiben Sie die alten Dateien
3. Gehen Sie zu "Web" und klicken Sie "Reload"

---

## 📝 Checkliste für Deployment

- [ ] PythonAnywhere-Account erstellt
- [ ] MySQL-Datenbank erstellt (`benutzername$crm`)
- [ ] MySQL-Passwort notiert
- [ ] Code hochgeladen (Git oder Upload)
- [ ] Virtuelle Umgebung erstellt (`crm-venv`)
- [ ] `requirements.txt` installiert
- [ ] `pymysql` installiert
- [ ] Web-App erstellt (Manual configuration, Python 3.10)
- [ ] WSGI-Datei angepasst (Benutzername, Passwort, Secret Key)
- [ ] Virtualenv-Pfad gesetzt
- [ ] Statische Dateien konfiguriert
- [ ] Datenbank initialisiert
- [ ] Web-App reloaded
- [ ] Funktioniert! 🎉

---

## 🆘 Support

**PythonAnywhere-Dokumentation:**
- https://help.pythonanywhere.com/pages/Flask/

**PythonAnywhere-Forum:**
- https://www.pythonanywhere.com/forums/

**Häufige Probleme:**
- Überprüfen Sie die Error Logs: **Web** → **Log files** → **Error log**
- Stellen Sie sicher, dass alle Pfade korrekt sind
- Das `$`-Zeichen im Datenbanknamen ist obligatorisch!
- Secret Key muss in der WSGI-Datei gesetzt sein

---

## 💡 Tipps

1. **Entwickeln Sie lokal** mit SQLite, deployen Sie mit MySQL
2. **Nutzen Sie Git** für einfachere Updates
3. **Backups regelmäßig erstellen** (Datenbank + Code)
4. **Error Logs überprüfen** bei Problemen
5. **Kostenloser Account:** Alle 3 Monate verlängern

---

**Viel Erfolg mit Ihrem CRM auf PythonAnywhere! 🚀**
