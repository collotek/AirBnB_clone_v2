#!/usr/bin/python3
"""HBNB project State Module"""
from models.base_model import BaseModel
from models.base_model import Base
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade='all, delete')

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """_summary_

            Returns:
                _type_: _description_
            """
            state_cities = []
            cities_dict = models.storage.all(City)
            for city in cities_dict.values():
                if city.state_id == self.id:
                    state_cities.append(city)

            return state_cities
