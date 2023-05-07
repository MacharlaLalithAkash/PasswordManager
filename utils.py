import authenticate
import input_output
import random_pass_generator


def create_user(users_json, users, salt):
    username = input("Username: ").strip()
    password = input("Master Password: ")

    users = authenticate.signup(users, username, password, salt)
    input_output.write_json(users_json, users)


def existing_user(users_json, users, username, salt):
    global service_password
    password = input("password: ").strip()
    isAuthenticated = authenticate.signin(users, username, password, salt)
    if isAuthenticated:
        if not len(users[username]["services"]):
            print(f"Welcome Back! {username}\nYour services list is empty!!")
            add_service_choice = int(input("1. Add Service\n2. Exit\n> "))
            if add_service_choice == 1:
                service_name = input("service name: ")
                service_user_name = input("service username: ")
                pass_gen_choice = int(input("1. Enter Password Manually\n2. Generate Strong Random Password\n> "))
                if pass_gen_choice == 1:
                    service_password = input("service password: ")
                elif pass_gen_choice == 2:
                    pass_length = int(input("Password Length: "))
                    service_password = random_pass_generator.generate_password(pass_length)
                users[username]["services"][service_name] = {
                    "username": service_user_name,
                    "password": service_password
                }
                input_output.write_json(users_json, users)
            elif add_service_choice == 2:
                print("Invalid Choice!")
                print("*" * 50)
        else:
            while True:
                print(f"************Logged in successfully!************")
                service_choice = int(input("Enter you choice\n1. Add Service\n2. Retrieve Service Data:\n> "))
                if service_choice == 1:
                    service_name = input("service name: ")
                    service_user_name = input("service username: ")
                    service_password = input("service password: ")
                    users[username]["services"][service_name] = {
                        "username": service_user_name,
                        "password": service_password
                    }
                    input_output.write_json(users_json, users)
                elif service_choice == 2:
                    print("*" * 50)
                    for key in users[username]["services"]:
                        print(f"* {key}")
                    print("*" * 50)
                    service_choice = input("Enter service name to see its username and password: ").strip()
                    if service_choice not in users[username]["services"]:
                        print("Service not found!")
                    else:
                        print("*" * 50)
                        print(f"username: {users[username]['services'][service_choice]['username']}")
                        print(f"password: {users[username]['services'][service_choice]['password']}")
                        print("*" * 50)
                else:
                    print("Invalid Choice!")
    else:
        print("*" * 50)
        print("Invalid Credentials")
        print("*" * 50)
