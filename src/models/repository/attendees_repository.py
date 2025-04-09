from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees

class AteendeeRepository:

   def insert_attendee(self, attendee_info: Dict) -> Dict:
      with db_connection_handler as database:
         try:
            attendee = (
            Attendees(
               id=attendee_info['id'],
               name=attendee_info['name'],
               email=attendee_info['email'],
               event_id=attendee_info['event_id']
               )
            )
            database.session.add(attendee)
            database.session.commit()

            return attendee_info
         except Exception as exception:
            database.session.rollback()
            raise exception