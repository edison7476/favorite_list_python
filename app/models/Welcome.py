""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class Welcome(Model):
    def __init__(self):
        super(Welcome, self).__init__()
  
    def add_user(self, info):
        print '------------ Model add_user------------------'
        errors = []
        password = info['password']
        EMAIL_valid = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        if len(info['name']) < 2 or len(info['aliad']) < 2:
            errors.append('Name must contain at lease 2 characters!')
            #print errors
        if len(password) < 8:
            errors.append('password must be at least 8 characters')
            #print errors
        if info['password'] != info['comfirm_pw']:
            errors.append('password does NOT match!')
            #print errors
        if not EMAIL_valid.match(info['email']):
            errors.append('invailid email address')
            #print errors
        if errors:
            return{'status':False, 'errors':errors}

        else:
            hash_pw = self.bcrypt.generate_password_hash(password)
            query = "INSERT into users (name, aliad, email, password, bday, created_at) VALUES (:name, :aliad, :email, :password, :bday, NOW())"
            value ={
                    'name':info['name'],
                    'aliad': info['aliad'], 
                    'email' :info['email'], 
                    'password': hash_pw,
                    'bday': info['bday']
                }
            self.db.query_db(query, value)    
            userdata = self.db.query_db("SELECT * from users WHERE email= :email LIMIT 1", {'email':info['email']})    
            return {'status':True, 'userdata':userdata[0] }
    
    def login(self, info):
        errors = []
        password = info['password']
        userdata = self.db.query_db("SELECT * from users WHERE email= :email LIMIT 1", {'email':info['email']})    
        if userdata == []:
            errors.append('user does NOT exist!!')
            return { 'status':False, 'errors':errors }
        elif self.bcrypt.check_password_hash(userdata[0]['password'], password): 
            return {'status':True, 'userdata':userdata[0]}
        else:
            errors.append('password dose NOT match!!')
            return { 'status':False, 'errors':errors }
    
    def user(self,user_id):
        return self.db.query_db("SELECT * from users WHERE id = :id",{'id':user_id})

    def add_quote(self, info):

        query = "INSERT Into quotes (flag, writer, quote, created_at, user_id) VALUES (:flag, :writer, :quote, NOW(), :user_id)"
        
        value = {
            'flag': info['flag'],
            'writer':info['writer'],
            'quote' : info['msg'],
            'user_id': info['poster_id']
        }
        return  self.db.query_db(query, value) 

    def all_quotes(self):
        #return self.db.query_db("SELECT quotes.flag AS flag,  users.id AS id, users.name AS name, quotes.id As quote_id, quotes.writer As writer, quotes.quote As quote, quotes.created_at As post_date, quotes.user_id As user_id from users JOIN quotes WHERE users.id = quotes.user_id")
        return self.db.query_db("SELECT * from users JOIN quotes WHERE users.id = quotes.user_id")

    def add_fav(self, info):
        query = query = "UPDATE quotes SET flag= :flag WHERE id= :quote_id"
        value = {'flag':info['flag'], 'quote_id': info['quote_id']}
        return  self.db.query_db(query, value) 
    def get_quote(self, user_id):
        return self.db.query_db("SELECT * from users JOIN quotes WHERE users.id = quotes.user_id && users.id= :user_id",{'user_id':user_id})