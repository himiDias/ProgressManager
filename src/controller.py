import model

class Controller:
    def __init__(self,view):
        self.view = view
        self.cM = None
        self.yM = []
        self.mM = []
        self.aseM = []
        self.asiM = []

        self.view.login_screen.loginClicked.connect(self.checkCredentials)




    def checkCredentials(self,user,passw):
        ret = model.initialise_user(user,passw)
         
        if ret == "Error":
            print("Incorrect Username/Password")
        else:
            print("Login Success")
            model.setup_db()
            print("Database tables initialised")
            self.getData()
            w = self.view.getCourseS()
            self.view.refreshView(w)
    
    def getData(self):
        self.cM = model.courseModel
        model.load_data(self.yM,self.mM,self.aseM,self.asiM)
    
     
         

    

    
     