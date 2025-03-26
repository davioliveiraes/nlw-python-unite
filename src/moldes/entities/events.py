from src.moldes.settings.base import Base
from sqlalchemy import Column, Integer, String

class Events(Base):
   __tablename__ = 'events'

   id = Column(Integer, primary_key=True)
   title = Column(String, nullable=False)
   details = Column(String, nullable=False)
   slug = Column(String, nullable=False)
   maximum_attendees = Column(Integer)
   
