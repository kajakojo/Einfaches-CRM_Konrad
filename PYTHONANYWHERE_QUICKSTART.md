# 🚀 PythonAnywhere Quick Start Guide

> **⏱️ Zeit:** 15-20 Minuten  
> **💰 Kosten:** Kostenlos (Beginner Account)  
> **✅ Voraussetzungen:** GitHub Account (für Git-Deployment)

---

## 📋 Schritt-für-Schritt Anleitung

### 1️⃣ PythonAnywhere Account erstellen (2 Minuten)

1. Gehe zu https://www.pythonanywhere.com
2. Klicke auf **"Pricing & signup"**
3. Wähle **"Create a Beginner account"** (kostenlos)
4. Registriere dich mit deiner E-Mail
5. Bestätige deine E-Mail-Adresse

✅ **Fertig!** Du bist jetzt eingeloggt im PythonAnywhere Dashboard

---

### 2️⃣ MySQL-Datenbank einrichten (3 Minuten)

1. Klicke im Dashboard auf **"Databases"**
2. Scrolle zu **"MySQL"**
3. Gib ein sicheres Passwort ein
4. Klicke **"Initialize MySQL"**
5. **⚠️ WICHTIG:** Notiere dir das Passwort!

**Datenbank erstellen:**
6. Scrolle zu **"Create database"**
7. Gib ein: `crm`
8. Klicke **"Create"**

✅ **Deine Datenbank heißt jetzt:** `deinbenutzername$crm`

---

### 3️⃣ Projekt hochladen (5 Minuten)

#### Option A: Git Clone (empfohlen)

1. Klicke im Dashboard auf **"Consoles"**
2. Starte eine **"Bash console"**
3. Führe aus:

```bash
cd ~
git clone https://github.com/kajakojo/Einfaches-CRM_Konrad.git
cd Einfaches-CRM_Konrad
```

#### Option B: Manueller Upload

1. Klicke auf **"Files"**
2. Navigiere zu `/home/deinbenutzername/`
3. Lade alle Projektdateien hoch

✅ **Projekt ist hochgeladen!**

---

### 4️⃣ Virtuelle Umgebung erstellen (3 Minuten)

In der **Bash Console**:

```bash
cd ~/Einfaches-CRM_Konrad
mkvirtualenv --python=/usr/bin/python3.10 crm-venv
pip install -r requirements.txt
```

⏳ **Warte bis die Installation abgeschlossen ist (~2 Minuten)**

✅ **Dependencies installiert!**

---

### 5️⃣ Web-App erstellen (2 Minuten)

1. Klicke im Dashboard auf **"Web"**
2. Klicke **"Add a new web app"**
3. Wähle deinen Domain-Namen: `deinbenutzername.pythonanywhere.com`
4. Wähle **"Manual configuration"** (⚠️ NICHT Flask!)
5. Wähle **"Python 3.10"**

✅ **Web-App erstellt!**

---

### 6️⃣ WSGI-Datei konfigurieren (5 Minuten)

**WICHTIGSTER SCHRITT!**

1. Auf der **Web**-Seite, scrolle zu **"Code"**
2. Klicke auf den WSGI-Datei Link (z.B. `/var/www/deinbenutzername_pythonanywhere_com_wsgi.py`)
3. **LÖSCHE** den gesamten Inhalt
4. **KOPIERE** den Inhalt von `kajetankonrad_pythonanywhere_com_wsgi.py` aus deinem Projekt
5. **PASSE AN:**
   - Zeile 14: Ändere `/home/kajetankonrad/` zu `/home/deinbenutzername/`
   - Zeile 70: Setze deinen SECRET_KEY (siehe unten)
   - Zeile 79: Setze deine MySQL-Zugangsdaten (siehe unten)

**SECRET_KEY generieren:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Kopiere die Ausgabe und füge sie in Zeile 70 ein.

**MySQL-Zugangsdaten (Zeile 79):**
```python
os.environ['DATABASE_URL'] = 'mysql+pymysql://deinbenutzername:DeinMySQLPasswort@deinbenutzername.mysql.pythonanywhere-services.com/deinbenutzername$crm'
```

6. Klicke **"Save"**

---

### 7️⃣ Virtualenv verlinken (1 Minute)

1. Auf der **Web**-Seite, scrolle zu **"Virtualenv"**
2. Gib ein: `/home/deinbenutzername/.virtualenvs/crm-venv`
3. Drücke **Enter** (grünes Häkchen erscheint)

---

### 8️⃣ Static Files konfigurieren (1 Minute)

1. Scrolle zu **"Static files"**
2. Klicke **"Add a new static file mapping"**
3. **URL:** `/static/`
4. **Directory:** `/home/deinbenutzername/Einfaches-CRM_Konrad/static`
5. Klicke das Häkchen zum Speichern

---

### 9️⃣ Datenbank initialisieren (2 Minuten)

In der **Bash Console**:

```bash
workon crm-venv
cd ~/Einfaches-CRM_Konrad

# Setze Umgebungsvariablen (temporär)
export DATABASE_URL='mysql+pymysql://deinbenutzername:DeinPasswort@deinbenutzername.mysql.pythonanywhere-services.com/deinbenutzername$crm'
export SECRET_KEY='dein-generierter-key'

# Initialisiere Datenbank
python init_db.py
```

✅ **Datenbank initialisiert!**

---

### 🔟 Web-App starten (1 Minute)

1. Gehe zurück zur **Web**-Seite
2. Klicke den grünen **"Reload"** Button oben rechts
3. Warte ~10 Sekunden
4. Klicke auf deinen Domain-Link

🎉 **FERTIG! Deine App läuft!**

---

## ❓ Probleme?

### ❌ "Internal Server Error"

1. Gehe zu **Web** → **Log files** → **Error log**
2. Scrolle nach unten
3. Suche nach der **DIAGNOSTICS** Ausgabe (zwischen `====` Linien)

**Die Diagnostik zeigt dir:**
- ✅ Ob der Projektpfad korrekt ist
- ✅ Ob der app Ordner gefunden wurde
- ✅ Welche Dateien im Projekt sind
- ❌ Was genau fehlt

### Häufige Fehler:

| Error | Lösung |
|-------|--------|
| `App folder NOT FOUND` | Projekt nicht hochgeladen → Schritt 3 wiederholen |
| `Project directory does not exist` | Pfad in WSGI-Datei falsch → Zeile 14 korrigieren |
| `Access denied for user` | MySQL-Passwort falsch → Zeile 79 in WSGI korrigieren |
| `No module named 'pymysql'` | Dependencies fehlen → Schritt 4 wiederholen |

---

## 📖 Weitere Dokumentation

- **Detaillierte Anleitung:** `PYTHONANYWHERE_DEPLOYMENT.md`
- **Fehlerbehebung:** `TROUBLESHOOTING_PYTHONANYWHERE.md`
- **Projekt-Status:** `PROJECT_STATUS.md`

---

## 💡 Tipps

- **Kostenloser Account:** Alle 3 Monate verlängern (kostenlos)
- **Nach Änderungen:** Immer "Reload" Button klicken
- **Bei Problemen:** Error Log ist dein Freund!
- **Backups:** Regelmäßig mit `mysqldump` erstellen

---

**Viel Erfolg! 🚀**
