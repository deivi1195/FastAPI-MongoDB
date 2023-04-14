from pydantic import BaseModel

#el id en mongodb es un str
class User(BaseModel):
    id: str | None
    username: str
    email: str









