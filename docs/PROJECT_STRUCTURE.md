# Projektstruktur - Einfaches CRM

## Hauptverzeichnis
```
Einfaches-CRM_Konrad/
│
├── app/                    # Flask Anwendung
│   ├── __init__.py         # App Factory
│   ├── models.py           # Datenbankmodelle
│   ├── routes.py           # Route Handler
│   ├── extensions.py       # Flask Extensions
│   └── utils.py            # Hilfsfunktionen
│
├── templates/              # HTML Templates
│   ├── base.html
│   ├── index.html
│   ├── contacts/           # Kontakt Templates
│   ├── customers/          # Kunden Templates
│   ├── orders/             # Aufträge Templates
│   ├── projects/           # Projekte Templates
│   ├── tasks/              # Aufgaben Templates
│   └── accounting/         # Buchhaltung Templates
│
├── static/                 # CSS, JS, Bilder
│   ├── style.css
│   └── smartcrm.css
│
├── scripts/                # Hilfsskripte
│   ├── init_db.py          # Datenbank initialisieren
│   ├── manage.py           # Management Commands
│   ├── test_app.py         # Tests
│   ├── setup_pythonanywhere.sh
│   ├── fix_pythonanywhere.sh
│   ├── diagnose_pythonanywhere.sh
│   └── QUICK_FIX.sh
│
├── docs/                   # Dokumentation
│   ├── Hosting-Anleitung/  # Alte Hosting Anleitung
│   ├── CHANGES_PYTHONANYWHERE.md
│   ├── COMMANDS_TO_RUN.txt
│   ├── COMPLETE_FIX_GUIDE.md
│   ├── FIX_PYTHON_VERSION.txt
│   ├── TROUBLESHOOTING_PYTHONANYWHERE.md
│   └── PROJECT_STATUS.md
│
├── deployment/             # Deployment Konfiguration
│   └── (WSGI-Dateien für Server)
│
├── config.py               # App Konfiguration
├── requirements.txt        # Python Dependencies
├── run.py                  # Lokaler Development Server
├── start_local.py          # Alternative zum Starten
├── .env                    # Umgebungsvariablen (nicht in Git!)
├── .env.example            # Beispiel für .env
├── .gitignore              # Git Ignore Rules
└── README.md               # Hauptdokumentation

# Ausgeschlossen von Git:
├── venv/                   # Virtual Environment
└── __pycache__/            # Python Cache
```

## Wichtige Dateien

### Kernapplikation
- **app/__init__.py**: Flask Factory Pattern, erstellt die App-Instanz
- **app/models.py**: SQLAlchemy Models (Contact, Customer, Order, Project, Task)
- **app/routes.py**: Alle Route Handler und View-Logik
- **config.py**: Datenbankkonfiguration, Secret Key, SQLALCHEMY Optionen

### Deployment
- **run.py**: Startet Flask Development Server lokal
- **requirements.txt**: Alle Python-Abhängigkeiten
- **deployment/**: WSGI-Dateien für PythonAnywhere

### Entwicklung
- **scripts/init_db.py**: Erstellt alle Datenbanktabellen
- **scripts/test_app.py**: Unit Tests
- **.env**: Umgebungsvariablen (SECRET_KEY, DATABASE_URL)

## Verwendung

### Lokal starten:
```bash
python run.py
```

### Datenbank initialisieren:
```bash
python scripts/init_db.py
```

### Tests ausführen:
```bash
python scripts/test_app.py
```

## Deployment auf PythonAnywhere
Siehe **README.md** für vollständige Anleitung.
