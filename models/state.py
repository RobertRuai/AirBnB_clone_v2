#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    # Relationship with City class
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
        __table_args__ = {'mysql_default_charset': 'latin1'}
    else:
        @property
        def cities(self):
            from models import storage
            city_objs = storage.all(City)
            res = []
            for city in city_objs.values():
                if city.state_id == self.id:
                    res.append(city)
            return res
