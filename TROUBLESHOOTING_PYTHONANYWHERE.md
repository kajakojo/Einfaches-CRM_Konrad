# 🔧 Troubleshooting: "No module named 'app'" Fehler

> **⚡ QUICK FIX:** Der häufigste Grund ist ein falscher Pfad in der WSGI-Datei!  
> Öffnen Sie die WSGI-Datei und prüfen Sie die `project_home` Variable.

## 🎯 Schnelle Diagnose (2 Minuten)

**Schritt 1: Prüfe Error Log auf PythonAnywhere**
1. Gehe zu **Web** Tab
2. Klicke auf **Error log**
3. Scrolle nach unten zu den neuesten Einträgen
4. Suche nach der diagnostischen Ausgabe (beginnt mit "=" Linien)

**Schritt 2: Was sagt das Diagnose-Output?**

| Diagnose-Meldung | Problem | Lösung |
|-----------------|---------|---------|
| `✅ App folder found` | Alles OK mit Pfad | Anderes Problem - siehe unten |
| `❌ App folder NOT FOUND` | Pfad falsch | → Siehe Abschnitt 3 unten |
| `❌ Project directory does not exist` | Projekt nicht hochgeladen | → Siehe Abschnitt 1 unten |
| `⚠️ Configured path does not exist` | Pfad-Tippfehler | → Siehe Abschnitt 3 unten |

---

## Problem
```
ModuleNotFoundError: No module named 'app'
```

## Ursachen und Lösungen

### 1. ✅ PRÜFE: Sind die Dateien hochgeladen?

**In PythonAnywhere Bash Console:**
```bash
cd /home/kajetankonrad
ls -la
```

**Erwartetes Ergebnis:** Du solltest einen Ordner sehen (z.B. `Einfaches-CRM_Konrad` oder `mysite`)

**Falls KEIN Projektordner existiert:**

#### Option A: Git Clone (Empfohlen)
```bash
cd /home/kajetankonrad
git clone https://DEINE-GIT-URL-HIER.git Einfaches-CRM_Konrad
```

#### Option B: Manuell hochladen
1. Gehe zum "Files" Tab in PythonAnywhere
2. Navigiere zu `/home/kajetankonrad/`
3. Erstelle einen Ordner `Einfaches-CRM_Konrad`
4. Lade ALLE Projektdateien hoch, besonders:
   - `app/` Ordner (mit allen Python-Dateien)
   - `templates/` Ordner
   - `static/` Ordner
   - `requirements.txt`
   - `config.py`

### 2. ✅ PRÜFE: Ist der `app` Ordner vorhanden?

**In PythonAnywhere Bash Console:**
```bash
cd /home/kajetankonrad/Einfaches-CRM_Konrad
ls -la
```

**Du MUSST folgendes sehen:**
```
drwxr-xr-x  2 kajetankonrad registered_users 4096 Nov 12 12:00 app
drwxr-xr-x  2 kajetankonrad registered_users 4096 Nov 12 12:00 static
drwxr-xr-x  2 kajetankonrad registered_users 4096 Nov 12 12:00 templates
-rw-r--r--  1 kajetankonrad registered_users  xxx Nov 12 12:00 config.py
-rw-r--r--  1 kajetankonrad registered_users  xxx Nov 12 12:00 requirements.txt
```

**Falls `app/` fehlt:**
- Du hast die Dateien nicht hochgeladen!
- Lade sie jetzt hoch (siehe Schritt 1)

**Prüfe den Inhalt von `app/`:**
```bash
cd /home/kajetankonrad/Einfaches-CRM_Konrad/app
ls -la
```

**Du MUSST sehen:**
```
-rw-r--r--  1 kajetankonrad registered_users xxx __init__.py
-rw-r--r--  1 kajetankonrad registered_users xxx models.py
-rw-r--r--  1 kajetankonrad registered_users xxx routes.py
-rw-r--r--  1 kajetankonrad registered_users xxx extensions.py
```

### 3. ✅ KORRIGIERE: Den Pfad in der WSGI-Datei

**Finde heraus, wo deine Dateien WIRKLICH liegen:**

```bash
# Suche nach dem app Ordner
find /home/kajetankonrad -type d -name "app" 2>/dev/null
```

**Mögliche Pfade:**
- `/home/kajetankonrad/Einfaches-CRM_Konrad/app`
- `/home/kajetankonrad/mysite/app`
- `/home/kajetankonrad/einfaches-crm_konrad/app`

**Wenn der Pfad z.B. `/home/kajetankonrad/mysite/app` ist:**

1. Öffne die WSGI-Datei in PythonAnywhere
2. Ändere Zeile 12:
   ```python
   project_home = '/home/kajetankonrad/mysite'  # NICHT /mysite/app !
   ```
3. Speichere die Datei
4. Reload die Web App

### 4. ✅ PRÜFE: Python-Pfad in sys.path

**Füge am Ende der WSGI-Datei (VOR `from app import create_app`) hinzu:**

```python
# DEBUGGING: Zeige sys.path
print("=" * 60)
print("DEBUGGING INFORMATION")
print("=" * 60)
print(f"Current working directory: {os.getcwd()}")
print(f"Project home: {project_home}")
print(f"Project home exists: {os.path.exists(project_home)}")
print(f"\nPython sys.path:")
for path in sys.path:
    print(f"  - {path}")

# Zeige Dateien im Projekt
if os.path.exists(project_home):
    print(f"\nFiles in {project_home}:")
    for item in os.listdir(project_home):
        item_path = os.path.join(project_home, item)
        if os.path.isdir(item_path):
            print(f"  [DIR]  {item}")
        else:
            print(f"  [FILE] {item}")
    
    # Zeige app Ordner Inhalt
    app_path = os.path.join(project_home, 'app')
    if os.path.exists(app_path):
        print(f"\nFiles in {app_path}:")
        for item in os.listdir(app_path):
            print(f"  - {item}")
    else:
        print(f"\nERROR: app folder NOT FOUND at {app_path}")
else:
    print(f"\nERROR: Project home NOT FOUND at {project_home}")
print("=" * 60)
```

**Dann:**
1. Speichere die WSGI-Datei
2. Reload die Web App
3. Schaue ins **Error Log**
4. Du siehst jetzt genau, was fehlt!

### 5. ✅ INSTALLIERE: Alle Requirements

**In PythonAnywhere Bash Console:**

```bash
cd /home/kajetankonrad/Einfaches-CRM_Konrad
workon crm-env  # oder wie dein virtualenv heißt
pip install -r requirements.txt
```

**Wichtig:** Prüfe ob PyMySQL installiert ist:
```bash
pip list | grep -i mysql
```

Du solltest sehen:
```
PyMySQL     x.x.x
```

Falls nicht:
```bash
pip install PyMySQL
```

### 6. ✅ VIRTUALENV: Richtig konfiguriert?

**Im Web Tab:**
1. Scrolle zu "Virtualenv"
2. Trage ein: `/home/kajetankonrad/.virtualenvs/crm-env`
3. Klicke das Häkchen zum Speichern

**Falls du noch KEIN Virtualenv hast:**

```bash
# In PythonAnywhere Bash Console
mkvirtualenv --python=/usr/bin/python3.10 crm-env
workon crm-env
cd /home/kajetankonrad/Einfaches-CRM_Konrad
pip install -r requirements.txt
```

## 🎯 SCHNELLE FIX-ANLEITUNG

**Führe diese Schritte der Reihe nach aus:**

1. **Prüfe Dateien:**
   ```bash
   cd /home/kajetankonrad
   ls -la
   ```

2. **Falls Projekt fehlt, hochladen/clonen**

3. **Prüfe app Ordner:**
   ```bash
   ls -la */app/
   ```

4. **Notiere den richtigen Pfad** (z.B. `/home/kajetankonrad/ORDNERNAME`)

5. **Öffne WSGI-Datei** und ändere `project_home`

6. **Speichere** und **Reload**

7. **Prüfe Error Log**

## 📝 VOLLSTÄNDIGE WSGI-DATEI (Beispiel)

Hier ist eine funktionierende WSGI-Datei mit Debugging:

```python
import sys
import os

# PFAD ANPASSEN!
project_home = '/home/kajetankonrad/Einfaches-CRM_Konrad'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

# DEBUGGING
print("=" * 60)
print(f"Project: {project_home}")
print(f"Exists: {os.path.exists(project_home)}")
if os.path.exists(project_home):
    print(f"Contents: {os.listdir(project_home)}")
print("=" * 60)

# Umgebungsvariablen
os.environ['SECRET_KEY'] = 'DEIN-GEHEIMER-KEY'
os.environ['FLASK_ENV'] = 'production'
os.environ['DEBUG'] = 'False'
os.environ['DATABASE_URL'] = 'mysql+pymysql://kajetankonrad:PASSWORT@kajetankonrad.mysql.pythonanywhere-services.com/kajetankonrad$crm'

# App laden
from app import create_app
application = create_app()
```

## 🆘 Immer noch Fehler?

### Neue Diagnose-Features (ab Version 2.0)

**Die WSGI-Dateien in diesem Projekt enthalten jetzt automatische Diagnostik!**

Wenn Sie die aktualisierte WSGI-Datei verwenden, sehen Sie im Error Log:
- ✅ Welcher Pfad konfiguriert ist
- ✅ Ob das Projektverzeichnis existiert
- ✅ Ob der app Ordner gefunden wurde
- ✅ Welche Dateien im Projekt vorhanden sind
- ✅ Python sys.path Einträge

**So nutzen Sie die Diagnostik:**
1. Kopieren Sie den Inhalt von `kajetankonrad_pythonanywhere_com_wsgi.py` in Ihre WSGI-Datei
2. Passen Sie NUR die `project_home` Variable an (Zeile 14)
3. Reload Ihrer Web App
4. Öffnen Sie das Error Log
5. Die Diagnose zeigt Ihnen GENAU wo das Problem ist!

**Beispiel Error Log Output:**
```
======================================================================
🔧 PYTHONANYWHERE WSGI DIAGNOSTICS
======================================================================
📁 Project home: /home/kajetankonrad/Einfaches-CRM_Konrad
✓  Project exists: True
🐍 Python version: 3.10.x
📌 Current working directory: /var/www

📂 Files in project directory:
   [DIR]  app/
   [DIR]  static/
   [DIR]  templates/
   [FILE] config.py
   [FILE] requirements.txt
   
📦 App folder check:
   Path: /home/kajetankonrad/Einfaches-CRM_Konrad/app
   Exists: True
   ✅ App folder found!
======================================================================
```

---

## 🆘 Weitere Hilfe benötigt?

**Schicke mir diese Informationen:**

1. Output von:
   ```bash
   cd /home/kajetankonrad
   find . -type d -name "app"
   ```

2. Output von:
   ```bash
   ls -la /home/kajetankonrad/
   ```

3. Den kompletten Error Log (letzte 50 Zeilen)

4. Deine aktuelle WSGI-Datei

---

**Die Lösung ist fast immer: Falscher Pfad oder Dateien nicht hochgeladen!** ✅
