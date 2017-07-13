""" Unit tests for the flask views """
import unittest
from ..app import APP
from ..app.views import BUCKETLIST

class FlaskTestCase(unittest.TestCase):
    """ unit test for index route """
    def setUp(self):
        self.tester = APP.test_client(self)
        BUCKETLIST.signup('newuser','1')
        
    def test_index(self):
        """ Ensure route / returns 200 """
        response = self.tester.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_correct_signup(self):
        """ Ensure that application runs on correct credentials"""
        response = self.tester.post('/signup',
                                    data=dict(username="Paul", password="1", rpassword="1"),
                                    follow_redirects=True)
        self.assertIn("Paul", response.data)

    def test_signup_duplicate_user(self):
        """ Ensure that application doesnt allow duplicate users """
        response = self.tester.post('/signup',
                                    data=dict(username="newuser", password="1", rpassword="1"))
        self.assertIn("User already exists ", response.data)

    def test_incorrect_signup(self):
        """ Ensure that application returns error  on mismatch passwords"""
        response = self.tester.post('/signup',
                                data=dict(username="Paul", password="1", rpassword="2"),
                                follow_redirects=True)
        self.assertIn("Passwords do not match", response.data)

    def test_correct_signin(self):
        """ Ensure that application returns username on correct sign in"""
        response = self.tester.post('/',
                                    data=dict(username="newuser", password="1"), 
                                    follow_redirects=True)
        self.assertIn("newuser", response.data)

    def test_incorrect_signin(self):
        """ Ensure that application returns username on incorrect sign in"""
        response = self.tester.post('/',
                                    data=dict(username="Paul", password="2"),
                                    follow_redirects=True)
        self.assertIn("Invalid Credentials", response.data)

    def test_correct_signout(self):
        """ Ensure that application returns username on incorrect sign in"""
        response = self.tester.get('/signout',
                               content_type="html/text")
        self.assertIn("Sign Up Here", response.data)

    def test_correct_signup_2(self):
        """ Ensure that the sign up page loads correctly """
        response = self.tester.get('/signup', content_type="html/text")
        self.assertIn("Repeat Password", response.data)

    def test_addbucketlist(self):
        """Ensure that get method for add bucket list works """
        response = self.tester.get('/home/create', content_type="html/text")
        self.assertIn("newuser",response.data)

    def test_addbucketlist_post(self):
        """ Ensure that post method for add bucket list works """
        response = self.tester.post('/home/create', data=dict(b_listname="Career",completed_by=30 ),
                                    follow_redirects=True)
        self.assertIn("Career", response.data)

    def test_addbucketlist_item(self):
        """ Ensure that route can add bucket list item """
        BUCKETLIST.current_user.add_bucketlist("Health", 30)
        response = self.tester.post('/home/bucketlist/0/add', data=dict(blist_item="Gym"),
                                    follow_redirects=True)
        self.assertIn('Gym', response.data)

    def test_addbucketlist_item_get(self):
        """ Ensure that get method works """
        BUCKETLIST.current_user.add_bucketlist("Health", 30)
        response = self.tester.get('/home/bucketlist/0/add', content_type="html/text")
        self.assertIn("newuser", response.data)
    

    

    

    
if __name__ == "__main__":
    unittest.main()
