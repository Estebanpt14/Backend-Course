from fastapi import FastAPI, status, HTTPException
from db.models.user import User
from db.client import *

app = FastAPI(openapi_tags=["userdb"],
              responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


def search_user_name(username: str) -> User:
    user = find_user_name(username)
    return user


@app.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(usr: User):
    if search_user_name(usr.name) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Usuario ya existente")
    user = find_user(insert_user(user=usr))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Usuario no encontrado")
    return user


@app.get("/{item_id}", response_model=User, status_code=status.HTTP_200_OK)
async def get_user(item_id: str):
    user = find_user(item_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Usuario no encontrado")
    return user


@app.get("/", response_model=list[User])
async def get_users():
    return (get_all_users())
