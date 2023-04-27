from questions import questions
import gspread
from google.oauth2.service_account import Credentials
import os
from tabulate import tabulate
import colorama

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("quiz-leaderboard")


def clear():
    """
    Function to clear the terminal at
    certain stages for a better UX.
    """
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    """
    Function to load main menu, error handling if correct option
    is not selected. Option to quit the game and break out of loop.

    Inspiration taken from you YouTube video by Phil Adams
    https://www.youtube.com/watch?v=f3D-w6XMTN8
    """
    print(Fore.CYAN + "1.", Fore.YELLOW + "Start Quiz")
    print(Fore.CYAN + "2.", Fore.YELLOW + "Instructions")
    print(Fore.CYAN + "3.", Fore.YELLOW + "Leaderboard")
    print(Fore.CYAN + "4.", Fore.YELLOW + "Quit\n")
    print("-------------------------------")
    while True:
        try:
            selection = int(input(Fore.CYAN + "\nEnter option: \n"))
            if selection == 1:
                clear()
                new_game()
                break
            elif selection == 2:
                print(Fore.WHITE + "-------------------------------")
                print(Fore.YELLOW +
                      "\nThe game is simple, read the questions..")
                print(Fore.YELLOW + "\nDecide on your answer..")
                print(Fore.YELLOW +
                      "\nInput your answer using option 1, 2, 3, 4.")
                print(Fore.YELLOW + "\nBest of luck!\n")
                print("-------------------------------")
                main_menu()
            elif selection == 3:
                clear()
                show_leaderboard()
                print("\n")
                main_menu()
            elif selection == 4:
                print(Fore.WHITE + "-------------------------------")
                print(Fore.YELLOW + "\nSorry to see you go! Come back soon!")
                break
            else:
                print(Fore.RED + "\nInvalid option. Enter 1-4")
                main_menu()
        except ValueError:
            print(Fore.RED + "\nInvalid option. Enter 1-4")
    exit()


def new_game():
    """
    Function to run the quiz, includes user name input,
    A for loop to iterate through the questions and options,
    A while loop to catch any incalid enteries, if/else statement
    to match user input with answers and increase score.

    Inspiration taken from article by Rahul Prasad M.
    https://medium.com/@rahulmallah785671/creating-an-engaging-quiz-game-with-python-a-step-by-step-guide-ea11bd76f159
    """
    global USER_NAME

    while True:
        try:
            USER_NAME = input(Fore.YELLOW +
                              "\nPlease enter your name to start quiz: \n")
        except ValueError:
            print(Fore.RED + "\nInvalid entry. Name must be 2 - 6 characters")
            print("\n")
        if (len(USER_NAME) >= 2 and len(USER_NAME) <= 6):
            break
        else:
            print(Fore.RED + "\nInvalid entry. Name must be 2 - 6 characters")

    print(Fore.CYAN + f"\nWelcome {USER_NAME}. Best of luck!\n")

    global CORRECT_ANSWERS

    CORRECT_ANSWERS = 0

    for question in questions:
        print(Fore.YELLOW + question["question"])

        for i, option in enumerate(question["options"]):
            print(i+1, option)

        user_answer = (input(Fore.YELLOW + "\nEnter 1, 2, 3, 4: "))

        while True:
            if user_answer not in ["1", "2", "3", "4"]:
                user_answer = (input(
                               Fore.RED +
                               """\nYou can only enter 1, 2, 3 or 4.
Try again: \n"""))
                continue
            else:
                break

        user_input = int(user_answer)
        if question["options"][user_input-1] == question["answer"]:
            CORRECT_ANSWERS += 1
            print(Fore.GREEN + "\nCorrect!")
        else:
            print(Fore.RED + "\nIncorrect!", Fore.GREEN +
                  "The correct answer is", Fore.GREEN + question["answer"])

    print(Fore.CYAN +
          f"\n{USER_NAME} you scored {CORRECT_ANSWERS} / {len(questions)}.")

    update_leaderboard()
    game_over()


def update_leaderboard():
    """
    Update google worksheet with the user name and final score.
    """
    data = USER_NAME, CORRECT_ANSWERS
    print(Fore.CYAN + "\nUpdating leaderboard...")
    leaderboard_sheet = SHEET.worksheet("main")
    leaderboard_sheet.append_row(data)
    print(Fore.CYAN + "\nLeaderboard updated successfully.")


def game_over():
    """
    Asks the user if they want to play again,
    While loop with nestled if/else statements to handle
    each option and invalid entries.
    """

    while True:
        try:
            play_again = input(Fore.YELLOW +
                               """\nDo you want to play again?
Enter Y/N: """).lower()
        except ValueError:
            print(Fore.RED + "\nInvalid option. Please enter Y/N.\n")
        if play_again == "y":
            clear()
            new_game()
        elif play_again == "n":
            clear()
            print(Fore.CYAN + "\nGoodbye! Thank you for playing!\n")
            print("\n-------------------------------\n")
            main_menu()
        else:
            print(Fore.RED + "\nInvalid option. Please enter Y/N.\n")
            game_over()


def show_leaderboard():
    """
    Function to show top 10 higheset scores,
    Using google sheets to pull the username and score and
    using tabulate to help format the data.

    Advice from classmate Indrek Mannik on how to
    create this table
    Indrek Mannik
    """
    main = SHEET.worksheet("main")
    data = main.get_all_values()

    def size(dat):
        return float(dat[1])

    data.sort(key=size, reverse=True)

    row_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(tabulate(data[0:10], headers=["Name", "Score"],
          tablefmt='fancy_grid', numalign="center", showindex=row_id))


main_menu()

