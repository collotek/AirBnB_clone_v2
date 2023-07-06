#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from models.city import City


class State(BaseModel):
    """ State class and everything to do with state """
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
            stat_cities = []
            cities_diction = models.storage.all(City)
            for city in cities_diction.values():
                if city.state_id == self.id:
                    stat_cities.append(city)

            return stat_cities
