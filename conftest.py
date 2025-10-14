# Imports.
import pytest

from app import create_app
from database import drop_database_tables

# Fixtures.
@pytest.fixture
def test_setup():
    """
    Deletes old database tables and creates a new app for testing.
    """
    drop_database_tables()
    app = create_app()
    
    app.config['TESTING'] = True
    
    with app.app_context():
        yield app