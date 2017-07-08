""" Tests for flask application """
import unittest
from app.bucketList import Application

class TestApplication(unittest.TestCase):
    """ Tests for bucket list application """
    def setUp(self):
        """ Generate essential parameters required for Tests to run """
        self.app = Application()

    def test_init(self):
        self.assertDictEqual({},self.app.users)
        self.assertFalse(self.app.authenticated)
        self.assertIsNone(self.app.current_user)
    
if __name__ == "__main":
    unittest.main()
