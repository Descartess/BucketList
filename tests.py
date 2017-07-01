""" Tests for flask application """
import unittest
from app.views import Main

class BucketListTest(unittest.TestCase):
    """ Tests for bucket list application """
    def setUp(self):
        """ Generate essential parameters required for Tests to run """
        self.username = " Paul Nyondo"
        self.password = " password "
        self.main = Main()
    def testsignup(self):
        """ Tests the sign up method """
        self.main.adduser(self.username, self.password)
        self.assertIn(self.username, self.main.users)

unittest.main()
