
#instala FastAPI: pip install "fastapi[all]"


from fastapi import FastAPI
from routers import products, users
#from routers import users

app = FastAPI()

#routers
app.include_router(products.router)
app.include_router(users.router)

#url local: http://127.0.0.1:8080 or http://localhost:8080

@app.get("/")
async def root():
    return "Hola FastAPI!"

#url local: http://127.0.0.1:8080/url

@app.get("/url")
async def url():
    return { "url": "https://google.com"}

# inicia el server uvicorn main:app --reload
# Detener el server : CTRL+C

# Documentation con swagger: http://127.0.0.1:8080/docs
# Documentation con redocly: http://127.0.0.1:8080/redoc




