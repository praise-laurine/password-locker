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

        