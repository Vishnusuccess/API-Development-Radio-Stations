from fastapi import FastAPI, Depends,status
from pydantic import BaseModel
import models 
from database import engine,SessionLocal
from blog import schema
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


#Create an API endpoint for obtaining a list of radio stations
#The results of this api call should allow us to obtain individual radio stations
@app.get("/stations")
async def read_root():
    return [{"name": 'YachTRock', 'id':'181-yachtrock'},
    {'name': 'power181', 'id':'181-powerexplicit'},
    {"name": 'ThePoint', 'id':'181-thepoint'}]


#Support the API with a database
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Create an API endpoint for obtaining the details for all radio station
@app.post("/stations_details", status_code=status.HTTP_201_CREATED)
def create(request: schema.stations_details,db:Session = Depends(get_db) ):
    new_stations=models.stations(name=request.name,song=request.song, artist=request.artist)
    db.add(new_stations)
    db.commit()
    db.refresh(new_stations) 
    return new_stations

    
@app.get("/all_stations_details")
def all_stations(db:Session = Depends(get_db)):

    stations_all=db.query(models.stations).all()
    return stations_all

#Create an API endpoint for obtaining the details for singulat radio station
@app.get("/stations/{id}")
def single_stations(id,db:Session = Depends(get_db)):

    stations_single=db.query(models.stations).filter(models.stations.station_id==id).first() 
    return stations_single


#Create an API endpoint for obtaining details about a user
@app.post("/users",status_code=status.HTTP_201_CREATED)
def create_user(request: schema.user_details,db:Session = Depends(get_db) ):
    new_users=models.users(user_name=request.user_name,email_id=request.email_id, Age=request.Age)
    db.add(new_users)
    db.commit()
    db.refresh(new_users) 
    return new_users

@app.get("/all_users")
def all_users(db:Session = Depends(get_db)):

    users_all=db.query(models.users).all()
    return users_all

@app.get("/single_users/{id}")
def single_user(id,db:Session = Depends(get_db)):

    user_single=db.query(models.users).filter(models.users.id==id).first()
    return user_single
