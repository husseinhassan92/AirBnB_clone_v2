#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy import Column, INTEGER, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="State",
                              cascade="all, delete")
    else:
        name = ""

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            Return list of city instances if City.state_id==current
                State.id
                FileStorage relationship between State and City
            """
            list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    list.append(city)
            return list
