from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = [{"name": "User 1", "age": 20},
         {"name": "User 2", "age": 22}]

@app.get("/")
def home():
    return {"message": "Hello world!"}

@app.get("/about")
def about():
    return {"status": "FastAPI"}

@app.get("/user/{name}")
def user(name):
    for u in users:
        if u.get("name") and u.get("name") == name:
            return {"user": u}
    return {"status": "not found"}

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    users.append({"name": user.name, "age": user.age})
    return {"status": 200, "user": user}