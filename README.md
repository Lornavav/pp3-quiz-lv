# Quiz App

![Cover Image](documentation/images/cover_image.png)


## Introduction
This quiz app contains 10 general knowledge multiple choice questions. The user will be given 4 possible answers with each question. All labelled 1-4. If the user gets the correct answer, they will receive a 'Correct' message. If the user gets the answer wrong. The 'Incorrect' message will display along with the correct answer. The user can keep going until they answer all 10 questions. They will receive a score marked out of 10 at the end. Their name and score will be exported to a google sheet.

View the live application [here.](https://pp3-quiz-lv.herokuapp.com/)

## User Experience - UX

### Application Goal

To allow users to enjoy a simple quiz game. They can have as many chances as they want to complete the game. They may pick up some general knowledge while they are playing.

### User Stories

#### As a user

* As a user I want to see a menu option called 'Start Quiz'. When I select this the quiz game will begin.
* As a user I want to see a menu option called 'Instructions'. When I select this the game instructions will load.
* As a user after I read the instructions, I want to be able to enter a menu option.
* As a user I want to see a menu option called 'Quit'. When I select this, I will see a goodbye message.
* As a user I want to enter my name at the start of the game.
* As a user I want to see a quiz question with 4 possible answers.
* As a user I want to option to enter 1-4 to answer the quiz question.
* As a user I want to see a 'Correct' message when I answer the quiz question correctly.
* As a user I want to see an 'Incorrect' message along with the correct answer if I get a quiz question wrong.
* As a user I want to see my score after I have answered all 10 questions.
* As a user I want the option to play the game again after completing a game. I want to be able to choose yes or no.
* As a user I want to a view a leaderboard with the top 10 usernames and scores.

#### As a website owner

* As a website owner I want to capture the users name and final score and export the data to a google sheet for storage.

## Design

### Flowchart

![](documentation/images/flowchart.png)

The flowchart was created and used to map out the user journey. This helped make sure that the user always has somewhere to go. It identified places in the game where the user had the potential to get blocked and ensured we gave them a way out. 

## Features

### Existing Features

* Main Menu

  The main menu allows the user to select from 4 options. They can start the quiz game, read the instructions, look at the leader board or quit. They are prompted to enter an option numbered 1-4. If they enter an invalid option, they will keep being prompted to enter an option until a valid option is entered.

  ![Main Menu](documentation/images/main_menu.png)


* Start Quiz

  The user is prompted to enter in their name. If they try and proceed without entering their name, they will keep being prompted to enter a valid name. They will then see a welcome message and the first question will be displayed.

  ![Start Quiz](documentation/images/user_name.png)

  ![Welcome Message](documentation/images/welcome_message.png)


* Instructions

  The user can choose thia option to view the game instructions. They will be able to continue by pressing another menu option once they are finished with the instructions.

  ![Instructions](documentation/images/instructions.png)


* Leaderboard

  Using google sheets the username and score will be exported and saved to the sheet. This will then display a leaderboard of the top 10 scores and the corresponding username. Link to the google sheet is [Here](https://docs.google.com/spreadsheets/d/1Y6Urtkmn0AbIWGVr8WcIsc378A38l-KzNgYdCeWyLI4/edit?usp=sharing).

  ![Google Sheet](documentation/images/leaderboard_google_sheet.png)

  ![Display Leaderboard](documentation/images/leaderboard.png)


* Quit

  This option gives the users the option to quit from the main menu.

  ![Quit](documentation/images/quit.png)


* Questions and possible answers

  The user will see a question displayed with a list of possible answers listed from 1-4. The user is prompted to enter 1, 2, 3 or 4. If the user enters an invalid option they will be prompted to try again until a valid option is entered.

  ![First Question](documentation/images/first_question.png)

  ![Invalid input](documentation/images/invalid_input.png)


* Question Validation

  If the user gets the answer correct, they will see the Correct! message display on screen.

  If the user gets the answer incorrect, they will see the Incorrect! messages display on screen alongside the correct answer.

  ![Correct Answer](documentation/images/correct_answer.png)

  ![Incorrect Answer](documentation/images/incorrect_answer.png)


* Final score

  After the user has answered 10 questions, they will see a final score be displayed with their name.

  ![Final Score](documentation/images/final_score.png)


* End game function

  The user will be asked if they want to play again. If they enter 'Y' a new game will start. 

  If they enter 'N' they will be shown a goodbye message and the game will be over.

  ![Goodbye message](documentation/images/goodbye.png)


### Future Features

* I would like to implement more styling throughout the application including some graphics.
* I would like to include more questions and import them from an API or storage in google sheets and then have them pulled in at random so that the same user can play 
  the game over and over and not get bored and not get too familiar with the answers.

## Testing

### CI Python Linter Testing

No errors found on run.py file

![run.py](documentation/images/ci_python_linter.png)

No errors found on questions.py file

![Questions.py](documentation/images/questions_ci%20python_linter.png)


### Manual testing based on user stories

* Manual testing was carried out on Edge & Chrome browsers using a Windows 10 desktop.

![Manual Testing](documentation/images/mannual_testing_1.png)

![Manual Testing 2](documentation/images/mannual_testing_2.png)

### Error Handling

Error handling has been implemented where relevant throughout the application. This prevents the user getting blocked at a step or getting thrown out of the application. It will also help prevent bugs and incorrect data from being entered.

  * Main Menu - User must enter options 1-4 to proceed. 
  
    [Error Main Menu](documentation/images/error_main_menu.png)

  * Enter Name - The user must enter a name with a minimum of 2 letters and a maximum of 6. 

    [Error Enter Name](documentation/images/error_enter_name.png)

  * Answering Quiz Questions - The user must input an option of 1-4 anything outside of this will receive an error. And the while loop will ensure that the user keeps getting asked to input the correct answer before proceeding.

    [Error Answer Question](documentation/images/error_answer_question.png)

  * End Game - After all the quiz questions have been completed the user has the option to play again. This should be answered using Y/N .lower() has been added to this input to accept lower case y/n also. If anything else is entered the user will receive an error.

    [Error End Game](documentation/images/error_end_game.png)

## Unfixed Bugs

* Not aware of any unfixed bugs at the time of deployment. A try/except with nestled if/else statements has been put in place to catch any errors. 

## Bugs encountered

* Strings being too long for the terminal and receiving an error when passing through the linter. This came up for me quite a bit especially with the quiz questions and when I started to add on the colorama syntax. When I thought I may have fixed the formatting I would deploy it and some strings were displaying with their blank spaces meaning that the strings were printed to the terminal making it unreadable.

The fix: by using multi line strings with the """ syntax sorted by issue after lots of trial and error and monitoring  the code through the linter to ensure there were no errors with the way i formatted it.

* Strange behaviour with the game over function - it was my mentor that reported this issue to me, and I could not recreate it myself. The issue was when you see the prompt 'Do you want to play again?' at the end of the game, if you typed in N you would see the first quiz question. As mentioned I could not recreate this so I turned to my peers I received feedback from 1 guy to say he played it 3 times with no issue. And another was getting inconsistent behaviour. It was him that suggested that i had an unnecessary input in the function. So, I simplified it and also added in the option where they are returned to the main menu if they select N for 'Do you want to play again?'. I am hoping this bug is gone now.

## Deployment

### Heroku deployment

About mid may through the final product I deployed the app in Heroku to ensure there were no issues. From then I manually deployed the branch each time I pushed something new. I followed the below steps:

* Created an account with Heroku and log in through the [Heroku](https://www.heroku.com/) website.
* From the dashboard click on the 'New' option and selected 'Create New App.
* Add in an app name and choose a region and click 'Create app'.
* Click on the 'Settings' tab and from the 'Config Vars' section click 'Reveal Config Vars'
* From here add in google sheet credentials if applicable.
* Type the name of the file (creds) into the 'KEY' field and then from the IDE open the creds.json file and copy and paste everything from there into the 'VALUE' field and click 'Add'.
* Still in the 'Config Vars' section add PORT into the 'KEY' field and 8000 into the 'VALUE' field and click 'Add'.
* From the buildpacks section click 'Add buildpack'.
* Add the Python buildpack first, followed by the ModeJs they must be added in this order.
* Go to the 'Deploy' tab and under 'Deployment Method' click on 'GitHub'.
* From the 'Connect to GitHub' section ensure the correct repository is selected and then search for the repository you want to connect to and click 'Connect'.
* You can choose an automatic deploy or a manual deploy. I chose a manual deploy.
* With a manual deploy I made sure the main branch was selected and clicked 'deploy branch'.
* Once the build is finished there should be a message saying 'Your app was successfully deployed' with a 'View' button.
* When I click on 'View' this opened the application.


### Fork repository

To create a copy of the repository on your own account, follow the below steps:

* Navigate to [My Repository Page](https://github.com/Lornavav/pp3-quiz-lv).
* Click on 'Fork' up on the top right of the page.
* There will now be a copy of the original repository in your Github account.

## Technologies Used

### Languages

* Python

### Python Packages
 
 * Import method used to import questions from questions.py into run.py
 * [gspread](https://pypi.org/project/gspread/) - This allows the application to communicate with google sheets.
 * [google.oauth2.service_account](https://google-auth.readthedocs.io/) - This provides the ability to authenticate to Google APIs.
 * [OS](https://docs.python.org/3/library/os.html) - Used to create clear function to clear terminal at certain points throughout the game.
 * [Tabulate](https://pypi.org/project/tabulate/) - Used to build leaderboard table.
 * [Colorama](https://pypi.org/project/colorama/) - Used to add colour to the terminal.

### Frameworks and Tools

 * [Lucid](https://lucid.app/) - Used to create flowchart.
 * [Codeanywhere](https://app.codeanywhere.com/) - IDE used to develop my project.
 * [GitHub](https://github.com/) - Used to host repository.
 * [Heroku](https://www.heroku.com/) used to deploy the application using CI [Python Template](https://github.com/Code-Institute-Org/python-essentials-template).
 * Google Sheets - Used to create the quiz leaderboard to hold username and score.
 * Google Drive, Google Sheet API and Google Cloud Platform - Used to connect the google sheet to the project.
 * [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to verify code to ensure there are no errors.

## Credits

* My peer Indrek Mannik from my cohort for helping me fix the bug mentioned above in the game over function and also for pointing me in the right direction of for formatting my leaderboard by using Tabulate.
* Rahul Prasad M [article](https://medium.com/@rahulmallah785671/creating-an-engaging-quiz-game-with-python-a-step-by-step-guide-ea11bd76f159) used for inspiration on creating the quiz with dictionaries.
* Phil Adams [YouTube video](https://www.youtube.com/watch?v=f3D-w6XMTN8) used for inspiration on creating a menu structure used for the main menu.




