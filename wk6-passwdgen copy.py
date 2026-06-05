import random
import string

def generation(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation 

    char = letters
    if numbers:
        characters += digits
    if special_char:
        char += special

    passwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(passwd) < min_length:
        new_char = random.choice(char)
        passwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_char: 
            meets_criteria = meets_criteria and has_special

generation(10)