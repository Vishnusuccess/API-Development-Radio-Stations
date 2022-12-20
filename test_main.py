from fastapi.testclient import TestClient
from fastapi import FastAPI,status
from main import app

# from pyesymain import app

client = TestClient(app)

def test_read_root():
    response = client.get("/stations")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{"name": 'YachTRock', 'id':'181-yachtrock'},
                                {'name': 'power181', 'id':'181-powerexplicit'},
                                {"name": 'ThePoint', 'id':'181-thepoint'}]

def test_station_details():
    response= client.post("/stations_details", json={"name": "aspire","song": "stereo hearts","artist": "gym class heroes"})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == { "name": "aspire","song": "stereo hearts","station_id": 12, "artist": "gym class heroes"}



# from fastapi import FastAPI
# from fastapi.testclient import TestClient

# app = FastAPI()


# @app.get("/")
# async def read_main():
#     return {"msg": "Hello World"}


# client = TestClient(app)


# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}