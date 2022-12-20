1. What libraries did you add to the application? What are they used for?

* FastAPI: or building APIs with Python, based on standard Python type hints
*  SQLAlchemy:  facilitates the communication between python program and database
* Pydantic: for data modelling/parsing that has efficient error handling and a custom validation mechanism
* Alembic:  database migrations

2. What’s the command to start the application locally?

uvicorn main:app --reload

3. If you had more time, what further improvements or new features would you add?

* If I had more time, I would implement unit test for all the functions I used, in a more efficient way.
* I would populate the database with more entries, and I would create different versions of the database.

4. Which parts are you most proud of? And why?

The part I am most proud of is implementing ORM in the application. Though familiar with the concept, it was the first time implementing it. I learned a lot more about the relational databases, and most importantly the interactions between the database and the OOP. I learned a new tool while implementing the ORM, SQLAlchemy, and it was interesting.

5. Which parts did you spend the most time with? What did you find most difficult?

* Supporting the application with the database is the part I spent more time in. I had to define, create, and populate the database with suitable fields and entries. Connecting the database with the program was a little bit challenging. I had to create endpoints for getting data from database as well as posting data into the database. It took a lot of time.
* Database migration tool was a new concept for me. I had to familiarize myself with the concept and understand the benefits of having a migration tool in the application. I spent a good amount of time learning more about Alembic.

6. How do you find the test overall?

* This was a really challenging task. I really enjoyed solving the tasks
* Completing all the required parts of the backend task in 2 hours seems a little difficult unless the candidate is an expert.
* It would be better to provide a bit more detail about some parts of the task. For example, I was unsure about where to collect the user data from. 

