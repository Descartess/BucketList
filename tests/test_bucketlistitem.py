""" unittests for bucketlistitem class tests"""
import unittest
from ..app.bucket_list import BucketListItem

class TestBucketListItemClass(unittest.TestCase):
    """unit test methods for Test_BucketListItem_Class """
    def setUp(self):
        """Initialisation before each test """
        self.blist_item = BucketListItem("Road trip across the country")

    def test_init(self):
        """ test the __init__ method"""
        self.assertEqual(self.blist_item.name, "Road trip across the country")
        self.assertFalse(self.blist_item.completed)

    def test_get_status(self):
        """ test get status method"""
        self.assertFalse(self.blist_item.get_status())

    def test_change_status(self):
        """ test the change status method """
        self.blist_item.change_status()
        self.assertTrue(self.blist_item.completed)

if __name__ == "__main__":
    unittest.main()