

# - Target number for when the user inputs the number the loop stops 
target_number = -1        
# - Variable with an empty string for the user to enter any number
num_input = ""             
# - Attempts variable to count the amount of times the user inputs a number
attempts = 0              
# - Empty list variable to store the numbers the user enters
num_entered = []          

while num_input != target_number:
    # - Turning the user input into an integer 
    num_input = int(input("Enter a number (Between -50 and 50): "))    
    
    if num_input > target_number:
        # - Plus 1 to the attempts counter           
        attempts += 1
        # - Add the number input to the empty list                       
        num_entered.append(num_input)
        # - Help user to get to the target number      
        print("Try a lower number!")
    
    elif num_input < target_number:
        attempts += 1
        num_entered.append(num_input)
        print("Try a higher number!")
# - Calculate the average of attempts when the target number is entered
else:
    average = sum(num_entered) / attempts 
    print(f"The average of your inputs is {average}")