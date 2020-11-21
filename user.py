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

     def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """
        self.user_ame = username
        self.password = password
        self.account = account
               
    @classmethod
   
    def find_by_username(cls,username):
        '''
        method that takes in a username and returns a user that matches the username
        '''

        for user in cls.user_list:
            if user.user_name == username:
                return user

    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user_list
        '''

        for user in cls.user_list:
            if user_name == username:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list




        




