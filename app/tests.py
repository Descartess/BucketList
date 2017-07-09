""" unittests for bucketlist item tests"""
import unittest
from bucketList import BucketListItem, BucketList, Application, User

class TestBucketListItemClass(unittest.TestCase):
    """unit test methods for Test_BucketListItem_Class """
    def setUp(self):
        """Initialisation before each test """
        self.blist_item = BucketListItem("Road trip across the country")

    def test_init(self):
        """ test the __init__ method"""
        self.assertEqual(self.blist_item.name, "Road trip across the country")
        self.assertFalse(self.blist_item.completed)

class Test_BucketList_Class(unittest.TestCase):
    """unit test methods for Test_BucketListItem_Class """
    def setUp(self):
        """Initialisation before each test """
        self.blist = BucketList("Adventure",30)

    def test_init(self):
        """ test the __init__ method"""
        self.assertEqual(self.blist.name, "Adventure")
        self.assertEqual(self.blist.completed_by, 30)
        self.assertEqual([],self.blist.list_items)
        self.assertFalse(self.blist.completed)

    def test_add_item(self):
        """ test the add_item method"""
        self.blist.add_item("Road trip across the country")
        self.assertEqual(1,len(self.blist.list_items))
        self.assertTrue(isinstance(self.blist.list_items[0],BucketListItem))


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

class TestApplication(unittest.TestCase):
    """ Tests for bucket list application """
    def setUp(self):
        """ Generate essential parameters required for Tests to run """
        self.app = Application()

    def test_init(self):
        self.assertDictEqual({},self.app.users)
        self.assertFalse(self.app.authenticated)
        self.assertIsNone(self.app.current_user)

    def test_signup(self):
        self.app.signup("PaulNyondo","password")
        self.assertEqual(1, len(self.app.users))
        self.assertTrue(isinstance(self.app.users['PaulNyondo']['user'],User))

    def test_signout(self):
        self.app.signout()
        self.assertIsNone(self.app.current_user)
        self.assertFalse(self.app.authenticated)

    def test_signin(self):
        self.app.signup("PaulNyondo", "password")
        self.app.signout()
        self.app.signin("PaulNyondo", "password")
        self.assertEqual("PaulNyondo",self.app.current_user.username)
    

if __name__ == "__main__":
    unittest.main()