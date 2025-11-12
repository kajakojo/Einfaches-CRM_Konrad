# PythonAnywhere Deployment Anleitung für kajetankonrad

## 📋 SCHRITT-FÜR-SCHRITT ANLEITUNG

### 1. Projekt auf PythonAnywhere hochladen

#### Option A: Via Git (Empfohlen)
```bash
# In der PythonAnywhere Bash Console
cd ~
git clone https://github.com/IhrUsername/Einfaches-CRM_Konrad.git
```

#### Option B: Dateien hochladen
- Nutzen Sie den "Files" Tab in PythonAnywhere
- Laden Sie alle Projektdateien hoch nach: `/home/kajetankonrad/Einfaches-CRM_Konrad`

### 2. Virtual Environment erstellen

```bash
# In der PythonAnywhere Bash Console
cd ~/Einfaches-CRM_Konrad
mkvirtualenv --python=/usr/bin/python3.10 crm-env
workon crm-env
pip install -r requirements.txt
```

### 3. MySQL-Datenbank erstellen

1. Gehen Sie zum "Databases" Tab in PythonAnywhere
2. Setzen Sie ein MySQL-Passwort (falls noch nicht geschehen)
3. Erstellen Sie eine neue Datenbank namens: `kajetankonrad$crm`
4. Notieren Sie sich das MySQL-Passwort!

### 4. WSGI-Datei konfigurieren

1. Gehen Sie zum "Web" Tab in PythonAnywhere
2. Erstellen Sie eine neue Web App (Flask, Python 3.10)
3. Klicken Sie auf die WSGI-Konfigurationsdatei: `/var/www/kajetankonrad_pythonanywhere_com_wsgi.py`
4. **LÖSCHEN Sie den gesamten Inhalt** der Datei
5. **KOPIEREN Sie den kompletten Inhalt** aus der Datei `kajetankonrad_pythonanywhere_com_wsgi.py` (die ich gerade erstellt habe)
6. **WICHTIG:** Ändern Sie in Zeile 33:
   ```python
   os.environ['DATABASE_URL'] = 'mysql+pymysql://kajetankonrad:IhrMySQLPasswort@...'
   ```
   Ersetzen Sie `IhrMySQLPasswort` mit Ihrem echten MySQL-Passwort!

7. **WICHTIG:** Ändern Sie in Zeile 25 den Secret Key zu einem sicheren Wert:
   ```python
   os.environ['SECRET_KEY'] = 'einen-sehr-sicheren-zufaelligen-string-hier'
   ```
   Generieren Sie einen sicheren Key z.B. mit:
   ```python
   import secrets
   print(secrets.token_hex(32))
   ```

8. Speichern Sie die Datei (Strg+S oder Button "Save")

### 5. Virtualenv in Web App konfigurieren

1. Im "Web" Tab, finden Sie den Abschnitt "Virtualenv"
2. Geben Sie ein: `/home/kajetankonrad/.virtualenvs/crm-env`
3. Klicken Sie auf das Häkchen zum Speichern

### 6. Static Files konfigurieren

Im "Web" Tab unter "Static files":

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/kajetankonrad/Einfaches-CRM_Konrad/static` |

### 7. Datenbank initialisieren

```bash
# In der PythonAnywhere Bash Console
cd ~/Einfaches-CRM_Konrad
workon crm-env
python init_db.py
```

### 8. Web App neu starten

1. Gehen Sie zum "Web" Tab
2. Klicken Sie auf den grünen Button "Reload kajetankonrad.pythonanywhere.com"

### 9. Testen

Öffnen Sie: https://kajetankonrad.pythonanywhere.com

## 🔧 TROUBLESHOOTING

### Error Log prüfen
Im "Web" Tab gibt es Links zu:
- Error log: Zeigt Python-Fehler
- Server log: Zeigt HTTP-Requests
- Access log: Zeigt alle Zugriffe

### Häufige Probleme

#### "Import Error: No module named 'app'"
- Prüfen Sie, ob der Pfad in der WSGI-Datei korrekt ist
- Stellen Sie sicher, dass alle Dateien hochgeladen wurden

#### "Database connection error"
- Prüfen Sie das MySQL-Passwort in der WSGI-Datei
- Stellen Sie sicher, dass die Datenbank `kajetankonrad$crm` existiert
- Prüfen Sie, ob PyMySQL installiert ist: `pip list | grep PyMySQL`

#### "500 Internal Server Error"
- Schauen Sie ins Error Log
- Stellen Sie sicher, dass `python-dotenv` NICHT in requirements.txt steht (wird auf PythonAnywhere nicht benötigt)

#### Static Files werden nicht geladen
- Prüfen Sie die Static Files Konfiguration im "Web" Tab
- Pfad muss exakt sein: `/home/kajetankonrad/Einfaches-CRM_Konrad/static`

### Debugging aktivieren (NUR für Entwicklung!)

Falls Sie Fehler debuggen müssen, ändern Sie temporär in der WSGI-Datei:
```python
os.environ['DEBUG'] = 'True'
```
**WICHTIG:** Deaktivieren Sie Debug in Produktion wieder!

## 📝 WICHTIGE HINWEISE

1. **Niemals** sensible Daten (Passwörter, Keys) in Git committen
2. **Immer** einen sicheren SECRET_KEY verwenden
3. **Regelmäßig** Backups der Datenbank erstellen
4. **Monitoring** des Error Logs für Probleme

## 🔄 UPDATES DEPLOYEN

Wenn Sie Änderungen am Code machen:

```bash
# In der PythonAnywhere Bash Console
cd ~/Einfaches-CRM_Konrad
workon crm-env
git pull  # oder Dateien manuell hochladen
pip install -r requirements.txt  # falls neue Abhängigkeiten
```

Dann im "Web" Tab: "Reload" klicken

## 📞 SUPPORT

Bei Problemen:
- PythonAnywhere Forum: https://www.pythonanywhere.com/forums/
- PythonAnywhere Help: https://help.pythonanywhere.com/

---

**Viel Erfolg beim Deployment! 🚀**
