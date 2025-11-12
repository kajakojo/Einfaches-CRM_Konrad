#!/usr/bin/env python
"""Quick test script to check if the app works"""

from app import create_app
from app.extensions import db
from app.models import Customer, Project, Task, User, ActivityLog

app = create_app()

with app.app_context():
    print('✓ Alle Models importierbar')
    print(f'Kunden: {Customer.query.count()}')
    print(f'Projekte: {Project.query.count()}')
    print(f'Aufgaben: {Task.query.count()}')
    print(f'Benutzer: {User.query.count()}')
    print(f'Aktivitäten: {ActivityLog.query.count()}')
    
    # Test Dashboard Daten
    from app.routes import bp
    with app.test_client() as client:
        print('\nTeste Dashboard Route...')
        response = client.get('/')
        if response.status_code == 200:
            print('✓ Dashboard lädt erfolgreich (Status 200)')
        else:
            print(f'✗ Dashboard Fehler: Status {response.status_code}')
            
        print('\nTeste Projekte Route...')
        response = client.get('/projects')
        if response.status_code == 200:
            print('✓ Projekte-Seite lädt erfolgreich')
        else:
            print(f'✗ Projekte Fehler: Status {response.status_code}')
            
        print('\nTeste Aufgaben Route...')
        response = client.get('/tasks')
        if response.status_code == 200:
            print('✓ Aufgaben-Seite lädt erfolgreich')
        else:
            print(f'✗ Aufgaben Fehler: Status {response.status_code}')

print('\n✓ Alle Tests bestanden!')
