from .models import MyUser
# implement logout
def logout(request):
    # take username and password from session
    request.session['username'] = ""
    request.session['password'] = ""
    request.session['is_authenticated'] = False

# implement authenticate
def authenticate(request, username, password):
    # log out any existing user first
    logout(request)
    # get the user object based on user name
    user = list(MyUser.objects.filter(username=username))
    if(len(user) == 0):
        return {"success": False,"message": "No such user"}
    else:
        # check if username and password are matching
        #there is a user, so check for correct password
        if(user[0].password == password):
            #password is correct
            return {"success": True, "message": "Logged in successfully", "user": user[0]}
        else:
            #password is incorrect
            return {"success": False,"error": "Password is incorrect", "user": None}
    
    
# implement login
def login(request, user):
    # store username and password in the sessions
    request.session['username'] = user.username
    request.session['password'] = user.password
    request.session['is_authenticated'] = True
