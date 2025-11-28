from app import create_app
from app.extensions import db
import os

def main():
    app = create_app()
    
    # Erstelle die Datenbank-Tabellen, falls sie nicht existieren
    with app.app_context():
        db.create_all()
        print("Datenbank-Tabellen wurden erstellt/überprüft.")
    
    # Starte die Anwendung
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()