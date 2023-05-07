import json

import input_output
import utils

USERS_JSON_FILE = "users.json"
SALT = input_output.get_salt()


def load_users():
    try:
        with open(USERS_JSON_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_users(users):
    with open(USERS_JSON_FILE, "w") as f:
        json.dump(users, f)


def main():
    users = load_users()

    while True:
        print("*" * 50)
        choice = input(f"1. signup\n2. Login\n3. Exit\n{'*'*50}\n> ")

        if choice == "1":
            utils.create_user(USERS_JSON_FILE, users, SALT)
        elif choice == "2":
            username = input("Enter your username: ").strip()
            if username not in users:
                print("User not found!")
            else:
                utils.existing_user(USERS_JSON_FILE, users, username, SALT)
        elif choice == "3":
            save_users(users)
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == '__main__':
    main()
