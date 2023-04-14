from fastapi import Depends, HTTPException, status, APIRouter
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

# esta secret key se utilizara para poder encriptar y desencriptar, solo nosotros la sabremos
SECRET_KEY = "4c5ba0ca5104158ad192d8b427f278c15001ae5ea0aee7447624eb7d36c297f7"
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1

router = APIRouter()


oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool
    
class UserDB(User):
    password: str
    

users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@gmail.com",
        "disable": False,
        "password": "$2a$12$WmuOzmWsJYbBZAF.r0uAOuIkZB3r3spGh8TYeoVteTeiNhe7xj8Wu"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@gmail.com",
        "disable": True,
        "password": "$2a$12$QPsuy547qYAD07pRqhj8zOCUHNMvIIX814aomOGK1wHfmcf5sD.S6"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
# nuevo criterio
async def auth_user(token: str = Depends(oauth2)):
    
    exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Credenciales de autenticacion invalidas", 
                headers= {"WWW-Authenticate": "bearer"})
    
    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
    except JWTError:
        raise exception
    
    return search_user(username)
        
    
# criterio de dependencia
async def current_user(user: User = Depends(auth_user)):
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    
    return user

@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto.")

    user = search_user_db(form.username)
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contrase;a no es correcta.")
    
    access_token = {"sub":user.username, 
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get('/users/me')
async def me(user: User = Depends(current_user)):
    return user




