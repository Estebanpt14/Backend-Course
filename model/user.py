class user():

    def __init__(self, name: str, id: int, age: int) -> None:
        self.name = name
        self.id = id
        self.age = age
        pass

    def getId(self):
        return self.id

    def getName(self):
        return self.name
