import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

from taskboard import Tasklist

import os

from myuser import MyUser
from taskboard_model import Taskboard
from task_model import Task

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        url = ''
        url_string = ''

        user = users.get_current_user()
        myuser = None

        #User logged in
        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'


            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()

            if myuser == None:
                myuser = MyUser(id=user.user_id())
                myuser.put()

        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'

        template_values = {'url' : url,'url_text' : url_string, 'myuser' : myuser}
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))

    def post(self):
        #self.response.header['Content-Type'] = 'text/html'

        button = self.request.get('button')

        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser',user.user_id())
        myuser = myuser_key.get()

        if button == 'Create':
            title = self.request.get('tb_title').strip()
            if title not in myuser.task_board:
                taskboard = Taskboard(id = title, tb_title = title, admin_id = user.user_id(), invite_list=[])
                taskboard.put()
                myuser.task_board.append(title)
                myuser.put()


        self.redirect('/')


#starts the web application we specify the full routing table here as well
app = webapp2.WSGIApplication([
    ('/', MainPage),('/taskboard',Tasklist),
], debug=True)
