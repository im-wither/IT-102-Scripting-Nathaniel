# Week 6 - Password Generator

import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
special = r"!@#$%^^&*()_-|\;<>"

min_len = 8

def yes_or_no(prompt: str) -> bool:
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter yes or no: ")

def get_password_length() -> int:
    while True:
        try:
            length = int(input("How long should the password be? "))
            if length >= min_len:
                return length
            print("Please enter a valid length...")
        except ValueError:
            print("Please enter a whole number...")

def get_criteria() -> dict:
    length = get_password_length()
   

    criteria = {
        "length": length,
        "uppercase": yes_or_no("Would you like uppercase letters? "),
        "lowercase": yes_or_no("Would you like lowercase letters? "),
        "digits": yes_or_no("Numbers (0-9) "),
        "special": yes_or_no("Would you like special characters? ")
    }
    if not any([criteria["uppercase"], criteria["lowercase"], criteria["digits"], criteria["special"]]):
        print(" You must select one character type:")
        return get_criteria()
    return criteria

def build_pool(criteria: dict) -> tuple[str, list[str]]:
    pool = ""
    required = []

    if criteria["uppercase"]:
        pool += upper
        required.append(random.choice(upper))
    if criteria["lowercase"]:
        pool += upper
        required.append(random.choice(lower))
    if criteria["digits"]:
        pool += upper
        required.append(random.choice(digits))
    if criteria["special"]:
        pool += upper
        required.append(random.choice(special))
    return pool, required

def generate(criteria: dict) -> str:
    pool, required = build_pool(criteria)
    length = criteria["length"]

    remaining_count = length - len(required)
    remaining = [random.choice(pool) for _ in range(remaining_count)]

    password_chars = required + remaining
    random.shuffle(password_chars)

    return"".join(password_chars)

def main():
    while True:
        criteria = get_criteria()
        password = generate(criteria)
        print("Generated password: ")
        print(f"{password}")

        if not yes_or_no("Generate again? (y/n)"):
            print("Exiting...")
            break
        print()

if __name__ == "__main__":
    main()