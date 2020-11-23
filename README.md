# Password Locker

### Author: [praise-laurine](https://github.com/praise-laurine)

## Description
This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.

## User Guidlines
The users should be able to:
- Create an account for the application by signing up or log in to the account
- Store existing account details
-  Generate new password for an account that i haven't registered for and store its credentials with the account name
- Delete stored account login details that i do now want anymore.

## Installation/setup instructions requirements
1. python3.6
 
 To install **python3.6** on the terminal execute
 ```
 apt-get install python3.6
  ```
  ```
  apt-get install pip3
  ```
2. pip
3. pyperclip  

## Setup instructions
1. Navigate into the [Project Repository](https://github.com/praise-laurine/password-locker)
2. Clone the project repository by writing the git clone command on the terminal
3. Navigate into the project folder(cd password-locker)

## Running the Application
1. Navigate into the cloned project folder using terminal and enter command `./run.py` to run the app.
The app will open on terminal 
2.  Follow and answer the prompts that will be displayed to use the application.

## How the project works
| Behaviour | Input | Output |
| ------------- |:-------------: |:-------------: |
| Display project folder in the terminal | **In terminal run: $./run.py** | Hello welcome to password locker! What is your name? (After you enter your name): select a short code to navigate through : ca - Create new Account, Lg - Log in to your account, ep - Enter your own password, gp - generate new password |
| Display prompt for creating an account | **Enter: ca** | You've created your new account successfully! Your account password is: |
| Display prompt to login into an account: **Enter: Lg** | Enter the correct username and password to log in | Hello (username)!Welcome to password locker. |
|  Display prompt for creating a credential | **Enter: CA** |  select a short code to navigate through : nc - new credentrial, dc - display credential, fc - find credential, gs - generate random password, ep - Enter your own password, dc - delete credential, ex - exit the application |
|  Display prompt for displaying all stored credential | **Enter: dc** | You dont seem to have any credentials yet(when you log in for the first time) |
| Exit the application | Enter ```ex``` | The application exits |

## Technologies 
* python3.6

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

### License
*MIT licence*
Copyright (c) Nov 2020 **laurine praise**

