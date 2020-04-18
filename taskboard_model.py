from google.appengine.ext import ndb

from task_model import Task

class Taskboard(ndb.Model):
    tb_id = ndb.StringProperty()
    tb_title = ndb.StringProperty()
    admin_id = ndb.StringProperty()
    invite_list = ndb.StringProperty(repeated = True)
