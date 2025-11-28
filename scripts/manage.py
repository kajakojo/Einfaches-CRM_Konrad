from flask.cli import FlaskGroup
from app import create_app
from app.utils import backup_database, restore_database
import click

cli = FlaskGroup(create_app=create_app)

@cli.command('db-backup')
def backup():
    """Backup the database."""
    backup_database()

@cli.command('db-restore')
@click.argument('backup_file')
def restore(backup_file):
    """Restore the database from a backup file."""
    restore_database(backup_file)

if __name__ == '__main__':
    cli()