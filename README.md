# API-Development-Radio-Stations

## Requiremnts

+ fastapi - 0.88.0
+ SQLAlchemy - 1.3.18
+ uvicorn[standard] - 0.20.0
+ pytest - 7.2.0
+ httpx - 0.23.1
+ alembic - 1.9.0

## Instuctions to run the program

+ Clone the repository to your local system

+ It is recomended to use VScode or PyCharm 

+ pip install all the requirements.txt using -r in the command terminal

+ Save all the python files using Cmd+s 

+ Download the SQLite Extensions in the VScode

+ Go to the command palatte select SQLite open database

+ Connect the blog.db file

+ Download the tableplus tool from google and create new connect and select SQLite from that

+ Name the new file and go to select file and select the blog.db file

+ Now use uvicorn main:app --reload to run the program

+ Copy the link+/doc and paste it in browser

+ There the APIs will be displayed

+ Use the pytest in the command termal for testing the program

## OpenAPI or Swaggerhub Schema

+ http://127.0.0.1:8000/docs

+ GET/stations: Returns the list of stations. The list is hard coded, and the endpoint returns the list.

+ POST/stations/details: Posts the details of stations into the database.

+ GET/all_stations_details: Returns the list of stations from the database. This endpoint is same as GET/stations. The difference being details are taken from the database, not hard coded.

+ GET/stations{id}: Returns the details of a single station.

+ POST/users: Adds the new user to the database.

+ GET/all_users: Returns the list of details of all users from the database.

+ GET/single_user/{id}: Returns the details of a user from the database.

## The API Image

<img width="1430" alt="Screenshot 2022-12-20 at 10 05 33 PM" src="https://user-images.githubusercontent.com/82315783/208775974-6f2f4c0f-0ce7-4f9e-992d-bc0a596d35ac.png">





