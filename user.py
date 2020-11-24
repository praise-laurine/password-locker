import random
import string
class User:
    
    """
    Class that generates new instances of users
    """

    user_list = []

    def __init__(self,user_name,password):
        self.user_name=username
        self.password=password
        
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(user):

        '''
        delete_user method deletes a saved user account from the user_list
        '''

        User.user_list.remove(self)

class Credentials:
    """
    Create credential class that generates new instances of credentials
    """

    credentials_list = [] 

    def __init__(self,account,username, password):
        """
        method that defines user credentials to be stored
        """
        self.user_name = username
        self.password = password
        self.account = account

    def save_credentials(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)    
    
    @classmethod
   
    def find_by_account(cls,account):
        '''
        method that takes in a username and returns a credential that matches the username
        '''

        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def credential_exist(cls,username):
        '''
        Method that checks if a user exists from the user_list
        '''

        for credential in cls.credentials_list:
            if user_name == username:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the user list
        '''
        return cls.credentials_list
    
    def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(password) for i in range(stringLength))
    




        




