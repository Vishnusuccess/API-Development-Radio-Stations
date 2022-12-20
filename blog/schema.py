from pydantic import BaseModel



class stations_details(BaseModel):
    name: str
    song: str
    artist: str

class user_details(BaseModel):
    user_name: str
    email_id: str
    Age: int
   
