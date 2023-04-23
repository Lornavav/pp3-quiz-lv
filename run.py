from questions import questions

"""
Function to load main menu, error handling if correct option
is not selected. Option to quit the game and break out of loop.
"""


def main_menu():
    print("1. Start Quiz")
    print("2. Instructions")
    print("3. Leaderboard")
    print("4. Quit")
    while True:
        try:
            selection = int(input("Enter option: "))
            if selection == 1:
                new_game()
                break
            elif selection == 2:
                print("The game is simple, read the questions..")
                print("Decide on your answer..")
                print("Input your answer using option 1, 2, 3, 4.")
                print("Best of luck!")
            elif selection == 3:
                pass
            elif selection == 4:
                print("Sorry to see you go! Come back soon!")
                break
            else:
                print("Invalid option. Enter 1-4")
                main_menu()
        except ValueError:
            print("Invalid option. Enter 1-4")
    exit()


"""
Function to run the quiz, includes user name input,
A for loop to iterate through the questions and options,
A while loop to catch any incalid enteries, if/else statement
to match user input with answers and increase score.
"""


def new_game():

    global USER_NAME

    USER_NAME = input("Please enter your name to start quiz: ")

    if USER_NAME == "":
        print("You must enter your name to begin!")
        new_game()
    else:
        print(f"Welcome {USER_NAME}. Best of luck!")

    global CORRECT_ANSWERS

    CORRECT_ANSWERS = 0

    for question in questions:
        print(question["question"])

        for i, option in enumerate(question["options"]):
            print(i+1, option)

        user_answer = (input("Enter 1, 2, 3, 4: "))

        while True:
            if user_answer not in ["1", "2", "3", "4"]:
                user_answer = (input(
                    "You can only enter 1, 2, 3 or 4. Try again: "))
                continue
            else:
                break

        user_input = int(user_answer)
        if question["options"][user_input-1] == question["answer"]:
            CORRECT_ANSWERS += 1
            print("Correct!")
        else:
            print("Incorrect! The correct answer is", question["answer"])

    print(f"{USER_NAME} you scored {CORRECT_ANSWERS} out of {len(questions)}.")

    # update_leaderboard()
    # game_over()


main_menu()
