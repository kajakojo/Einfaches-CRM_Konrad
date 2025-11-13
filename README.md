# CRM System

Einfaches Customer Relationship Management System mit Flask und MySQL.

**Live Demo:** [kajetankonrad.pythonanywhere.com](https://kajetankonrad.pythonanywhere.com)

---

## 🚀 In 5 Minuten online hosten (PythonAnywhere)

### 1. Account erstellen
- Gehe zu [pythonanywhere.com](https://www.pythonanywhere.com) → Kostenlosen Account erstellen

### 2. Datenbank erstellen
- Tab **"Databases"** → MySQL Passwort setzen → Datenbank `username$default` erstellen

### 3. Code hochladen
Bash Console öffnen:
```bash
git clone https://github.com/kajakojo/Einfaches-CRM_Konrad.git crmproject
cd crmproject
pip3.13 install --user -r requirements.txt
```

### 4. Web App einrichten
- Tab **"Web"** → "Add a new web app" → **Manual Configuration** → **Python 3.13**

### 5. WSGI Datei anpassen
WSGI configuration file öffnen, alles löschen und einfügen:

```python
import sys, os
project_home = '/home/USERNAME/crmproject'
sys.path.insert(0, project_home)

os.environ['SECRET_KEY'] = 'irgendeinlangertext123'
os.environ['DATABASE_URL'] = 'mysql+pymysql://USERNAME:PASSWORT@USERNAME.mysql.pythonanywhere-services.com/USERNAME$default'

from app import create_app
application = create_app()
```

**Ersetze:** `USERNAME` (3x) und `PASSWORT` mit deinen Daten!

### 6. Fertig!
**"Reload"** Button klicken → Fertig! 🎉

---

## � Lokal testen

```bash
git clone https://github.com/kajakojo/Einfaches-CRM_Konrad.git
cd Einfaches-CRM_Konrad
pip install -r requirements.txt
python start_local.py
```

Öffne: `http://127.0.0.1:5000`

---

## � Code aktualisieren

**Lokal:** `git push`  
**PythonAnywhere Bash Console:** `cd ~/crmproject && git pull`  
**Web Tab:** "Reload" klicken

---

Erstellt von **Kajetan Konrad** - TGM Wien