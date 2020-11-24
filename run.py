from user import User
from user import Credentials

def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function that saves new user
    '''
    user.save_user()

def del_user(user):
    '''
    Function that deletes a user
    '''
    user.delete_user()

def find_user(user_name):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_user_name(user_name)

def check_existing_users(user_name):
    '''
    Function that check if a user exists with that account name and returns a Boolean
    '''
    return User.user_exist(user_name)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def create_credentials(user_name,password,account):
    '''
    Function that creates new credential details
    '''
    new_credentials = Credentials(user_name,password,account)
    return new_credentials

def save_credentials(credentials):
    '''
    Function that saves new credentials to the credential list
    '''
    credentials.save_credentials()
def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def find_credentials(account):
    '''
    Function that finds Credential by account name and return the credential details that matches the account name
    '''
    return  Credentials.find_by_account(account)

def check_existing_credentials(username):
    '''
    Function that checks if Credentials exists with the account provided and returns a boolean
    '''
    return Credentials.credentials_exist(user_name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Hello welcome to password locker! What is your name?")
    user_name = input()
    print(f"Hello {user_name} . Apply these commands to continue:CH = create account," )
    short_code = input().lower()
    if short_code == 'ch':
        print('Enter new account details to log in')
        print('*' * 100)
        account = input('Enter accountName: ')
        username = input('Enter Username: ')
        while True:
            print('use :  EP =  to enter password')
            password_choice = input().lower()
            if password_choice == 'ep':
                password = input('Enter Password: ')
                break
            else:
                print('Invalid password code. Please try again')
            save_user(create_user(username, password))
        print('*' * 100)
        print(f'Hello {username} , You have created your new account successfully! Your account password is: {password}')
        print('*' * 100)
    while True:
        print('Use these short codes to manage and navigate through your credentials: \n NC = new credential, \n VC = display credentials,\n SC =     find credential  \n Dc = delete credential, \n  EX = exit application')
        short_code = input().lower()
        if short_code == 'nc':
            print('Enter New Credential Details')
            print('*' * 100)
            account = input('account Name : ')
            user_name = input('Username : ')
            while True:
                print('Need a password? Use: EP = enter password')
                password_choice = input().lower()
                if password_choice == 'ep':
                    password = input('Enter password : ')
                    break
                else:
                    print('Invalid short code. Please try again')
                print('*' * 100)
            save_credentials(create_credentials(account, user_name,password))
            print('*' * 100)
            print(f'Your {account} account has been saved')
            print('*' * 100)
        elif short_code == 'vc':
            if display_credentials():
                print('Your saved credentials are:')
                for account in display_credentials():
                    print('*' * 100)
                    print(f' Name: {account} \n Username: {user_name} \n Password: {password}')
                    print('*' * 100)
            else:
                print('*' * 100)
                print('You dont seem to have any Credentials yet. Please Create One')
                print('*' * 100)
        elif short_code == 'dc':
            print('Enter account name to delete...')
            name = input('account Name : ')
            print('*' * 100)
            if find_credentials(user_name):
                name_result = find_credentials(user_name)
                name_result.delete_credentials()
                print(f'account {name} has been successfully deleted ')
                print('*' * 100)
            else:
                print('Incorrect account name')
                print('*' * 100)
        elif short_code == 'sc':
            print('Enter Account Name To Search...')
            search = input('Account Name : ')
            print('*' * 100)
            if find_credentials(search):
                search = find_credentials(search)
                print(f'Found credential by Account Name: {search} ')
                print('*' * 100)
            else:
                print('Credential does not exist')
                print('*' * 100)
        elif short_code == 'ex':
            print('Goodbye and Thanks for using password locker.Have a nice day!')
            print('*' * 100)
            break
        else:
            print('Invalid Short code. Please try again!')
            print('*' * 100)
if __name__ == '__main__':
    main()
