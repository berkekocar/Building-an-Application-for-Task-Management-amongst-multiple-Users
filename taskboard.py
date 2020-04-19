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

        title = self.request.get('tb_title').strip()
        taskboard = Taskboard(id = title, tb_title = title, admin_id = user.user_id(), invite_list=[])
        taskboard.put()



        template_values = {
            'myuser' : myuser,
            'taskboard' : taskboard,


        }
        template = JINJA_ENVIRONMENT.get_template('taskboard.html')
        self.response.write(template.render(template_values))

    def post(self):
        #self.response.header['Content-Type'] = 'text/html'

        button = self.request.get('button')

        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser',user.user_id())
        myuser = myuser_key.get()

        if button == 'Create':
            title = self.request.get('t_title').strip()
            if title not in myuser.task_board:
                taskboard = Taskboard(id = title, tb_title = title, admin_id = user.user_id(), invite_list=[])
                taskboard.put()
                myuser.task_board.append(title)
                myuser.put()


        self.redirect('/')
