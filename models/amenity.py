#!/usr/bin/python3
""" Amenity Module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ amenity table declarative class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenties = relationship('Place', secondary='place_amenity', viewonly=False)
