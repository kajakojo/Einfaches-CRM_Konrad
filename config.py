import os
from dotenv import load_dotenv

# Lade Umgebungsvariablen aus .env Datei
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Datenbank-Konfiguration für das CRM-System
    
    Diese Konfiguration liest die Datenbankzugangsdaten aus der .env Datei.
    Der Benutzer trägt seine eigenen Zugangsdaten laut Installationsanleitung ein.
    
    Unterstützte Datenbanken:
    - SQLite (Standard, keine zusätzliche Installation nötig)
    - MySQL/MariaDB
    - PostgreSQL
    """
    
    # Flask Sicherheitsschlüssel
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-please-change-in-production')
    
    # Debug-Modus
    DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1', 'yes')
    
    # Template Auto-Reload
    TEMPLATES_AUTO_RELOAD = True
    
    # SQLAlchemy-Konfiguration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Datenbank-URI Konstruktion
    @staticmethod
    def get_database_uri():
        """
        Erstellt die Datenbank-URI basierend auf den Umgebungsvariablen.
        
        Falls DATABASE_URL gesetzt ist, wird diese direkt verwendet.
        Ansonsten wird die URI aus DB_TYPE, DB_USER, DB_PASSWORD, etc. zusammengesetzt.
        """
        # Direkte DATABASE_URL hat Vorrang
        database_url = os.getenv('DATABASE_URL')
        if database_url:
            return database_url
        
        # Ansonsten aus einzelnen Komponenten zusammensetzen
        db_type = os.getenv('DB_TYPE', 'sqlite')
        
        if db_type.lower() == 'sqlite':
            # SQLite-Datenbank (Standard)
            db_name = os.getenv('DB_NAME', 'app.db')
            return f'sqlite:///{os.path.join(basedir, db_name)}'
        
        elif db_type.lower() in ('mysql', 'mariadb'):
            # MySQL/MariaDB-Datenbank
            db_user = os.getenv('DB_USER', 'root')
            db_password = os.getenv('DB_PASSWORD', '')
            db_host = os.getenv('DB_HOST', 'localhost')
            db_port = os.getenv('DB_PORT', '3306')
            db_name = os.getenv('DB_NAME', 'crm_database')
            
            return f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        
        elif db_type.lower() in ('postgresql', 'postgres'):
            # PostgreSQL-Datenbank
            db_user = os.getenv('DB_USER', 'postgres')
            db_password = os.getenv('DB_PASSWORD', '')
            db_host = os.getenv('DB_HOST', 'localhost')
            db_port = os.getenv('DB_PORT', '5432')
            db_name = os.getenv('DB_NAME', 'crm_database')
            
            return f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        
        else:
            # Fallback auf SQLite
            return f'sqlite:///{os.path.join(basedir, "app.db")}'
    
    # Setze die SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI = get_database_uri.__func__()