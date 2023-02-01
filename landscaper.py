money = 0

while(True):
    user_choice = input("[1] Mow Lawn [2] Check Money [Q] Quit")
    if(user_choice == "1"):
        money += 1
    if(user_choice == "2"):
        print(money)
    if(user_choice == "Q"):
        break

