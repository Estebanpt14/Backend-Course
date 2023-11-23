from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oAuth2 = OAuth2PasswordBearer(tokenUrl="login")


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


async def current_user(token: str = Depends(oAuth2)):
    user = search_username(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales de autenticacion invalidas",
                            headers={"WWW-Authenticate": "Bearer"})

    if user.disable:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Usuario deshabilitado4")
    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    userdb = search_username_db(form.username)
    if not userdb:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No autenticado")
    if userdb.password == form.password:
        return {"acces_token": userdb.usuario, "token_type": "bearer"}


@app.get("/users/me")
async def getUsers(user: User = Depends(current_user)):
    return user
