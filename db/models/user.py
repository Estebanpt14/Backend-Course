from pydantic import BaseModel


class User(BaseModel):
    id: str | None
    name: str
    age: int
    email: str
