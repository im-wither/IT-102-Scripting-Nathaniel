# wk5 cipher
def encrypt(inp, shift):
    encrypted_text = ""
    for letter in inp:
        ascii_num = ord(letter)
        
        if ascii_num >= 97 and ascii_num <=122:
            new_ascii = ascii_num + shift
            if new_ascii > 122:
                new_ascii = new_ascii -26
            encrypted_text = encrypted_text + chr(new_ascii)
        else:
            encrypted_text = encrypted_text + chr(ascii_num)
    print("Your encrypted text is", encrypted_text)
    return encrypted_text

def decrypt(inp, shift):
    decrypted_text = ""
    for letter in inp:
        ascii_num = ord(letter)
        
        if ascii_num >= 97 and ascii_num <=122:
            new_ascii = ascii_num - shift
            if new_ascii > 122:
                new_ascii = new_ascii -26
            decrypted_text = decrypted_text + chr(new_ascii)
        else:
            decrypted_text = decrypted_text + chr(ascii_num)
    print("Your decrypted text is:", decrypted_text)


message = str(input("Enter your message: "))
shift_value = int(input("Enter a shift value: "))
encrypted_message = str(encrypt(message, shift_value))

decrypt_question = input("Would you like to decrypt the message? (y/n): ")
if decrypt_question == "y" or decrypt_question == "Y":
    decrypt(encrypted_message, shift_value)
else: 
    print("End of script...")