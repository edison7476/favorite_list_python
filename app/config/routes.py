"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Welcome'
routes['POST']['/register'] = 'Welcome#register'
routes['POST']['/login'] = 'Welcome#login'
routes['/quote'] = 'Welcome#quote'
routes['POST']['/add'] = 'Welcome#add'
routes['POST']['/fav/<quote_id>'] = 'Welcome#fav'
routes['POST']['/remove/<quote_id>'] = 'Welcome#remove'
routes['/logout']='Welcome#logout'
routes['/user/<user_id>'] = 'Welcome#getuser'