# read file
with open("hackme.txt", "r") as file:
    target_data = file.read()
    print("Here is someone to hack: ")
    print(target_data)