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
            print("COURSES",self.cM.get_courses())
            self.displayData(w,self.cM.get_courses())
    
    def getData(self):
        self.cM = model.courseModel()
        model.load_data(self.yM,self.mM,self.aseM,self.asiM)
    
    def displayData(self,widget,array):
        arr1 = []
        arr2 = []
        arr3 = []
        if type(array[0]) == model.Course:
            for i in array:
                arr1.append(i.get_title())
                arr2.append(i.get_grade())
        elif type(array[0]) == model.Module:
            for i in array:
                arr1.append(i.get_title())
                arr2.append(i.get_credits())
                arr3.append(i.get_grade())
        else:
            for i in array:
                arr1.append(i.get_title())
                arr2.append(i.get_weight())
                arr3.append(i.get_grade())
        
        self.view.refreshView(widget,arr1,arr2,arr3)
        


        



    
     
         

    

    
     