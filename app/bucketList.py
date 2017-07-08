"""contains the main classes that make BucketList """

class BucketListItem(object):
    """ bucket list item class """
    def __init__(self, name):
        self.name = name
        self.completed = False

class BucketList(object):
    """ bucket list class and methods """
    def __init__(self, name, due_age):
        self.name = name
        self.due_age = due_age
        self.list_items = []

class User(object):
    """ user class  and methods"""
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Application(object):
    def __init__(self):
        self.users = {}
        self.authenticated = False
        self.current_user = None

