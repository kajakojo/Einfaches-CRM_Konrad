# CRM System# CRM System



**Live:** [kajetankonrad.pythonanywhere.com](https://kajetankonrad.pythonanywhere.com)Einfaches Customer Relationship Management System mit Flask und MySQL.



## Hosting (PythonAnywhere)**Live Demo:** [kajetankonrad.pythonanywhere.com](https://kajetankonrad.pythonanywhere.com)



**1.** [pythonanywhere.com](https://www.pythonanywhere.com) → Account erstellen---



**2.** Tab "Databases" → MySQL Passwort → Datenbank `username$default`## 🚀 In 5 Minuten online hosten (PythonAnywhere)



**3.** Bash Console:### 1. Account erstellen

```bash- Gehe zu [pythonanywhere.com](https://www.pythonanywhere.com) → Kostenlosen Account erstellen

git clone https://github.com/kajakojo/Einfaches-CRM_Konrad.git crmproject

cd crmproject### 2. Datenbank erstellen

pip3.13 install --user -r requirements.txt- Tab **"Databases"** → MySQL Passwort setzen → Datenbank `username$default` erstellen

```

### 3. Code hochladen

**4.** Tab "Web" → "Add new" → Manual Config → Python 3.13Bash Console öffnen:

```bash

**5.** WSGI File (alles löschen, einfügen):git clone https://github.com/kajakojo/Einfaches-CRM_Konrad.git crmproject

```pythoncd crmproject

import sys, ospip3.13 install --user -r requirements.txt

project_home = '/home/USERNAME/crmproject'```

sys.path.insert(0, project_home)

os.environ['SECRET_KEY'] = 'irgendeinlangertext123'### 4. Web App einrichten

os.environ['DATABASE_URL'] = 'mysql+pymysql://USERNAME:PASSWORT@USERNAME.mysql.pythonanywhere-services.com/USERNAME$default'- Tab **"Web"** → "Add a new web app" → **Manual Configuration** → **Python 3.13**

from app import create_app

application = create_app()### 5. WSGI Datei anpassen

```WSGI configuration file öffnen, alles löschen und einfügen:

Ersetze `USERNAME` (3x) + `PASSWORT`

```python

**6.** Reload → Fertig! 🎉import sys, os

project_home = '/home/USERNAME/crmproject'

---sys.path.insert(0, project_home)



Kajetan Konrad - TGM Wienos.environ['SECRET_KEY'] = 'irgendeinlangertext123'

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