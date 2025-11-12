import os
import datetime
import shutil
import click
from flask.cli import with_appcontext

def backup_database():
    """Backup the database to a timestamped file."""
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = 'backups'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    source_db = 'app.db'
    backup_file = os.path.join(backup_dir, f'backup_{timestamp}.db')
    
    if os.path.exists(source_db):
        shutil.copy2(source_db, backup_file)
        click.echo(f'Database backed up to {backup_file}')
    else:
        click.echo('No database file found to backup')

def restore_database(backup_file):
    """Restore the database from a backup file."""
    if not os.path.exists(backup_file):
        click.echo('Backup file not found')
        return
        
    target_db = 'app.db'
    if os.path.exists(target_db):
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        os.rename(target_db, f'{target_db}.{timestamp}')
        
    shutil.copy2(backup_file, target_db)
    click.echo(f'Database restored from {backup_file}')