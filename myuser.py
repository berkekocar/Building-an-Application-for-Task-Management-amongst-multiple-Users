from google.appengine.ext import ndb

from taskboard_model import Taskboard


class MyUser(ndb.Model):
    #email address of this user
    user_id = ndb.StringProperty()
    email_address = ndb.StringProperty()
    user_name = ndb.StringProperty()
    task_board = ndb.StringProperty(repeated=True)
