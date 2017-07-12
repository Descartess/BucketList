""" unittests for bucketlist user class"""
import unittest
from ..app.bucket_list import  BucketList, User

class Test_User_Class(unittest.TestCase):
    """unit test methods for Test_BucketListItem_Class """
    def setUp(self):
        """Initialisation before each test """
        self.user = User("PaulNyondo","password")

    def test_init(self):
        """ test the __init__ method"""
        self.assertEqual(self.user.username, "PaulNyondo")
        self.assertEqual(self.user.password, "password")

    def test_add_bucketlist(self):
        """ test the add_bucket list method"""
        self.user.add_bucketlist("Adventure", 30)
        self.assertEqual(1,len(self.user.bucket_lists))
        self.assertTrue(isinstance(self.user.bucket_lists[0],BucketList))

    def test_delete_bucketlist(self):
        """ test deletion of bucket list"""
        self.user.add_bucketlist("Adventure", 30)
        self.user.delete_bucketlist(0)
        self.assertEqual([], self.user.bucket_lists)

    def test_edit_bucketlist(self):
        """ test editing of bucket list """
        self.user.add_bucketlist("Adventure", 30)
        self.user.edit_bucketlist(0,"Family", 35)
        self.assertEqual(self.user.bucket_lists[0].name, "Family")
        self.assertEqual(self.user.bucket_lists[0].completed_by, 35)
        
if __name__ == "__main__":
    unittest.main()