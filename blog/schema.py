


from pydantic import BaseModel



class stations_details(BaseModel):
    name: str
    song: str
    artist: str

class user_details(BaseModel):
    user_name: str
    email_id: str
    Age: int
    




# @app.post("/blog")
# def all_details(id,station_name):
#     return {'id':details.id,'name':details.station_name}