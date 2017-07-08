""" unittests for bucketlist item tests"""
import unittest
from app.bucketList import BucketListItem

class TestBucketListItemClass(unittest.TestCase):
    """unit test methods for Test_BucketListItem_Class """
    def setUp(self):
        """Initialisation before each test """
        self.blist_item = BucketListItem("Road trip across the country")

    def test_init(self):
        """ test the __init__ method"""
        self.assertEqual(self.blist_item.name, "Road trip across the country")
        self.assertFalse(self.blist_item.completed)

if __name__ == "__main__":
    unittest.main()