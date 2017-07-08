""" unittests for bucketlist  tests"""
import unittest

class Test_User_Class(unittest.TestCase):
    """unit test methods for Test_BucketListItem_Class """
    def setUp(self):
        """Initialisation before each test """
        self.user = User("PaulNyondo","password")

    def test_init(self):
        """ test the __init__ method"""
        self.assertEqual(self.user.username, "PaulNyondo")
        self.assertEqual(self.user.password, "password")
      
if __name__ == "__main__":
    unittest.main()