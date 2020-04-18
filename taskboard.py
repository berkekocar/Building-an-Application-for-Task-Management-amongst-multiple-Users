import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

import os

from myuser import MyUser
from taskboard_model import Taskboard
from task_model import Task

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class Tasklist(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser',user.user_id())
        myuser = myuser_key.get()

        template_values = {
            'myuser' : myuser,
        }
        template = JINJA_ENVIRONMENT.get_template('taskboard.html')
        self.response.write(template.render(template_values))
