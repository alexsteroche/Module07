# ------------ #
# Assignment 07
# Description: Examples of pickling and structured error handling
# Changelog: (Me, Today, Everything)
# ARochester, 3.1.21, Created, edited
# ------------ #

import pickle

# This function pickle dumps and loads the lists that are created, then prints them
def save_and_load_data(x,y,z):

    # this will create and write to a binary file. if the file exists it will overwrite data
    f = open("fruit1.dat",
             "wb")
    # pickle.dump puts each dataset into the file as one object
    pickle.dump(x, f)
    pickle.dump(y, f)
    pickle.dump(z, f)
    f.close()

    print("\nThis shows how the file is unpickled and prints the loaded data")
    #this reads the binary data file
    f = open("fruit1.dat", "rb")
    fruit = pickle.load(f)
    shape = pickle.load(f)
    cost = pickle.load(f)
    print(fruit, shape, cost)
    f.close()

# this code creates and prints lists
print("Types of Fruit")
fruit = ["apple", "orange", "pear"]
shape = ["whole", "sliced", "diced"]
cost = [1, 2, 3]
fruitInput = "" # this sets up the input to be in quotation marks later in the code
shapeInput = ""

# this saves and loads the lists via the pickle function at the beginning of the code
save_and_load_data(fruit,shape,cost)

# by putting the try/except into a while true, it is looking for the boolean in the try portion of the code
while True:
    fruitInput = input("Enter a fruit: ")

# if the input is an integer the while True is true and so it prints "don't enter numbers, enter a fruit"
    try:
        int(fruitInput)
        print("Don't enter numbers, enter a fruit")
        # this is an exception that will spot if the input is the value expected (not an integer) it will print "thanks"
    except ValueError:
        print("thanks")
# the break ends the while loop once the correct type of input has been entered
        break

# this is the same as the above code, just for a different variable
while True:
    shapeInput = input("Enter the shape: ")

    try:
        int(shapeInput)
        print("Don't enter numbers, enter the shape")

    except ValueError:
        print("thanks")

        break

# this while loop wants the input to be an integer. So I nested an if else statement that looked for a numeric value
while True:
    costInput = input("Enter the cost: ")

    try:
        if costInput.isnumeric():
            print("thanks")
            break
        else:
            raise Exception  # if the input is not numeric it throws the program to line 79
    # this is a general exception that will spot any error through the entire exception class
    except Exception as e:
        print("I need a numeric cost")
        print("Error info from python:")
        print(e, e.__doc__,type(e),sep='\n')


# We then check the input has been acknowledged by printing them
print(fruitInput + "," , shapeInput + ", ", costInput)

# those inputs are appended onto the fruit, shape and cost lists
fruit.append(fruitInput)
shape.append(shapeInput)
cost.append (int(costInput))  # this converts the input into an integer

# we print the appended lists using the pickle function
print("This is the new appended set of lists" '\n')
save_and_load_data(fruit,shape,cost)