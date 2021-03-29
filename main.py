import random


# boolean for checking the game status

check = True
count = 1


# list for object names

bag_list = [10, 10, 10]

# game sequence
def game_user(index):
    User_check=True
    while User_check:
        try:
            human_var = int(input("please enter number from 0 to 5"))
            if bag_list[index] >= 5:
                if 0 < human_var <= 5:
                    bag_list[index] = bag_list[index] - human_var
                    User_check = False
                else:
                    print(
                        "please re-enter  ")

            else:
                if 0 < human_var <= bag_list[index]:
                    bag_list[index] = bag_list[index] - human_var
                    User_check= False
                else:
                    print(
                        "please re-enter  to wrong input values ")

        except ValueError:
            print("please enter a number ")
    # return bag_list


while check:

    print(bag_list[0],bag_list[1],bag_list[2])

    if count % 2 == 0:
        bag_Number = random.randint(0, 2)
        while bag_list[bag_Number] == 0:
            bag_Number = random.randint(0, 2)
        if bag_list[bag_Number] > 5:
            bag_list[bag_Number] = bag_list[bag_Number]-random.randint(1, 5)
        elif 0 < bag_list[bag_Number] <= 5:
            bag_list[bag_Number] = bag_list[bag_Number]-random.randint(1, bag_list[bag_Number])
        if bag_list[0] == 0 and bag_list[1]  == 0 and bag_list[2] == 0:
            check = False
            print("computer wins")
        count = count + 1

    elif count % 2 != 0:
        bag_choice = int(input("please choose bag 1 or 2 or 3"))
        if bag_choice == 1 or bag_choice == 2 or bag_choice == 3:

            if bag_choice == 1:

                if bag_list[bag_choice-1] == 0:
                    print("please choose a valid bag")
                    count = count - 1
                else:
                    game_user(bag_choice-1)

                check = True
                count = count + 1

            elif bag_choice == 2:
                if bag_list[bag_choice - 1] == 0:
                    print("please choose a valid bag")
                    count = count - 1
                else:
                    game_user(bag_choice - 1)

                check = True
                count = count + 1
            elif bag_choice == 3:
                if bag_list[bag_choice - 1] == 0:
                    print("please choose a valid bag")
                    count = count - 1
                else:
                    game_user(bag_choice - 1)

                check = True
                count = count + 1

        else:
            print("please re-enter your values an error has occurred due to wrong input values ")
        if bag_list[0] == 0 and bag_list[1] == 0 and bag_list[2] == 0:
            check = False
            print("User wins")









