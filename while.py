#------Number Guessing Game------

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
    num_input = input("Enter a number (Between -50 and 50): ")
    
    if num_input.isdigit() or (num_input.startswith("-") and num_input[1:].isdigit()):
        num_input = int(num_input)
    
        # - Check the number is in range
        if -50 <= num_input <= 50:
            # - Plus 1 to the attempts counter           
            attempts += 1
            # - Add the number input to the empty list                       
            num_entered.append(num_input)
            
            if num_input > target_number:
                # - Help user to get to the target number      
                print("Try a lower number!")
    
            elif num_input < target_number:
                print("Try a higher number!")

            else:
                break
        
        else:
            print("Number out of range") 
    else:
        print("Invalid Input")

# - Calculate the average of attempts when the target number is entered
if attempts > 0:
    average = sum(num_entered) / attempts 
    print(f" That is Correct! The average of your inputs is {average}")
else: 
    print("You made no attempts")