""" Tests for flask application """
import unittest
from app.bucketList import Application

class Test_Application(unittest.TestCase):
    """ Tests for bucket list application """
    def setUp(self):
        """ Generate essential parameters required for Tests to run """
        app = Application()
    

unittest.main()
