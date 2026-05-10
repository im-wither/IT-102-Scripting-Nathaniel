# week 4 - function

def send_message():
    for i in range(10):
        print("Yes it is!")

today = input(str("Is today a good day? (y/n)"))

if today == "y":
    send_message()

else: 
    print("I guess not.")
    

   