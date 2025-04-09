from .attendees_repository import AttendeeRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

def test_insert_attendee():
   pass