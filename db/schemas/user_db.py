def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "name": user["name"],
            "age": user["age"],
            "email": user["email"]}


def users_schema(users):
    list_users = []
    for user in users:
        list_users.append(
            {"id": str(user["_id"]),
             "name": user["name"],
             "age": user["age"],
             "email": user["email"]})
    return list_users
