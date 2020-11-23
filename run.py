import random
from user import User
from user import Credentials

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function that saves new user
    '''
    return user.save_user()

def display_user():
    '''
    Function that displays existing user
    '''
    return User.display_user() 

def user_login():
     '''
     Function that checks wether a user is logged in
     '''
     confirm_user = Credentials.user_verification(username,password)
     return confirm_user

def create_credential(username,password,account):
    '''
    Function that creates new credential details
    '''
    new_credential = Credentials(username,password,account)  
    return new_credential

def save_credentials(credentials):
    '''
    Function that saves new credentials to the credential list
    '''
    return credentials.save_credentials()

def delete_credential(credentials):
    '''
    Function to delete credentials from credential list
    '''
    return credentials.delete_credentials() 

def find_credential(username):
    '''
    Function that finds Credential by username and return the credentials that matches the username
    '''
    return Credentials.find_by_username(username)

def check_existing_credentials(username):
    '''
    Function that checks if Credentials exists with that username and return a boolean
    '''
    return Credentials.credential_exists(username)

def display_credential_details():
    '''
    Function that returns all the saved credentials
    '''
    return credentials.display_credentials()

def generate_password():
    '''
    Function that generates a random password for the user
    '''
    created_password=Credentials.generatePassword()
    return created_password
        

def main():
    print("Hello welcome to password locker! What is your name?")
    user_name = input()
    print(f"Hello {user_name} Sign up or login to password locker") 
    print('\n')

    while True:
        print("select a short code to navigate through : ca - Create new Account, Lg - Log in to your account, ep - Enter your own password, gp - generate new password")
        short_code = input().lower()
        if short_code == 'ca':
            print("Sign up")
            print("-" * 70)
            user_name = input('username: ')
        if short_code == 'ep':
            password = input("Enter password\n")
            break
            if password_new == 'gp':
                password = generate_password()
                # print("enter password")
                break
            else:
                print("Incorrect password, please try again.")
            save_user(create_user(username,password))
            print('\n')
            print(f"Hi {user_name}, You've created your new account successfully! Your account password is: {password}")
            print('\n')
        elif short_code == "Lg":
            print('\n')
            print("Enter the correct username and password to log in:")
            print('\n')
            user_name = input("username: ") 
            password = input("password: ")
            login = user-login(username,password)
            if user_login == login:
                print("Hello {user_name}!Welcome to password locker.")
                print('\n')

    while True:
        print("select a short code to navigate through : nc - new credentrial, dc - display credential, fc - find credential, gs - generate random password, ep - Enter your own password, dc - delete credential, ex - exit the application")
        short_code = input().lower() 
        if short_code == "nc":
            print("Create new credential") 
            print("-"*30)
            print ("Account name")
            account = input().lower() 
            print("Your username")
            username = input()
        if short_code == 'ep':
            password = input("Enter Your password\n")
            break
        elif short_code == 'gp':
            password = generate_password()
            break
        else:
            print("Incorrect password,please try again.")
    save_credentials(create_credential(user_name,password,account))
    print('\n')
    print(f"Account Credential details for: username: {user_name}, password: {password}, account: {account} has been created successfully")
    print('\n')
    if short_code == "dc":
        if display_credential_details():
            print("Here is your credential details: ")
            print('\n')
        for credential in display_credential_details():
            print(f"username: {credential.user_name}, password: {credential.password}, account: {credential.account}")
            print('\n')
        else:
            print('\n')
            print("You dont seem to have any credentials yet")
            print('\n')
    if short_code == "fc":
        print("Enter the username you want to search for")
        search_username = input().lower()
        if find_credential(search_username):
            search_credential = find_credential(search_username)
            print(f"Account usename: {search_credential.user_name}")
            print('-' * 40)
            print(f"Account: {search_credential.account} password: {search_credential.password}")
            print('-' * 40)
    else:
        print("That credential does not exist") 
        print('\n')
    if short_code == "dc":
        print(f"Enter the account username of the credentials you want to delete")
        search_username = input().lower()
        if find_credential(search_username):
            search_credential = find_credential(search_username)
            print('-' * 40)
            search_credential.delete_credential()
            print('\n')
            print(f"Your stored account credentials for : {search_credential.user_name} has been deleted successfully!")
    else:
        print("The credential ypu want to delete does not exist in your account")
    if short_code == 'gp':
        password = generate_password()
        print(f" {password} has been generated successfully.You can use it in your account")
    if short_code == 'ex':
        print("Thanks for using password locker.Have a nice day!") 
    else:
        print("Wrong entry. check the correct command from the menu")

if __name__ == '__main__':
    main()    











                  






