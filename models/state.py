#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Relationship wit City class
    if storage.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            from models import storage
            city_objs = storage.all(City)
            return [city for city in city_objs.values() if city.state_id == self.id]
