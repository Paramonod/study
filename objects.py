import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

Base = declarative_base()


class WeatherStat(Base):
    __tablename__ = 'weatherstat'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True)
    city = Column(String)
    mean = Column(Float)
    median = Column(Float)
    days = Column(String)


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    days = Column(String)
