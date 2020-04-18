from google.appengine.ext import ndb


class Task(ndb.Model):
    t_id = ndb.StringProperty()
    t_title = ndb.StringProperty()
    status = ndb.BooleanProperty()
    due_date = ndb.DateTimeProperty(auto_now=True, auto_now_add=True)
    assigned_user_id = ndb.StringProperty()
