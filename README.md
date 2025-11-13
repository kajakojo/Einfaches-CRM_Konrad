# Einfaches CRM System 📊

Ein einfaches Customer Relationship Management (CRM) System mit Flask und MySQL.

## 🌐 Live Demo

**Jetzt online:** [https://kajetankonrad.pythonanywhere.com](https://kajetankonrad.pythonanywhere.com)

---

## 🚀 Lokale Installation (zum Testen)

```bash
# Repository klonen
git clone https://github.com/kajakojo/Einfaches-CRM_Konrad.git
cd Einfaches-CRM_Konrad

# Abhängigkeiten installieren
pip install -r requirements.txt

# Lokal starten
python start_local.py
```

Öffne dann: `http://127.0.0.1:5000`

---

## 🌍 PythonAnywhere Hosting - Komplette Anleitung

### 1️⃣ Account erstellen
- Gehe zu [www.pythonanywhere.com](https://www.pythonanywhere.com)
- Erstelle einen **kostenlosen Beginner Account**
- Merke dir deinen Benutzernamen (z.B. `maxmuster`)

### 2️⃣ MySQL Datenbank erstellen
1. Tab **"Databases"** öffnen
2. MySQL Passwort setzen und merken ✏️
3. Neue Datenbank erstellen: `maxmuster$default`

### 3️⃣ Code hochladen
Öffne eine **Bash Console** (Tab "Consoles"):

```bash
# Repository klonen
git clone https://github.com/kajakojo/Einfaches-CRM_Konrad.git crmproject
cd crmproject

# Pakete installieren
pip3.13 install --user -r requirements.txt
```

### 4️⃣ Web App erstellen
1. Tab **"Web"** öffnen
2. **"Add a new web app"** klicken
3. Auswählen: **Manual Configuration** → **Python 3.13**

### 5️⃣ WSGI Datei konfigurieren
1. Im "Web" Tab auf **WSGI configuration file** klicken
2. **GESAMTEN Inhalt löschen** ❌
3. Folgenden Code einfügen:

```python
import sys
import os

# ⚠️ WICHTIG: Ersetze 'maxmuster' mit deinem Benutzernamen!
project_home = '/home/maxmuster/crmproject'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

# ⚠️ WICHTIG: Trage deine eigenen Daten ein!
os.environ['SECRET_KEY'] = 'ZufälligerGeheimSchlüssel123ABC'
os.environ['FLASK_ENV'] = 'production'
os.environ['DEBUG'] = 'False'

# ⚠️ WICHTIG: Ersetze alle 3x 'maxmuster' und 'deinpasswort'!
os.environ['DATABASE_URL'] = 'mysql+pymysql://maxmuster:deinpasswort@maxmuster.mysql.pythonanywhere-services.com/maxmuster$default'

from app import create_app
application = create_app()
```

4. **Ersetzen:**
   - `maxmuster` → dein Benutzername (3x!)
   - `deinpasswort` → dein MySQL Passwort
   - `ZufälligerGeheimSchlüssel...` → beliebiger langer Text

5. **Save** klicken 💾

### 6️⃣ Static Files einrichten
Im "Web" Tab unter **"Static files"**:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/maxmuster/crmproject/static` |

*(Ersetze `maxmuster` mit deinem Benutzernamen!)*

### 7️⃣ App starten
1. Grünen Button **"Reload maxmuster.pythonanywhere.com"** klicken
2. Warte 10 Sekunden ⏱️
3. Besuche: `https://maxmuster.pythonanywhere.com`

**✅ Fertig! Deine CRM-App läuft jetzt online!**

---

## 🔄 Code Updates (nach Änderungen)

### Auf deinem Computer:
```bash
git add .
git commit -m "Beschreibung der Änderung"
git push
```

### Auf PythonAnywhere (Bash Console):
```bash
cd ~/crmproject
git pull
```

Dann im **Web Tab**: Grünen **"Reload"** Button klicken!

---

## 📁 Projektstruktur

```
Einfaches-CRM_Konrad/
├── app/
│   ├── __init__.py          # Flask App
│   ├── models.py            # Datenbank
│   ├── routes.py            # URLs
│   └── extensions.py        # Extensions
├── templates/               # HTML
├── static/                  # CSS/JS
├── requirements.txt         # Pakete
├── start_local.py          # Lokal starten
└── kajetankonrad_pythonanywhere_com_wsgi.py  # WSGI
```

---

## 🐛 Probleme lösen

### ❌ "Something went wrong"
1. PythonAnywhere → Tab **"Web"**
2. Klicke auf **"Error log"**
3. Letzte Zeilen lesen

### ❌ Datenbank-Fehler
✔️ WSGI-Datei prüfen: Benutzername/Passwort richtig?  
✔️ Datenbank existiert? (Tab "Databases")

### ❌ Module nicht gefunden
```bash
# In PythonAnywhere Bash Console:
cd ~/crmproject
pip3.13 install --user -r requirements.txt
```

---

## 💡 Wichtige Hinweise

- 🆓 **Kostenloser Account**: Website "schläft" nach Inaktivität (täglich Reload nötig)
- 🔒 **HTTPS**: Automatisch von PythonAnywhere bereitgestellt
- 🌐 **Domain**: `deinusername.pythonanywhere.com`

---

## 📝 Features

✅ Kunden verwalten  
✅ Aufträge tracken  
✅ Kontakte speichern  
✅ Projekte organisieren  
✅ MySQL Datenbank  

---

## 👤 Autor

**Kajetan Konrad** - TGM Wien

---

## 📄 Lizenz

Dieses Projekt wurde für Bildungszwecke erstellt.