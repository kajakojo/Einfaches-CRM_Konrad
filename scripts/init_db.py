#!/usr/bin/env python
"""
Datenbank-Initialisierungsskript für PythonAnywhere

Dieses Skript erstellt alle Datenbanktabellen und fügt optional Beispieldaten hinzu.

Verwendung:
    python init_db.py

Voraussetzungen:
    - Die DATABASE_URL Umgebungsvariable muss gesetzt sein
    - Oder die .env Datei muss die korrekten Werte enthalten
"""

import os
import sys

def init_database():
    """Initialisiert die Datenbank mit allen Tabellen."""
    
    print("=" * 60)
    print("DATENBANK-INITIALISIERUNG")
    print("=" * 60)
    
    # Importiere die Flask-App
    try:
        from app import create_app
        from app.extensions import db
        from app.models import Customer, Order, Contact, User, Project, Task, ActivityLog
        from datetime import datetime, timedelta
        print("✓ Module erfolgreich importiert")
    except ImportError as e:
        print(f"✗ Fehler beim Importieren: {e}")
        print("\nStellen Sie sicher, dass:")
        print("  1. Sie sich im richtigen Verzeichnis befinden")
        print("  2. Die virtuelle Umgebung aktiviert ist")
        print("  3. Alle Abhängigkeiten installiert sind")
        sys.exit(1)
    
    # Erstelle die Flask-App
    try:
        app = create_app()
        print("✓ Flask-App erstellt")
    except Exception as e:
        print(f"✗ Fehler beim Erstellen der App: {e}")
        sys.exit(1)
    
    # Zeige die Datenbank-URI (ohne Passwort)
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if 'mysql' in db_uri:
        # Verstecke das Passwort in der Ausgabe
        safe_uri = db_uri.split('@')[1] if '@' in db_uri else db_uri
        print(f"✓ Datenbank: MySQL - {safe_uri}")
    else:
        print(f"✓ Datenbank: {db_uri}")
    
    # Erstelle die Tabellen
    with app.app_context():
        try:
            print("\nErstelle Datenbanktabellen...")
            db.create_all()
            print("✓ Tabellen erfolgreich erstellt:")
            print("  - customers")
            print("  - orders")
            print("  - contacts")
        except Exception as e:
            print(f"✗ Fehler beim Erstellen der Tabellen: {e}")
            sys.exit(1)
        
        # Prüfe, ob bereits Daten existieren
        customer_count = Customer.query.count()
        
        if customer_count > 0:
            print(f"\n✓ Datenbank enthält bereits {customer_count} Kunden")
            response = input("\nBeispieldaten hinzufügen? (j/n): ").lower()
            if response != 'j':
                print("\nAbgebrochen. Keine Änderungen vorgenommen.")
                return
        
        # Füge Beispieldaten hinzu
        try:
            print("\nFüge Beispieldaten hinzu...")
            
            # Beispiel-Kunde
            if not Customer.query.filter_by(email='max.mustermann@example.com').first():
                customer1 = Customer(
                    name='Max Mustermann',
                    email='max.mustermann@example.com',
                    phone='+43 1 234 5678'
                )
                db.session.add(customer1)
            
            if not Customer.query.filter_by(email='anna.schmidt@example.com').first():
                customer2 = Customer(
                    name='Anna Schmidt',
                    email='anna.schmidt@example.com',
                    phone='+43 664 123 4567'
                )
                db.session.add(customer2)
            
            if not Customer.query.filter_by(email='firma@beispiel.at').first():
                customer3 = Customer(
                    name='Beispiel GmbH',
                    email='firma@beispiel.at',
                    phone='+43 1 987 6543'
                )
                db.session.add(customer3)
            
            db.session.commit()
            print("✓ Beispielkunden hinzugefügt")
            
            # Beispiel-Aufträge
            customer1 = Customer.query.filter_by(email='max.mustermann@example.com').first()
            if customer1 and not Order.query.filter_by(customer_id=customer1.id).first():
                order1 = Order(
                    customer_id=customer1.id,
                    total=1500.00,
                    description='Website-Entwicklung',
                    status='in_progress'
                )
                db.session.add(order1)
            
            customer3 = Customer.query.filter_by(email='firma@beispiel.at').first()
            if customer3 and not Order.query.filter_by(customer_id=customer3.id).first():
                order2 = Order(
                    customer_id=customer3.id,
                    total=3200.00,
                    description='CRM-System Anpassung',
                    status='completed'
                )
                db.session.add(order2)
            
            db.session.commit()
            print("✓ Beispielaufträge hinzugefügt")
            
            # Beispiel-Kontakte
            if customer1 and not Contact.query.filter_by(customer_id=customer1.id).first():
                contact1 = Contact(
                    customer_id=customer1.id,
                    type='meeting',
                    notes='Erstgespräch geführt. Sehr interessiert an neuer Website. Budget ca. 2000 EUR. Nächster Termin: Angebot erstellen.'
                )
                db.session.add(contact1)
            
            customer2 = Customer.query.filter_by(email='anna.schmidt@example.com').first()
            if customer2 and not Contact.query.filter_by(customer_id=customer2.id).first():
                contact2 = Contact(
                    customer_id=customer2.id,
                    type='email',
                    notes='Email-Anfrage zu Preisen erhalten. Informationen zu verschiedenen Paketen gesendet.'
                )
                db.session.add(contact2)
            
            db.session.commit()
            print("✓ Beispielkontakte hinzugefügt")
            
            # Beispiel-Benutzer
            if not User.query.filter_by(email='admin@smartcrm.at').first():
                admin = User(
                    firstname='Admin',
                    lastname='User',
                    email='admin@smartcrm.at',
                    role='admin'
                )
                db.session.add(admin)
                print("✓ Admin-Benutzer hinzugefügt")
            
            if not User.query.filter_by(email='manager@smartcrm.at').first():
                manager = User(
                    firstname='Maria',
                    lastname='Manager',
                    email='manager@smartcrm.at',
                    role='manager'
                )
                db.session.add(manager)
            
            if not User.query.filter_by(email='employee1@smartcrm.at').first():
                employee1 = User(
                    firstname='Thomas',
                    lastname='Developer',
                    email='employee1@smartcrm.at',
                    role='employee'
                )
                db.session.add(employee1)
            
            if not User.query.filter_by(email='employee2@smartcrm.at').first():
                employee2 = User(
                    firstname='Sarah',
                    lastname='Designer',
                    email='employee2@smartcrm.at',
                    role='employee'
                )
                db.session.add(employee2)
            
            db.session.commit()
            print("✓ Beispielbenutzer hinzugefügt")
            
            # Hole Benutzer für Zuweisungen
            admin_user = User.query.filter_by(email='admin@smartcrm.at').first()
            employee1_user = User.query.filter_by(email='employee1@smartcrm.at').first()
            employee2_user = User.query.filter_by(email='employee2@smartcrm.at').first()
            
            # Beispiel-Projekte
            if customer1 and not Project.query.filter_by(project_name='Website Relaunch').first():
                project1 = Project(
                    project_name='Website Relaunch',
                    customer_id=customer1.id,
                    description='Kompletter Relaunch der Unternehmenswebsite mit modernem Design',
                    status='aktiv',
                    progress=65,
                    start_date=datetime.now() - timedelta(days=30),
                    end_date=datetime.now() + timedelta(days=30)
                )
                db.session.add(project1)
            
            if customer3 and not Project.query.filter_by(project_name='CRM Integration').first():
                project2 = Project(
                    project_name='CRM Integration',
                    customer_id=customer3.id,
                    description='Integration des CRM-Systems mit bestehender ERP-Software',
                    status='geplant',
                    progress=10,
                    start_date=datetime.now() + timedelta(days=7),
                    end_date=datetime.now() + timedelta(days=90)
                )
                db.session.add(project2)
            
            if customer2 and not Project.query.filter_by(project_name='Marketing Kampagne').first():
                project3 = Project(
                    project_name='Marketing Kampagne',
                    customer_id=customer2.id,
                    description='Social Media Kampagne für Produktlaunch',
                    status='aktiv',
                    progress=40,
                    start_date=datetime.now() - timedelta(days=15),
                    end_date=datetime.now() + timedelta(days=45)
                )
                db.session.add(project3)
            
            db.session.commit()
            print("✓ Beispielprojekte hinzugefügt")
            
            # Hole Projekte für Aufgaben
            project1 = Project.query.filter_by(project_name='Website Relaunch').first()
            project2 = Project.query.filter_by(project_name='CRM Integration').first()
            project3 = Project.query.filter_by(project_name='Marketing Kampagne').first()
            
            # Beispiel-Aufgaben
            tasks_added = 0
            if project1 and employee1_user:
                if not Task.query.filter_by(title='Frontend Design erstellen').first():
                    task1 = Task(
                        title='Frontend Design erstellen',
                        description='Mockups und Prototypen für neue Website erstellen',
                        project_id=project1.id,
                        assigned_to=employee2_user.id,
                        priority='hoch',
                        status='erledigt',
                        due_date=datetime.now() - timedelta(days=5)
                    )
                    db.session.add(task1)
                    tasks_added += 1
                
                if not Task.query.filter_by(title='Backend Entwicklung').first():
                    task2 = Task(
                        title='Backend Entwicklung',
                        description='API-Endpunkte und Datenbank-Integration implementieren',
                        project_id=project1.id,
                        assigned_to=employee1_user.id,
                        priority='hoch',
                        status='in_bearbeitung',
                        due_date=datetime.now() + timedelta(days=10)
                    )
                    db.session.add(task2)
                    tasks_added += 1
                
                if not Task.query.filter_by(title='Content Migration').first():
                    task3 = Task(
                        title='Content Migration',
                        description='Bestehende Inhalte auf neue Website übertragen',
                        project_id=project1.id,
                        assigned_to=employee2_user.id,
                        priority='mittel',
                        status='offen',
                        due_date=datetime.now() + timedelta(days=20)
                    )
                    db.session.add(task3)
                    tasks_added += 1
            
            if project2 and employee1_user:
                if not Task.query.filter_by(title='API Spezifikation').first():
                    task4 = Task(
                        title='API Spezifikation',
                        description='Technische Spezifikation für API-Schnittstellen erstellen',
                        project_id=project2.id,
                        assigned_to=employee1_user.id,
                        priority='hoch',
                        status='offen',
                        due_date=datetime.now() + timedelta(days=5)
                    )
                    db.session.add(task4)
                    tasks_added += 1
            
            if project3 and employee2_user:
                if not Task.query.filter_by(title='Social Media Posts').first():
                    task5 = Task(
                        title='Social Media Posts',
                        description='Content für Facebook, Instagram und LinkedIn erstellen',
                        project_id=project3.id,
                        assigned_to=employee2_user.id,
                        priority='mittel',
                        status='in_bearbeitung',
                        due_date=datetime.now() + timedelta(days=7)
                    )
                    db.session.add(task5)
                    tasks_added += 1
                
                if not Task.query.filter_by(title='Analytics Setup').first():
                    task6 = Task(
                        title='Analytics Setup',
                        description='Google Analytics und Conversion Tracking einrichten',
                        project_id=project3.id,
                        assigned_to=employee1_user.id,
                        priority='niedrig',
                        status='offen',
                        due_date=datetime.now() + timedelta(days=14)
                    )
                    db.session.add(task6)
                    tasks_added += 1
            
            # Allgemeine Aufgabe ohne Projekt
            if admin_user and not Task.query.filter_by(title='Quartalsbericht').first():
                task7 = Task(
                    title='Quartalsbericht',
                    description='Bericht über Geschäftsentwicklung Q1 erstellen',
                    assigned_to=admin_user.id,
                    priority='hoch',
                    status='offen',
                    due_date=datetime.now() - timedelta(days=2)  # Überfällig
                )
                db.session.add(task7)
                tasks_added += 1
            
            db.session.commit()
            print(f"✓ {tasks_added} Beispielaufgaben hinzugefügt")
            
            # Beispiel-Aktivitätslog
            if admin_user:
                activities = [
                    ActivityLog(user_id=admin_user.id, action='Projekt erstellt', 
                               details='Website Relaunch', created_at=datetime.now() - timedelta(days=30)),
                    ActivityLog(user_id=employee1_user.id, action='Aufgabe abgeschlossen', 
                               details='Backend Entwicklung', created_at=datetime.now() - timedelta(hours=5)),
                    ActivityLog(user_id=employee2_user.id, action='Aufgabe erstellt', 
                               details='Social Media Posts', created_at=datetime.now() - timedelta(hours=12)),
                    ActivityLog(user_id=admin_user.id, action='Kunde hinzugefügt', 
                               details='Beispiel GmbH', created_at=datetime.now() - timedelta(days=10)),
                    ActivityLog(user_id=employee1_user.id, action='Kommentar hinzugefügt', 
                               details='API Spezifikation - Rückfragen geklärt', created_at=datetime.now() - timedelta(hours=2))
                ]
                
                for activity in activities:
                    if not ActivityLog.query.filter_by(user_id=activity.user_id, action=activity.action, details=activity.details).first():
                        db.session.add(activity)
                
                db.session.commit()
                print("✓ Aktivitätslog-Einträge hinzugefügt")
            
        except Exception as e:
            db.session.rollback()
            print(f"✗ Fehler beim Hinzufügen der Beispieldaten: {e}")
            import traceback
            traceback.print_exc()
            print("\nTabellen wurden erstellt, aber Beispieldaten konnten nicht hinzugefügt werden.")
            sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ SMARTCRM DATENBANK ERFOLGREICH INITIALISIERT!")
    print("=" * 60)
    print("\nSie können jetzt die Anwendung starten und verwenden.")
    print("\nBeispieldaten:")
    print("  - 3 Kunden")
    print("  - 2 Aufträge")
    print("  - 2 Kontakte")
    print("  - 4 Benutzer (Admin, Manager, 2 Mitarbeiter)")
    print("  - 3 Projekte")
    print("  - 7 Aufgaben")
    print("  - 5 Aktivitätslog-Einträge")
    print("\nViel Erfolg mit Ihrem SmartCRM-System!")
    print("\nBenutzer:")
    print("  - admin@smartcrm.at (Administrator)")
    print("  - manager@smartcrm.at (Manager)")
    print("  - employee1@smartcrm.at (Thomas Developer)")
    print("  - employee2@smartcrm.at (Sarah Designer)")

if __name__ == '__main__':
    # Prüfe, ob DATABASE_URL gesetzt ist
    if not os.getenv('DATABASE_URL') and not os.path.exists('.env'):
        print("WARNUNG: Keine DATABASE_URL Umgebungsvariable gefunden!")
        print("\nFür PythonAnywhere, setzen Sie die Variable:")
        print("  export DATABASE_URL='mysql+pymysql://user:pass@server/database'")
        print("\nOder erstellen Sie eine .env Datei.")
        print("\nFortfahren mit Standard-SQLite? (j/n): ", end='')
        
        response = input().lower()
        if response != 'j':
            print("Abgebrochen.")
            sys.exit(1)
    
    init_database()
