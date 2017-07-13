""" unittests for bucketlist application tests"""
import unittest
from ..app.bucket_list import BucketListApp, User

class TestApplication(unittest.TestCase):
    """ Tests for bucket list application """
    def setUp(self):
        """ Generate essential parameters required for Tests to run """
        self.app = BucketListApp()

    def test_init(self):
        """ test class initialisation """
        self.assertDictEqual({}, self.app.users)
        self.assertFalse(self.app.authenticated)
        self.assertIsNone(self.app.current_user)

    def test_signup(self):
        """ test user sign up"""
        self.app.signup("PaulNyondo", "password")
        self.assertEqual(1, len(self.app.users))
        self.assertTrue(isinstance(self.app.users['PaulNyondo']['user'], User))

    def test_signout(self):
        """ test user sign out"""
        self.app.signout()
        self.assertIsNone(self.app.current_user)
        self.assertFalse(self.app.authenticated)

    def test_signin(self):
        """test authentication flow of user sign in and sign up """
        self.app.signup("PaulNyondo", "password")
        self.app.signout()
        self.app.signin("PaulNyondo", "password")
        self.assertEqual("PaulNyondo", self.app.current_user.username)

    def test_signup_user_exists(self):
        """ ensure that no duplicate user names"""
        self.app.signup("PaulNyondo", "password")
        self.assertFalse(self.app.signup("PaulNyondo", "password"))
        
if __name__ == "__main__":
    unittest.main()
    