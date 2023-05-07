import hashlib


def hash_password(password, salt):
    salted_password = salt + password
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password


def check_password(password, salt, hashed_password):
    salted_password = salt + password
    new_hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    if new_hashed_password == hashed_password:
        return True
    else:
        return False
