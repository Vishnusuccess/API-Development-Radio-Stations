from sqlalchemy import Column, Integer, String
from database import Base

class stations(Base):
    __tablename__ = 'stations'
        
    station_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    song = Column(String)
    artist = Column(String) 


class users(Base):
    __tablename__ = 'User_Details' 
        
    id = Column(Integer, primary_key=True, index=True) 
    user_name = Column(String)
    email_id = Column(String)
    Age = Column(String)   