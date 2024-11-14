# Programmers:  Rayan Haq
# Course:  CS151, Dr. Yalew
# Due Date: 11/7/2024
# Programming Assignment:  pa 03
# Problem Statement:  Creating a program to display ASCII art and string decorations to the user
# Data In: Ask the user if they want to see a circle, lines or a random piece of art
# Data Out:  Displays the art the user has selected
# Credits: for one of the random images , https://stackoverflow.com/questions/23623288/print-full-ascii-art

import random #import random function for generating random numbers between 1-3 for the random image function
def circle():
    print("           ------          ")
    print("         /       \        ")
    print("       /           \      ")
    print("      |             |     ")
    print("       \           /      ")
    print("         \        /       ")
    print("            -----             ")


def lines():
    user_input = input("Please enter the character you would like to display ")# asking the user which specific character they would like to use for creating their image
    user_lines = int(input("Please enter the amount of lines you would like your character to display ")) #This input function lets the user decide how many times in a row the specific character will be printed
    user_columns = int(input("Please enter the amount of columns you would like your character to display ")) #Lets the user decide how many collums they would life
    while user_lines <= 0: #while loop for error checking
        print("*****Please enter a valid number of lines you would like to display***** ")
        user_lines = input("Please enter the amount of lines you would like your character to display ")
    while user_columns <=0: #while loop for error checking
        print("*****Please enter a valid number of columns you would like to display***** ")
        user_columns = input("Please enter the amount of columns you would like your character to display")
    count = 0 #variable created for counting the amount of times
    while count < user_lines: #main loop for creating the image
        print(user_input*user_columns)
        count += 1

def random_choice():
    ran_choice = random.randint(0,3)
    if ran_choice == 1:
        print("""\

                                               ._ o o
                                               \_`-)|_
                                            ,""       \ 
                                          ,"  ## |   ಠ ಠ. 
                                        ," ##   ,-\__    `.
                                      ,"       /     `--._;)
                                    ,"     ## /
                                  ,"   ##    /


                            """)
        # I got this random image from https://stackoverflow.com/questions/23623288/print-full-ascii-art
    elif ran_choice == 2: # This section handles the case where the random choice is 2, displaying a square.
        print("Congratulation you got a boring square!!!!!")
        print(f'{"----------":^5}') # Print the top border of the square
        print(f'{"|":<5}{"|":>5}')  # Print the sides of the square (repeated 3 times for a square shape)
        print(f'{"|":<5}{"|":>5}')
        print(f'{"|":<5}{"|":>5}')
        print(f'{"----------":^5}')# Print the bottom border of the square
    elif ran_choice == 3: # This section handles the case where the random choice is 3, displaying a face.
        print("You get a face!!!!!")
        # Print the top of the face (two squares representing eyes)
        print(f'{"----------":^5}     {"----------":^10}')
        print(f'{"|":<5}{"|":>5}     {"|":<5}{"|":>5}')
        print(f'{"|":<5}{"|":>5}     {"|":<5}{"|":>5}')
        print(f'{"|":<5}{"|":>5}     {"|":<5}{"|":>5}')
        print(f'{"----------":^5}     {"----------":^10}')
        # Print the nose and mouth section of the face using backslashes and dashes
        print("             \                           ")
        print("               \                         ")
        print("                 \                       ")
        print("            - - - -                       ")
        print("                                        ")
        # Print the bottom border for the mouth
        print(f'{"/----------/":>20}')



# The main function of the game
def main():
    # Welcome message explaining the game options
    print("Welcome to my game")
    print("In this game you will be able to create your own image, choose a random image, as well as seeing a image of a circle, or you can quit the game")
    # Prompt the user to choose an option
    option = input("Which image would you like to create? The options are circle, random and or create, or quit")
    # Validation loop for the user input, ensuring they choose one of the valid options
    while option != "circle" and option != "random" and option != "create" and option != "quit":
        print("Please enter a valid option")
        option = input("Which image would you like to create? The options are circle, random and or create, or quit")
    if option == "quit": # If the user chooses to quit, end the game with a thank you message
        print("Thank you for using my game")
    while option != "quit": # Continue the game while the option is not "quit"
        if option == "circle":# Call the circle function if the option is "circle"
            circle()
        elif option == "random":# Call the random_choice function if the option is "random"
            random_choice()
        elif option == "create":# Call the lines function if the option is "create"
            lines()
        # After executing the user's choice, prompt for the next option
        option = input("Which image would you like to create? The options are circle, random and or create, or quit")



main()












