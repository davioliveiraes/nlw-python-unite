import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    event_id = "meu-uuid-vai-fortaleza"
    attenddes_info = {
        "uuid": "meu-uuid_attendee2",
        "name": "atendee name2",
        "email": "email2@email.com",
        "event_id": event_id
    }

    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attenddes_info)
    print(response)

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_get_attendee_badge_by_id():
    attendde_id = "meu-uuid_attendee"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendde_id)
    print(attendee)
    print(attendee.name)
