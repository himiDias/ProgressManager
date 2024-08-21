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
        self.view.previousClicked.connect(self.changeScreenPrev)
        self.view.addItemClicked.connect(self.addItem)
        self.view.delItemClicked.connect(self.delItem)
    
    def delItem(self,item):
        pStack = self.view.pageStack.getStack()
        currentS = self.view.getCurrentS()
        if len(pStack) == 0:
            for i in self.cM.get_courses():
                if i.get_title() == item:
                    id = i.get_id()
                    print(id)
                    self.cM.rem_course(id)
                    self.displayData(currentS,self.cM.get_courses())
        elif len(pStack) == 1:
            course = pStack[0]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        years = j.get_years()
                        if years[0].get_cid() == courseid:
                            for k in years:
                                if k.get_title() == item:
                                    id = k.get_id()
                                    j.rem_year(id)
                                    self.displayData(currentS,years)
                                    if not (years):
                                        self.yM.remove(j)
        elif len(pStack) == 2:
            course = pStack[0]
            year = pStack[1]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        years = j.get_years()
                        if years[0].get_cid() == courseid:
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM[1:]:
                                        modules = l.get_modules()
                                        if modules[0].get_yid() == yearid:
                                            for m in modules:
                                                if m.get_title() == item:
                                                    id = m.get_id()
                                                    l.rem_module(id)
                                                    self.displayData(currentS,modules)
                                                    if not (modules):
                                                        self.mM.remove(l)
        elif len(pStack) == 3:
            course = pStack[0]
            year = pStack[1]
            module = pStack[2]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        years = j.get_years()
                        if years[0].get_cid() == courseid:
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM[1:]:
                                        modules = l.get_modules()
                                        if modules[0].get_yid() == yearid:
                                            for m in modules:
                                                if m.get_title() == module: 
                                                    moduleid = m.get_id()
                                                    for n in self.aseM[1:]:
                                                        assessments = n.get_assessments()
                                                        if assessments[0].get_mid() == moduleid:                                                             
                                                            if item == "Coursework":
                                                                n.rem_cw()
                                                            else:
                                                                n.rem_e()
                                                            self.displayData(currentS,assessments)
                                                            if not(assessments):
                                                                self.aseM.remove(n)
        else:
            course = pStack[0]
            year = pStack[1]
            module = pStack[2]
            assessment = pStack[3]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        years = j.get_years()
                        if years[0].get_cid() == courseid:
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM[1:]:
                                        modules = l.get_modules()
                                        if modules[0].get_yid() == yearid:
                                            for m in modules:
                                                if m.get_title() == module:
                                                    moduleid = m.get_id()
                                                    for n in self.aseM[1:]:
                                                        assessments = n.get_assessments()
                                                        if assessments[0].get_mid() == moduleid:
                                                            for o in assessments:
                                                                if o.get_title() == assessment:
                                                                    assessmentid = o.get_id()
                                                                    for p in self.asiM[1:]:
                                                                        assignments = p.get_assignments()
                                                                        if assignments[0].get_cid() == assessmentid:
                                                                            for q in assignments:
                                                                                if q.get_title() == item:
                                                                                    id = q.get_id()
                                                                                    p.rem_assignment(id)
                                                                                    self.displayData(currentS,assignments)
                                                                                    if not(assignments):
                                                                                        self.asiM.remove(p)



    def addItem(self,array):
        type = array[0]
        title = array[1]
        pStack = self.view.pageStack.getStack()
        exists = False
        empty = True
        if type == "Course":
            try:
                grade = float(array[2])
            except:
                print("INVALID TYPE")
            else:
                if  grade <0 or grade > 100.0:
                    print("INVALID INPUTS")
                else:
                    for i in self.cM.get_courses():
                        if i.get_title() == title:
                            exists = True
                            print("Title already exists")
                    if not(exists):
                        id = self.cM.get_nextID()
                        self.cM.add_course(model.Course(id,title,grade))
                        self.displayData(self.view.getCurrentS(),self.cM.get_courses())
                        print(self.cM.get_courses())
                        self.view.add_window.close()
        elif type == "Module":
            try:
                credits = int(array[2])
                grade = float(array[3])
            except:
                print("INVALID TYPE")
            else:
                if (credits < 0 or credits > 180) or (grade < 0 or grade > 100.0):
                    print("INVALID INPUTS")
                else:
                    id = self.mM[0].get_nextID()
                    course = pStack[0]
                    year = pStack[1]
                    for i in self.cM.get_courses():
                        if i.get_title() == course:
                            courseid = i.get_id()
                            for j in self.yM[1:]:
                                years = j.get_years()
                                print(years)
                                if (years[0].get_cid() == courseid):
                                    for k in years:
                                        if k.get_title() == year:
                                            yearid = k.get_id()
                                            for l in self.mM[1:]:
                                                modules = l.get_modules()
                                                if modules[0].get_yid() == yearid:
                                                    print("Found")
                                                    empty = False
                                                    l.add_module(model.Module(id,title,credits,grade,yearid))
                                                    self.displayData(self.view.getCurrentS(),modules)
                                                    self.view.add_window.close()
                                                    break
                                            if (empty):
                                                self.mM.append(model.moduleModel(yearid))
                                                modules = self.mM[-1].get_modules()
                                                self.mM[-1].add_module(model.Module(id,title,credits,grade,yearid))
                                                self.displayData(self.view.getCurrentS(),modules)
                                                self.view.add_window.close()
                                                break

        else:
            try:
                weight = int(array[2])
                grade = float(array[3])
            except:
                print("INVALID TYPE")
            else:
                if (weight < 0 or weight > 100) or (grade < 0 or grade > 100):
                    print("INVALID INPUT")
                elif (type == "Year"):
                    id = self.yM[0].get_nextID()
                    course = pStack[0]
                    for i in self.cM.get_courses():
                        if i.get_title() == course:
                            courseid = i.get_id()
                            for j in self.yM[1:]:
                                years = j.get_years()
                                if (years[0].get_cid() == courseid):
                                    empty = False
                                    j.add_year(model.Year(id,title,weight,grade,courseid))
                                    self.displayData(self.view.getCurrentS(),years)
                                    self.view.add_window.close()
                                    break
                            if(empty):
                                self.yM.append(model.yearModel(courseid))
                                years = self.yM[-1].get_years()
                                self.yM[-1].add_year(model.Year(id,title,weight,grade,courseid))
                                self.displayData(self.view.getCurrentS(),years)
                                self.view.add_window.close()
                                break
                elif (type == "Assessment"):
                    if (title == "Coursework"):
                        id = self.aseM[0].get_nextID_CW()
                    else:
                        id = self.aseM[0].get_nextID_E()
                    course = pStack[0]
                    year = pStack[1]
                    module = pStack[2]
                    for i in self.cM.get_courses():
                        if i.get_title() == course:
                            courseid = i.get_id()
                            for j in self.yM[1:]:
                                years = j.get_years()
                                if (years[0].get_cid() == courseid):
                                    for k in years:
                                        if k.get_title() == year:
                                            yearid = k.get_id()
                                            for l in self.mM[1:]:
                                                modules = l.get_modules()
                                                if (modules[0].get_yid()==yearid):
                                                    for m in modules:
                                                        if m.get_title() == module:
                                                            moduleid = m.get_id()
                                                            for n in self.aseM[1:]:
                                                                assessments = n.get_assessments()
                                                                if (assessments[0].get_mid() == moduleid):
                                                                    empty = False
                                                                    cwPres = False
                                                                    ePres = False
                                                                    for o in assessments:
                                                                        if o.get_title() == "Coursework":
                                                                            cwPres = True
                                                                        else:
                                                                            ePres = True
                                                                    if (title == "Coursework" and not cwPres):
                                                                        n.add_cw(model.Coursework(id,weight,grade,moduleid))
                                                                        self.displayData(self.view.getCurrentS(),assessments)
                                                                        self.view.add_window.close()
                                                                    elif (title == "Exam" and not ePres):
                                                                        n.add_e(model.Exam(id,weight,grade,moduleid))
                                                                        self.displayData(self.view.getCurrentS(),assessments)
                                                                        self.view.add_window.close()
                                                                    else:
                                                                        print(title," Already Exists in Module")
                                                                    break
                                                            if(empty):
                                                                self.aseM.append(model.assessmentModel(moduleid))
                                                                assessments = self.aseM[-1].get_assessments()
                                                                if (title == "Coursework"):
                                                                    self.aseM[-1].add_cw(model.Coursework(id,weight,grade,moduleid))
                                                                    self.displayData(self.view.getCurrentS(),assessments)
                                                                    self.view.add_window.close()
                                                                else:
                                                                    self.aseM[-1].add_e(model.Exam(id,weight,grade,moduleid))
                                                                    self.displayData(self.view.getCurrentS(),assessments)
                                                                    self.view.add_window.close()
                                                                break
                else:
                    id = self.asiM[0].get_nextID()
                    course = pStack[0]
                    year = pStack[1]
                    module = pStack[2]
                    assessment = pStack[3]
                    for i in self.cM.get_courses():
                        if i.get_title() == course:
                            courseid = i.get_id()
                            for j in self.yM[1:]:
                                years = j.get_years()
                                if (years[0].get_cid() == courseid):
                                    for k in years:
                                        if k.get_title() == year:
                                            yearid = k.get_id()
                                            for l in self.mM[1:]:
                                                modules = l.get_modules()
                                                if (modules[0].get_yid()==yearid):
                                                    for m in modules:
                                                        if m.get_title() == module:
                                                            moduleid = m.get_id()
                                                            for n in self.aseM[1:]:
                                                                assessments = n.get_assessments()
                                                                if (assessments[0].get_mid() == moduleid):
                                                                    for o in assessments:
                                                                        if o.get_title() == assessment:
                                                                            assessmentid = o.get_id()
                                                                            for p in self.asiM[1:]:
                                                                                assignments = p.get_assignments()
                                                                                if (assignments[0].get_cid() == assessmentid):
                                                                                    empty = False
                                                                                    p.add_assignment(model.Assignment(id,title,weight,grade,assessmentid))
                                                                                    self.displayData(self.view.getCurrentS(),assignments)
                                                                                    self.view.add_window.close()
                                                                                    break
                                                                            if (empty):
                                                                                self.asiM.append(model.assignmentModel(assessmentid))
                                                                                assignments = self.asiM[-1].get_assignments()
                                                                                self.asiM[-1].add_assignment(model.Assignment(id,title,weight,grade,assessmentid))
                                                                                self.displayData(self.view.getCurrentS(),assignments)
                                                                                self.view.add_window.close()
                                                                                break

                     
                                                


                


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
    
    def changeScreenPrev(self):
        pStack = self.view.pageStack.getStack()
        currentS = self.view.getCurrentS()
        if currentS == self.view.years_screen:
            w = self.view.getCourseS()
            courses = self.cM.get_courses()
            self.displayData(w,courses)
            self.view.pageStack.pop()
        elif currentS == self.view.modules_screen:
            w = self.view.getYearS()
            course = pStack[0]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        years = j.get_years()
                        if (years[0].get_cid() == courseid):
                            self.displayData(w,years)
                            self.view.pageStack.pop()
                            break
        elif currentS == self.view.assessments_screen:
            w = self.view.getModuleS()
            course = pStack[0]
            year = pStack[1]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        years = j.get_years()
                        if (years[0].get_cid() == courseid):
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM[1:]:
                                        modules = l.get_modules()
                                        if (modules[0].get_yid()==yearid):
                                            self.displayData(w,modules)
                                            self.view.pageStack.pop()
                                            break
        else:
            w = self.view.getAssessmentS()
            course = pStack[0]
            year = pStack[1]
            module = pStack[2]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        years = j.get_years()
                        if (years[0].get_cid() == courseid):
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM[1:]:
                                        modules = l.get_modules()
                                        if (modules[0].get_yid() == yearid):
                                            for m in modules:
                                                if (m.get_title() == module):
                                                    moduleid = m.get_id()
                                                    for n in self.aseM[1:]:
                                                        assessments = n.get_assessments()
                                                        if (assessments[0].get_mid() == moduleid):
                                                            self.displayData(w,assessments)
                                                            self.view.pageStack.pop()
                                                            break
        print(pStack)
        print(len(pStack))
                    

    def changeScreen(self,title):
        print("Change screen started")
        pStack = self.view.pageStack.getStack()
        currentS = self.view.getCurrentS()
        empty = True
        if currentS == self.view.courses_screen:
            w = self.view.getYearS()
            for i in self.cM.get_courses():
                if i.get_title() == title:
                    id = i.get_id()
                    for j in self.yM[1:]:
                        print("L")
                        years = j.get_years()
                        print(years)
                        if years[0].get_cid() == id:
                            print("Found")
                            empty = False
                            self.displayData(w,years)
                            break
                    if(empty): 
                        self.displayData(w,[])
                        break
            self.view.pageStack.push(title)
                    
        
        elif currentS == self.view.years_screen:
            w = self.view.getModuleS()
            course = pStack[0]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        years = j.get_years()
                        if years[0].get_cid() == courseid:
                            for k in years:
                                if k.get_title() == title:
                                    id = k.get_id()
                                    for l in self.mM[1:]:
                                        modules = l.get_modules()
                                        if modules[0].get_yid() == id:
                                            empty = False
                                            self.displayData(w,modules)
                                            break
                                    if(empty):
                                        self.displayData(w,[])
                                        break
            self.view.pageStack.push(title)
        elif currentS == self.view.modules_screen:
            w = self.view.getAssessmentS()
            course = pStack[0]
            year = pStack[1]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        years = j.get_years()
                        if years[0].get_cid() == courseid:
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM[1:]:
                                        modules = l.get_modules()
                                        if modules[0].get_yid() == yearid:
                                            for m in modules:
                                                if m.get_title() == title:
                                                    id = m.get_id()
                                                    for n in self.aseM[1:]:
                                                        print("TEST")
                                                        assessments = n.get_assessments()
                                                        if assessments[0].get_mid() == id:
                                                            empty = False
                                                            self.displayData(w,assessments)
                                                            break
                                                    if (empty):
                                                        self.displayData(w,[])
            self.view.pageStack.push(title)
        elif currentS == self.view.assessments_screen and title == "Coursework":
            w = self.view.getAssignmentS()
            course = pStack[0]
            year = pStack[1]
            module = pStack[2]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        years = j.get_years()
                        if years[0].get_cid() == courseid:
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM[1:]:
                                        modules = l.get_modules()
                                        if modules[0].get_yid() == yearid:
                                            for m in modules:
                                                if m.get_title() == module:
                                                    moduleid = m.get_id()
                                                    for n in self.aseM[1:]:
                                                        assessments = n.get_assessments()
                                                        if assessments[0].get_mid() == moduleid:
                                                            for o in assessments:
                                                                if o.get_title() == title:
                                                                    id = o.get_id()
                                                                    for p in self.asiM[1:]:
                                                                        assignments = p.get_assignments()
                                                                        if assignments[0].get_cid() == id:
                                                                            empty = False
                                                                            self.displayData(w,assignments)
                                                                            break
                                                                    if(empty):
                                                                        self.displayData(w,[])
            self.view.pageStack.push(title)
        print(pStack)
        print(len(pStack))



    
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
            if (totalCredits == 0):
                cValue = 0
            else:
                cValue += (credits[i] * grades[i])/totalCredits
            array.append(cValue)


        

        


        



    
     
         

    

    
     