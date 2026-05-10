# ask for information
name = str(input("What is your name? "))
fav_color = str(input("What is your favorite color? "))
pet_name = str(input("What was your first pet's name? "))
maiden_name = str(input("What is your mother's maiden name? "))
school = str(input("What elementary school did you attend? "))

# put data in list
data = [name, fav_color, pet_name, maiden_name, school]

# write to file
with open("hackme.txt", "w") as file:
    file.write(str(data))