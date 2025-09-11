
def average_age():
    # Get User Inputs for the ages
    friend1_age = float(input("Enter the age of your first friend. Assuming you have any friends: "))
    friend2_age = float(input("Enter the age of your second friend: "))
    friend3_age = float(input("Enter the age of your third friend: "))
    friend4_age = float(input("Enter the age of your fourth friend: "))
    friend5_age = float(input("Enter the age of your fifth friend. Although you probably don't even have a single friend, let alone 5: "))

    # Sum ages and set average_age to the sum.
    average_age = friend1_age + friend2_age + friend3_age + friend4_age + friend5_age
    
    # Average the ages
    average_age /= 5.0

    # Print the results
    print("The average age of your friends is " + str(average_age) + ".")

# Line which calls the above function.
average_age()
