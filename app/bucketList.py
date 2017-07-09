"""contains the main classes that make BucketList """

class BucketListItem(object):
    """ bucket list item class """
    def __init__(self, name):
        self.name = name
        self.completed = False

class BucketList(object):
    """ bucket list class and methods """
    def __init__(self, name, completed_by):
        self.name = name
        self.completed_by = completed_by
        self.completed = False
        self.list_items = []

    def add_item(self, name):
        """ add bucket list item to bucket list"""
        item = BucketListItem(name)
        self.list_items.append(item)

    def delete_bucketlistitem(self, b_id):
        """ removes bucketlist item"""
        del self.list_items[b_id]

    def edit_bucketlistitem(self,b_id, name):
        """ edits bucket list item """
        self.list_items[b_id].name = name

class User(object):
    """ user class  and methods"""
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bucket_lists = []

    def add_bucketlist(self, name, age):
        """ user creates bucket list """
        bucket_list = BucketList(name, age)
        self.bucket_lists.append(bucket_list)

    def delete_bucketlist(self,b_id):
        """ removes bucket list from bucket lists """
        del self.bucket_lists[b_id]

    def edit_bucketlist(self, b_id, name, completed_by):
        """ edit bucket list entries """
        self.bucket_lists[b_id].name = name
        self.bucket_lists[b_id].completed_by = completed_by

class Application(object):
    """main class and methods """
    def __init__(self):
        self.users = {}
        self.authenticated = False
        self.current_user = None

    def signup(self, username, password):
        ''' Adds signed up user to global dict of users '''
        if username in self.users:
            return "User already exists"
        user = User(username, password)
        self.users[username] = {'password': password, 'user': user}
        self.current_user = user
        self.authenticated = True

    def signout(self):
        ''' signs out authenticated user '''
        self.current_user = None
        self.authenticated = False

    def signin(self, username, password):
        """ signs in registered users """
        if username in self.users:
            if self.users[username]['password'] == password:
                self.current_user = self.users[username]['user']
                self.authenticated = True 
        return 'User doesnt exist '
