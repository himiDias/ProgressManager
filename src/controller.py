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
        self.view.itemClicked.connect(self.changeScreen)




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
    
    def changeScreen(self,title):
        print("Change screen started")
        pStack = self.view.pageStack.getStack()
        currentS = self.view.getCurrentS()
        if currentS == self.view.courses_screen:
            w = self.view.getYearS()
            for i in self.cM.get_courses():
                if i.get_title() == title:
                    id = i.get_id()
                    for j in self.yM:
                        print("L")
                        years = j.get_years()
                        print(years)
                        if years[0].get_cid() == id:
                            print("Found")
                            self.view.pageStack.push(title)
                            self.displayData(w,years)
                            break
        elif currentS == self.view.years_screen:
            w = self.view.getModuleS()
            course = pStack[0]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM:
                        years = j.get_years()
                        if years[0].get_cid() == courseid:
                            for k in years:
                                if k.get_title() == title:
                                    id = k.get_id()
                                    for l in self.mM:
                                        modules = l.get_modules()
                                        if modules[0].get_yid() == id:
                                            self.view.pageStack.push(title)
                                            self.displayData(w,modules)
                                            break
        elif currentS == self.view.modules_screen:
            w = self.view.getAssessmentS()
            course = pStack[0]
            year = pStack[1]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM:
                        years = j.get_years()
                        if years[0].get_cid() == courseid:
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM:
                                        modules = l.get_modules()
                                        if modules[0].get_yid() == yearid:
                                            for m in modules:
                                                if m.get_title() == title:
                                                    id = m.get_id()
                                                    for n in self.aseM:
                                                        print("TEST")
                                                        assessments = n.get_assessments()
                                                        if assessments[0].get_mid() == id:
                                                            self.view.pageStack.push(title)
                                                            self.displayData(w,assessments)
                                                            break
        elif currentS == self.view.assessments_screen and title == "Coursework":
            w = self.view.getAssignmentS()
            course = pStack[0]
            year = pStack[1]
            module = pStack[2]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM:
                        years = j.get_years()
                        if years[0].get_cid() == courseid:
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM:
                                        modules = l.get_modules()
                                        if modules[0].get_yid() == yearid:
                                            for m in modules:
                                                if m.get_title() == module:
                                                    moduleid = m.get_id()
                                                    for n in self.aseM:
                                                        assessments = n.get_assessments()
                                                        if assessments[0].get_mid() == moduleid:
                                                            for o in assessments:
                                                                if o.get_title() == title:
                                                                    id = o.get_id()
                                                                    for p in self.asiM:
                                                                        assignments = p.get_assignments()
                                                                        if assignments[0].get_cid() == id:
                                                                            self.view.pageStack.push(title)
                                                                            self.displayData(w,assignments)
                                                                            break



    
    def getData(self):
        self.cM = model.courseModel()
        model.load_data(self.yM,self.mM,self.aseM,self.asiM)
    
    def displayData(self,widget,array):
        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []
        if array:
            if type(array[0]) == model.Course:
                for i in array:
                    arr1.append(i.get_title())
                    arr2.append(i.get_grade())
            elif type(array[0]) == model.Module:
                for i in array:
                    arr1.append(i.get_title())
                    arr2.append(i.get_credits())
                    arr3.append(i.get_grade())
                self.calculateCumulativeScoreModules(arr2,arr3,arr4)
                
            else:
                for i in array:
                    arr1.append(i.get_title())
                    arr2.append(i.get_weight())
                    arr3.append(i.get_grade())
                self.calculateCumulativeScore(arr2,arr3,arr4)
                     
            
        self.view.refreshView(widget,arr1,arr2,arr3,arr4)
    
    def calculateCumulativeScore(self,weight,grades,array):
        cValue = 0
        array.append(0)
        for i in range(0,len(grades)):
            cValue += grades[i] * (weight[i]/100)
            array.append(cValue)
    
    def calculateCumulativeScoreModules(self,credits,grades,array):
        cValue = 0
        totalCredits = sum(credits)
        array.append(0)
        for i in range(0,len(grades)):
            cValue += (credits[i] * grades[i])*totalCredits
            array.append(cValue)


        

        


        



    
     
         

    

    
     