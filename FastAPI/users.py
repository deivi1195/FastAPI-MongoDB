from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Inicia el server uvicorn users:app --reload

# Entidad user

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(name="Moure", surname="Dev", url="https://moure2.dev", age=30),
              User(name="Haakon", surname="Dahlberg", url="https://moure3.dev", age=33)]


@app.get('/usersjson')
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age":35},
            {"name": "Moure", "surname": "Dev", "url": "https://moure2.dev", "age":30},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://moure3.dev", "age":33}]
    
@app.get('/users')
async def users():
    return users_list