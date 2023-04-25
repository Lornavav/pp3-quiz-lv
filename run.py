from questions import questions
import gspread
from google.oauth2.service_account import Credentials
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("quiz-leaderboard")

# main = SHEET.worksheet("main")

# data = main.get_all_values()
# print(data)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


"""
Function to load main menu, error handling if correct option
is not selected. Option to quit the game and break out of loop.
"""


def main_menu():
    print("1. Start Quiz")
    print("2. Instructions")
    print("3. Leaderboard")
    print("4. Quit\n")
    print("-------------------------------")
    while True:
        try:
            selection = int(input("\nEnter option: \n"))
            if selection == 1:
                clear()
                new_game()
                break
            elif selection == 2:
                print("\nThe game is simple, read the questions..")
                print("\nDecide on your answer..")
                print("\nInput your answer using option 1, 2, 3, 4.")
                print("\nBest of luck!")
            elif selection == 3:
                pass
            elif selection == 4:
                print("\nSorry to see you go! Come back soon!")
                break
            else:
                print("\nInvalid option. Enter 1-4")
                main_menu()
        except ValueError:
            print("\nInvalid option. Enter 1-4")
    exit()


"""
Function to run the quiz, includes user name input,
A for loop to iterate through the questions and options,
A while loop to catch any incalid enteries, if/else statement
to match user input with answers and increase score.
"""


def new_game():

    global USER_NAME

    USER_NAME = input("\nPlease enter your name to start quiz: \n")

    if USER_NAME == "":
        print("\nYou must enter your name to begin!")
        new_game()
    else:
        print(f"\nWelcome {USER_NAME}. Best of luck!\n")

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
                    "\nYou can only enter 1, 2, 3 or 4. Try again: \n"))
                continue
            else:
                break

        user_input = int(user_answer)
        if question["options"][user_input-1] == question["answer"]:
            CORRECT_ANSWERS += 1
            print("\nCorrect!")
        else:
            print("\nIncorrect! The correct answer is", question["answer"])

    print(f"\n{USER_NAME} you scored {CORRECT_ANSWERS} / {len(questions)}.")

    update_leaderboard()
    game_over()


"""
Function to update google sheet with user name and
score.
"""


def update_leaderboard():
    """
    Update the worksheet with the user name and their final points.
    """
    data = USER_NAME, CORRECT_ANSWERS
    print("\nUpdating leaderboard...")
    leaderboard_sheet = SHEET.worksheet("main")
    leaderboard_sheet.append_row(data)
    print("\nLeaderboard updated successfully.")


"""
Asks the user if they want to play again,
While loop with nestled if/else statements to handle
each option and invalid entries.
"""


def game_over():
    play_again = input("\nDo you want to play again? Enter Y/N: ").lower()

    while True:
        if play_again not in ["y", "n"]:
            play_again = input(
                "\nNot a valid option. Enter Y/N: \n").lower()
            continue
        else:
            if play_again == "y":
                clear()
                new_game()
            else:
                clear()
                print("\nGoodbye! Thank you for playing!\n")
                print("\n-------------------------------\n")
                main_menu()


main_menu()
