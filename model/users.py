from user import user


class listUser():

    def __init__(self) -> None:
        self.listUsers = []
        self.createUsers()
        pass

    def createUsers(self):
        for i in range(3):
            user1 = user(f"W{i}", i, i)
            self.listUsers.append(user1)

    def getListUsers(self):
        return self.listUsers
