"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Welcome')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view('index.html')
    def logout(self):
        session.pop('id')
        return redirect('/')
    def register(self):
        print '---------- contorller register ------------'
        
        info = {
                'name' : request.form['name'],
                'aliad': request.form['aliad'],
                'email':request.form['email'],
                'password':request.form['password'],
                'comfirm_pw':request.form['comfirm_pw'],
                'bday':request.form['bday']
            }
        print info
        check = self.models['Welcome'].add_user(info)

        if check['status'] == False:
            errors = check['errors']
            print errors
            return self.load_view('index.html', errors= errors)
        else:
            user = check['userdata']
            session['id'] = user['id']
            return redirect('/quote')
    def login(self):
        info ={
            'email':request.form['email'],
            'password':request.form['password']
        }
        check = self.models['Welcome'].login(info)
        if check['status'] == False:
            return self.load_view('index.html', errors= check['errors'])
        else:
            user = check['userdata']
            session['id'] = user['id']
            return redirect('/quote')

    def quote(self):
        
        user = self.models['Welcome'].user(session['id'])
        quotes = self.models['Welcome'].all_quotes()
        return self.load_view('quote.html', user = user[0], quotes = quotes )

    def add(self):
        info = {
            'flag': 0,
            'writer':request.form['writer'],
            'msg': request.form['msg'],
            'poster_id':session['id']
        }
        print info
        self.models['Welcome'].add_quote(info)
        return redirect('/quote')

    def fav(self, quote_id):
        info = { 
            'flag': 1,
            'quote_id': quote_id
            }
        self.models['Welcome'].add_fav(info)
        return redirect('/quote')

    def remove(self, quote_id):
        info = { 
            'flag': 0,
            'quote_id': quote_id
            }
        self.models['Welcome'].add_fav(info)
        return redirect('/quote')
    def getuser(self, user_id):
        info = self.models['Welcome'].get_quote(user_id)
        return self.load_view('user.html', info = info)