# Rock Paper Scessor Lizard Spock- Game

# Introduction
Rock, Paper, Scissors, Lizard, Spock is a game of chance that expands the traditional game of Rock, Paper, Scissors.<br>
Each player picks a variable and reveals it at the same time. The winner is the one who defeats the others.<br>
In a tie, the process is repeated until a winner is found.<br>

[Live Project Here](https://rock-pape-scissors-game-a3ea2fb2d802.herokuapp.com/)

![Mockup](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/ee8f51d3-5e7c-4c27-b437-4d6d2e36f742)


## User Experience - UX

### User Stories

* As a website creator, I want to:
  
1. Build an easy app for the users to play the game.
2. Build a game that is enjoyable for the players.
   
* As Player, I want to:

1. Be able to understand the purpose of the App and start a new game.
2. Be able to follow the score.
3. Be able to see the computer choices.


## Design

#### Colours
* The colours in the game are supplied by the Python Colorama Model.

### Flowcharts 
![Flowcharts](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/ce5c25a0-1f80-4585-a602-7d9b3d7ec0d3)
I spent time planning and thinking about the logic and flow behind the game to ensure I had a general idea of how it could be built. I created flowcharts to assist me with the logical flow throughout the application. The charts were generated using [Lucidchart](https://lucid.app/) Integration and are shown below.<br>


## Features

### Logo and Intro Message

![Logo](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/26f12e4b-b22d-472b-8731-47e59ed92347)
![Intro message](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/1980ae25-59d4-489a-bd8c-54b496d4924a)

* When the users reach the website, they will see this feature. The game logo and the intro message are displayed here.<br>

### Ask Player Name

![Ask Player Name](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/40592628-8d37-4fc0-9f42-7b0212e78f21)

* After the player sees the intro feature, the computer will ask the user's to input their name.<br>

### Display Game rules

![game rules](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/79c1d148-014b-4f5c-851d-213c7b0be69f)
* After the user inputs their name, the program will appear the game rules.


### Options

![display options](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/84fa9545-74aa-4c3b-89d4-75d609af3b64)
* After the user press the Enter Key or any other key, the program will appear the options list.


### players choices and round score

![choice and score](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/19f6fe38-4b80-4f92-bd7b-ceeb98208919)
* After the user select an option, the program will appear both user and computer choices with the winner<br>
between enteties message and round score.


### Error message

![error msg](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/53144e39-0759-488e-9127-dc4df28466b0)
![error msg 2](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/0dffeaa0-11b3-45c2-b8d1-2de3ecf4efe9)
* If the user select an invalid choice the programm will appear an error message and ask the user to reselect a valid option. 


### Winner message

![display winner](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/d96c457a-2cbf-4664-b49a-aae732ee9354)
* When the Rounds are done, the programm appear a message to inform who is the winner.

### Update worksheet

![worksheet](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/4d7d18df-4f44-4353-8856-43196a42c470)
![worksheet screenshot](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/b95258db-7482-4747-b5a4-7aaef353e865)
* By the end of the game, the data will be sent to the worksheet.

### Restart

![restart](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/f6b0a970-81e9-4ae7-a233-b80257199766)
* At the end, the programm will ask the user if he want to restart the game

## Storage data

*I have used the google sheet to save the player name, date, their score and computer score.


## Technologies Used
### Languages Used 

* [Python](https://www.python.org)


#### Python Packages

* [Random](https://docs.python.org/3/library/random.html?highlight=random#module-random): returns a random integer to get a random word
* [Datetime](https://pypi.org/project/DateTime/): returns the full date
* [Gspread](https://pypi.org/project/gspread/): allows communication with Google Sheets
* [Colorama](https://pypi.org/project/colorama/): allows terminal text to be printed in different colours / styles
* [Time](https://pypi.org/project/time/): defined time sleep
* [google.oauth2.service_accoun](https://google-auth.readthedocs.io/en/stable/index.html): credentials used to validate credentials and grant access to Google service accounts
* [enum](https://docs.python.org/3/library/enum.html): create enumerations, which are a set of symbolic names (members) bound to unique, constant values.
* [typing](https://docs.python.org/3/library/typing.html): provides runtime support for type hints.
* [sys](https://docs.python.org/3/library/sys.html#:~:text=This%20module%20provides%20access%20to,It%20is%20always%20available.):provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.


* [Git](https://git-scm.com/)
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
* [GitHub](https://github.com/)
    * GitHub is used to store the project's code after being pushed from Git
* [Heroku](https://id.heroku.com)
    * Heroku was used to deploy the live project
* [VSCode](https://code.visualstudio.com/)
    * VSCode was used to create and edit the website
* [Lucidchart](https://lucid.app/)
    * Lucidchart was used to create the flowchart
* [PEP8](https://peps.python.org/pep-0008/)
    * The PEP8 was used to validate all the Python code using pycodestyle command Line.
* [Patorjk](https://patorjk.com)
    * Patorjk (ASCII Art Generator) was used to draw the game logos


## Testing

### PEP 8 

The [PEP8](https://peps.python.org/pep-0008/) pycodestyle was used to validate every Python file in the project to ensure there were no syntax errors in the project.

* No errors or warnings were found during the testing of the code in PEP8 but in the run page I got some whitelines errors because of the ASCII Logo.
![run page white spaces](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/2831165f-4e50-47f2-be49-40eaa130ade3)


### Functionality 

* The terminal has no issues and is working properly 
* The typewriter starts typing at the right time and is working correctly 
* The input for name have the right behaviour 
* The game rules appear without any issues after the player submits their name and city
* The option to press [Enter] key to start a game is running well
* The game runs without any issues and as expected 
* At the end of the game, the worksheet is updating correctly
* The restart option works correctly


## Bugs 
### Whitespaces

![run page white spaces](https://github.com/soukasamadi/Rock-paper-scissors-lizard-spock.game/assets/131408125/2831165f-4e50-47f2-be49-40eaa130ade3)



### Unfixed Bug

* I could not update the logo (ASCII Art Generator) to avoid these issues.


## Deploying this Project

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
8. Click Reveal Config Vars again and enter CREDS into the Key box and the Google credentials into the Value box
9. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
10. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github


## Forking This Project

* Fork this project by following the steps:

1. Open [GitHub](https://github.com/)
2. Click on the project to be forked
3. Find the Fork button at the top right of the page
4. Once you click the button the fork will be in your repository




## Cloning This Project

* Clone this project by following the steps:
  
1. Open [GitHub](https://github.com/)
2. Click on the project to be cloned
3. You will be provided with three options to choose from, HTTPS, SSH, or GitHub CLI, click the clipboard icon in order to copy the URL
4. Once you click the button the fork will be in your repository
5. Open a new terminal
6. Change the current working directory to the location that you want the cloned directory
7. Type git clone and paste the URL copied in step 3
8. Press Enter and the project is cloned


## Credits

### Content
 
* The terminal function and template for the deployable application was provided by [Code Institute - Template](https://github.com/Code-Institute-Org/python-essentials-template)
* The Python code for the typewriter was taken from the following repo: [PedroCristo](https://github.com/PedroCristo/portfolio_project_3/blob/main/hangman_extras.py)
* Readme template from [PedroCristo](https://github.com/PedroCristo/portfolio_project_3/blob/main/README.md?plain=1)

  
### Information Sources / Resources

* [W3Schools - Python](https://www.w3schools.com/python/)
* [Stack Overflow](https://stackoverflow.com/)
* [Scrimba - Pyhton](https://scrimba.com/learn/python)
