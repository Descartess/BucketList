""" unittests for bucketlist  tests"""
import unittest
from app.bucketList import BucketList

class Test_BucketList_Class(unittest.TestCase):
    """unit test methods for Test_BucketListItem_Class """
    def setUp(self):
        """Initialisation before each test """
        self.blist = BucketList("Adventure",30)

    def test_init(self):
        """ test the __init__ method"""
        self.assertEqual(self.blist.name, "Adventure")
        self.assertEqual(self.blist.completedBy, 30)
        self.assertEqual([],self.blist.list_items)
        self.assertFalse(self.blist.completed)

if __name__ == "__main__":
    unittest.main()