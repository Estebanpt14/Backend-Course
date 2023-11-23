from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

ALGORITHM = "HS256"

app = FastAPI()

oAuth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


class User(BaseModel):
    usuario: str
    fullname: str
    disable: bool


class UserDB(User):
    password: str


usuarios = {
    "manu": {
        "usuario": "manu",
        "password": "1234wasd",
        "fullname": "Manuela",
        "disable": False,
    },
    "cev": {
        "usuario": "cev",
        "password": "345wasd",
        "fullname": "Cevil",
        "disable": True,
    }
}


def search_username_db(username: str):
    if username in usuarios:
        return UserDB(**usuarios[username])


def search_username(username: str):
    if username in usuarios:
        return User(**usuarios[username])


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    userdb = search_username_db(form.username)
    if not userdb:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No autenticado")
    if userdb.password == form.password:
        return {"acces_token": userdb.usuario, "token_type": "bearer"}
