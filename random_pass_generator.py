import random
import string


def generate_password(pass_len, smalls=True, capitals=True, numbers=True, special_chars=True):
    small_alphabets_list = list(string.ascii_lowercase)
    capital_alphabets_list = list(string.ascii_uppercase)
    numbers_list = [str(_) for _ in range(0, 10)]
    special_chars_list = [char for char in string.printable if not char.isalnum() and char not in string.whitespace]
    all_chars_list = []
    all_chars = []

    if smalls:
        all_chars_list.append(small_alphabets_list)
        all_chars += small_alphabets_list
    if capitals:
        all_chars_list.append(capital_alphabets_list)
        all_chars += capital_alphabets_list
    if numbers:
        all_chars_list.append(numbers_list)
        all_chars += numbers_list
    if special_chars:
        all_chars_list.append(special_chars_list)
        all_chars += special_chars_list
    if len(all_chars_list) == 0:
        return None

    password = ""
    for i in range(pass_len // 2):
        selected_list = random.choice(all_chars_list)
        password += str(random.choice(selected_list))
    for i in range(pass_len - pass_len // 2):
        password += str(random.choice(all_chars))

    return password
