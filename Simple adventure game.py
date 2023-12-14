name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right, Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or sweinm accross? Type walk around it or swim across")

    if answer == "swim":
        print("You swam across and were eaton by a alligator.")

    elif answer == "walk":
        print("You walked for may miles, ran out of water and you lost the game")

    else:
        print('Not a valid option. You lose!')

elif answer == "right":
    answer = input("you come to bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose")

    elif answer == "cross":
        answer = input("You cross the brideg and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You tallk to the stranger and they give you gold. You WIN!")

        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose")

        else:
            print('Not a valid option. You lose!')
else:
    print('Not a valid option. You lose!')

print("Thank you for trying", name)