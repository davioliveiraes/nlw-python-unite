from src.models.settings.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import func

class CheckIns(Base):
   __tablename__ = "check_ins"

   id = Column(Integer, primary_key=True)
   created_at = Column(DateTime, server_default=func.now())
   attendee_id = Column(Integer, ForeignKey("attendees.id"))

   def __repr__(self):
      return f"CheckIns [attendee_id={self.attendee_id}"
