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
