import model

class Controller:
    def __init__(self,view):
        self.view = view

        self.view.login_screen.loginClicked.connect(self.checkCredentials)


    def checkCredentials(self,user,passw):
        ret = model.initialise_user(user,passw)
         
        if ret == "Error":
            print("Incorrect Username/Password")
        else:
            print("Login Success")
            model.setup_db()
            print("Database tables initialised")
         

    

    
     