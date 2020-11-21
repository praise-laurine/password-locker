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

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours
    '''
    def setUp(self):
        '''
        Set Up method to run before each individual test case
        '''
        self.new_credential = Credentials("PraiseLaurine","Test435s","gmail")

    def test_init_(self):
        '''
        test_init test case to test if the credentials object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,"PraiseLaurine")
        self.assertEqual(self.new_credential.password,"Test435s")
        self.assertEqual(self.new_credential.account,"gmail")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into the credential list
        '''
        self.new_credential.save_credential() 
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
    






   





if __name__==  '__main__':
    unittest.main()
               