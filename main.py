import random

# three variables for three bags

bag_x = 10
bag_y = 10
bag_z = 10
print(bag_x, bag_y, bag_z)

# variables for the computer list

var_x = 1
var_y = 1
var_z = 1


# boolean for checking the game status

check = True
count = 1


# list for object names

bag_list = ['x', 'y', 'z']

# game sequence

while check:

    print(bag_x, bag_y, bag_z)

    if count == 1:

        bag_choice = input("please choose bag x or y or z")
        if bag_choice == 'x' or 'y' or 'z':

            while check:
                try:
                    human_var = int(input("please enter number between 0 and 5"))
                    check = False
                except ValueError:
                    print("please enter an integer ")
            check = True

            if 0 < human_var <= 5:
                if bag_choice == 'x':
                    bag_x = bag_x - human_var
                elif bag_choice == 'y':
                    bag_y = bag_y - human_var
                elif bag_choice == 'z':
                    bag_z = bag_z - human_var
                count = count + 1
            else:
                print("please re-enter your values an error has occurred due to wrong input values ")
        else:
            print("please re-enter your values an error has occurred due to wrong input values ")


    elif count % 2 == 0:

        if bag_x == 0 and var_x == 1:
            bag_list.remove('x')
            var_x = 0
        elif bag_y == 0 and var_y == 1:
            bag_list.remove('y')
            var_y = 0
        elif bag_z == 0 and var_z == 1:
            bag_list.remove('z')
            var_z = 0

        bag_name = random.choice(bag_list)

        if bag_name == 'x':

            if bag_x > 5:
                bag_x = bag_x-random.randint(1, 5)
            elif 0 < bag_x < 5:
                bag_x = bag_x - random.randint(1, bag_x)

        elif bag_name == 'y':

            if bag_y > 5:
                bag_y = bag_y - random.randint(1, 5)
            elif 0 < bag_y < 5:
                bag_y = bag_y - random.randint(1, bag_y)

        elif bag_name == 'z':

            if bag_z > 5:
                bag_z = bag_z - random.randint(1, 5)
            elif 0 < bag_z < 5:
                bag_z = bag_z - random.randint(1, bag_z)

        if bag_x == 0 and bag_y == 0 and bag_z == 0:
            check = False
            print("computer wins")
        count = count + 1

    elif count % 2 != 0:

        bag_choice = input("please choose bag x or y or z")
        if bag_choice == 'x' or 'y' or 'z':


            if bag_choice == 'x':

                if bag_x == 0:
                    print("please choose a valid bag")
                    count = count - 1
                else:
                    while check:
                        try:
                            human_var = int(input("please enter number from 0 to 5"))
                            if bag_x >= 5:
                                if 0 < human_var <= 5:
                                    bag_x = bag_x - human_var
                                    check = False
                                else:
                                    print("please re-enter your values an error has occurred due to wrong input values ")

                            else:
                                if 0 < human_var <= bag_x:
                                    bag_x = bag_x - human_var
                                    check = False
                                else:
                                    print("please re-enter your values an error has occurred due to wrong input values ")

                        except ValueError:
                            print("please enter a number ")

                check = True





            elif bag_choice == 'y':

                if bag_y == 0:
                    print("please choose a valid bag")
                    count = count - 1
                else:
                    while check:
                        try:
                            human_var = int(input("please enter number from 0 to 5"))
                            if bag_y >= 5:
                                if 0 < human_var <= 5:
                                    bag_y = bag_y - human_var
                                    check = False
                                else:
                                    print(
                                        "please re-enter your values an error has occurred due to wrong input values ")

                            else:
                                if 0 < human_var <= bag_y:
                                    bag_y = bag_y - human_var
                                    check = False
                                else:
                                    print(
                                        "please re-enter your values an error has occurred due to wrong input values ")

                        except ValueError:
                            print("please enter a number ")

                check = True


            elif bag_choice == 'z':

                if bag_z == 0:
                    print("please choose a valid bag")
                    count = count-1
                else:
                    while check:
                        try:
                            human_var = int(input("please enter number from 0 to 5"))
                            if bag_z >= 5:
                                if 0 < human_var <= 5:
                                    bag_z = bag_z - human_var
                                    check = False
                                else:
                                    print("please re-enter your values an error has occurred due to wrong input values ")

                            else:
                                if 0 < human_var <= bag_z:
                                    bag_z = bag_z - human_var
                                    check = False
                                else:
                                    print("please re-enter your values an error has occurred due to wrong input values ")

                        except ValueError:
                            print("please enter a number ")

                check = True

            count = count + 1
        else:
            print("please re-enter your values an error has occurred due to wrong input values ")
        if bag_x == 0 and bag_y == 0 and bag_z == 0:
            check = False
            print("User wins")



