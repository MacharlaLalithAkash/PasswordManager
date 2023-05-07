import password_hasher


def signup(users, username, password, salt):
    if username in users:
        print(f"{username} already exists!")
        return

    users[username] = {}
    users[username]["password"] = password_hasher.hash_password(password, salt)
    users[username]["services"] = {}
    return users


def signin(users, username, password, salt):
    if username not in users:
        return

    hashed_password = users[username]["password"]
    isAuthenticated = password_hasher.check_password(password, salt, hashed_password)
    return isAuthenticated
