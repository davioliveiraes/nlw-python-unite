import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro no banco de dados")
def test_insert_events():

   event = {
      "uuid": "meu-uuid-vai-fortaleza",
      "title": "Evento do fortaleza",
      "slug": "evento-fortaleza",
      "maximum_attendees": 500,   
         }

   events_repository = EventsRepository()
   response = events_repository.insert_event(event)
   print(response)

def test_get_events_by():
   event_id = "meu-uuid-vai-fortaleza987654321"
   events_repository = EventsRepository()
   response = events_repository.get_events_by(event_id)
   print(response)
   # print(response.title)

