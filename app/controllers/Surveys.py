
from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

        self.load_model('WelcomeModel')
        self.db = self._app.db

   
    def index(self):
        return self.load_view('index.html')

    def create_user(self):
        print "I am create user"

        if 'counter' in session:
            session['counter']=session['counter']+1
        else:
            session['counter']=0


        name=request.form['name']
        location=request.form['location']
        langauge=request.form['langauge']
        comment=request.form['comment']


        return self.load_view('submit.html', name=name, location=location, langauge=langauge, comment=comment)



