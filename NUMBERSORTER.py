# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.
print("Welcome to Number Sorter!")
print("This program will sort the 4 numbers you input from highest to lowest.")
one = int(input("Enter the first number: "))
two = int(input("Enter the second number: "))
three = int(input("Enter the third number: "))
four = int(input("Enter the fourth number: "))

if one > two > three > four:
    print("This is their order from highest to lowest:", one, two, three, four)
else:
    if one > two > four > three:
        print("This is their order from highest to lowest:", one, two, four, three)
    else:
        if one > three > two > four:
            print("This is their order from highest to lowest:", one, three, two, four)
        else:
            if one > three > four > two:
                print("This is their order from highest to lowest:", one, three, four, two)
            else:
                if one > four > three > two:
                    print("This is their order from highest to lowest:", one, four, three, two)
                else:
                    if one > four > two > three:
                        print("This is their order from highest to lowest:", one, four, two, three)
if two > one > three > four:
    print("This is their order from highest to lowest:", two, one, three, four)
else:
    if two > one > four > three:
        print("This is their order from highest to lowest:", two, one, four, three)
    else:
        if two > three > one > four:
            print("This is their order from highest to lowest:", two, three, one, four)
        else:
            if two > three > four > one:
                print("This is their order from highest to lowest:", two, three, four, one)
            else:
                if two > four > one > three:
                    print("This is their order from highest to lowest:", two, four, one, three)
                else:
                    if two > four > three > one:
                        print("This is their order from highest to lowest:", two, one, four, three)
if three > one > two > four:
    print("This is their order from highest to lowest:", three, one, two, four)
else:
    if three > one > four > two:
        print("This is their order from highest to lowest:", three, one, four, two)
    else:
        if three > two > one > four:
            print("This is their order from highest to lowest:", two, one, four, three)
        else:
            if three > two > four > one:
                print("This is their order from highest to lowest:", three, two, four, one)
            else:
                if three > four > one > two:
                    print("This is their order from highest to lowest:", three, four, one, two)
                else:
                    if three > four > two > one:
                        print("This is their order from highest to lowest:", three, four, two, one)
if four > one > two > three:
    print("This is their order from highest to lowest:", four, one, four, three)
else:
    if four > one > three > two:
        print("This is their order from highest to lowest:", four, one, three, two)
    else:
        if four > two > one > three:
            print("This is their order from highest to lowest:", four, two, one, three)
        else:
            if four > two > three > one:
                print("This is their order from highest to lowest:", four, two, three, one)
            else:
                if four > three > one > two:
                    print("This is their order from highest to lowest:", four, three, one, two)
                else:
                    if four > three > two > one:
                        print("This is their order from highest to lowest:", two, one, four, three)
if one == two == three == four:
    print("Of course, we can't sort the numbers you input from highest to lowest because they are all equal. Try different numbers, please!")