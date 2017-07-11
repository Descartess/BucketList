""" unittests for bucketlist application tests"""
import unittest
from ..app.bucket_list import BucketList, BucketListItem

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
        self.assertEqual(1, len(self.blist.list_items))
        self.assertTrue(isinstance(self.blist.list_items[0], BucketListItem))

    def test_delete_bucketlistitem(self):
        """ test the delete_bucketlistitem method"""
        self.blist.add_item("Road trip across the country")
        self.blist.delete_bucketlistitem(0)
        self.assertEqual([], self.blist.list_items)

if __name__ == "__main__":
    unittest.main()
