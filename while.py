

target_number = -1        # Target number for when the user inputs the number the loop stops 
num_input = ""            # num_input variable with an empty string for the user to enter any number 
attempts = 0              # attempts variable to count the amount of times the user inputs a number
num_entered = []          # num_entered variable with an empty list to store the numbers the user enters


# Using while loop for the program to loop back to the orginal question when the target number is not entered

while num_input != target_number:
    num_input = int(input("Enter a number (Between -50 and 50): "))    # turning the user input into an integer 
   
    if num_input > target_number:           # if statement with a greater than operator to loop back for when the user enters a number higher than the target number
        attempts += 1                       # Using the += 1 to add 1 to the attempts variable for everytime the user enters a number
        num_entered.append(num_input)       # Using .append to add the number the user entered to the num_entered variable
        print("Try a lower number!")        # Print funtion to help the user get to the target number
    
    elif num_input < target_number:         # elif statement with a less than operator to loop back for when the user enters a number lower than the target number
        attempts += 1
        num_entered.append(num_input)
        print("Try a higher number!")

else:
    average = sum(num_entered) / attempts   # Making an variable called 'average' and using the sum funtion to add the numbers stored in the num_entered list then dividing that by the attempts to get the average 
    print(f"The average of your inputs is {average}")