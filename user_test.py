import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    '''
    def setUp(self):
        '''
        Set Up method to run before each individual test case
        '''
        self.new_user = User("PraiseLaurine","Test435s")

    def test_init_(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"PraiseLaurine")
        self.assertEqual(self.password.password,"Test435s")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list 
        '''
        self.new_user.save_user()  
        self.assertEqual(len(User.user_list)1,)
             