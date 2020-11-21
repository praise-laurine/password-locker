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

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential objects to the credentials_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials ("mercyVuu","P46HJ","yahoo")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential detail from the credentials list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials ("mercyVuu","P46HJ","yahoo")
        test_delete_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credential_by_username(self):
        '''
        test to check if we can find a credential by username and display information
        '''
        self.new_credential.save_credential()
        test_credential = Credentials ("mercyVuu","P46HJ","yahoo")
        TestCredentials.save_credential

        found_credential = Credentials.find_by_username("mercyVuu")

        self.assertEqual(found_credential.user_name,test_credential.user_name)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials ("mercyVuu","P46HJ","yahoo")
        test_credential.save_credential()

        credential_exists = Credentials.credential_exists("mercyVuu")

        self.assertEqual(credential_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__==  '__main__':
    unittest.main()
                       



    
    

    






    
    
    






   





