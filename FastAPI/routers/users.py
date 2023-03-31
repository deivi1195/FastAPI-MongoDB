from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(tags=["Users"])



# Inicia el server uvicorn users:app --reload

# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="Moure", surname="Dev", url="https://moure2.dev", age=30),
              User(id=3, name="Haakon", surname="Dahlberg", url="https://moure3.dev", age=33)]


@router.get('/usersjson')
async def usersjson():
    return [{"id":1, "name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age":35},
            {"id":2, "name": "Moure", "surname": "Dev", "url": "https://moure2.dev", "age":30},
            {"id":3, "name": "Haakon", "surname": "Dahlberg", "url": "https://moure3.dev", "age":33}]
    
@router.get('/users')
async def users():
    return users_list

# Path
@router.get('/user/{id}')
async def user(id: int):
    return search_user(id)


# Query
# se le puede dejar el mismo path 
#ej: @app.get('/user/') = se hace la busqueda por query (?id=)
@router.get('/userquery/')
async def user(id: int):
    return search_user(id)

#response_model=User, mejora la documentacion, le dice a la documentacion que es lo que tiene que retornar en caso de que sea correcto
@router.post('/user/', response_model=User ,status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
        #return {'error': 'User already exists'}
    else:
        users_list.append(user)
        return user

@router.put('/user/')
async def user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user
            
@router.delete('/user/{id}')
async def user(id: int):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {"error": "No se ha eliminado el usuario"} 




def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}    