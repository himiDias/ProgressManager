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
        self.view.editItemClicked.connect(self.editItem)
    
    def editItem(self,array):
        pStack = self.view.pageStack.getStack()
        currentS = self.view.getCurrentS()
        type = array[0]
        title = array[1]
        prevTitle = array[2]
        exists = False
        if type == "Course":
            if not title:
                print("INVALID TITLE")
                self.view.edit_window.alertL.setText("Invalid Title")
            else:
                for i in self.cM.get_courses():
                    if i.get_title() == title:
                        print("Title already exists")
                        self.view.edit_window.alertL.setText("Title name already exists")
                    else:
                        for j in self.cM.get_courses():
                            if j.get_title() == prevTitle:
                                j.update_title(title)
                                self.cM.edit_course(model.Course(j.get_id(),j.get_title(),j.get_grade()))
                                self.displayData(currentS,self.cM.get_courses())
                                self.view.edit_window.close()
                                break
        elif type == "Module":
            try:
                credits = int(array[3])      
            except:
                print("INVALID TYPE")
                self.view.edit_window.alertL.setText("Credits must be Integer")
            else:
                if (credits < 0 or credits > 180):
                    print("INVALID INPUTS")
                    self.view.edit_window.alertL.setText("Credits must be between 0-180")
                elif not(title):
                    print("INVALID TITLE")
                    self.view.edit_window.alertL.setText("Invalid Title")
                else:
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
                                                    for x in modules:
                                                        if x.get_title() == title and x.get_title() != prevTitle:
                                                            exists = True
                                                            print("Title already exists")
                                                            self.view.edit_window.alertL.setText("Title name already exists")
                                                    if not(exists):
                                                        for x in modules:
                                                            if x.get_title() == prevTitle:
                                                                x.update_title(title)
                                                                x.update_credits(credits)
                                                                l.edit_module(model.Module(x.get_id(),x.get_title(),x.get_credits(),x.get_grade(),yearid))
                                                                self.displayData(currentS,modules)
                                                                self.updateGrade(modules,len(pStack))
                                                                self.view.edit_window.close()
                                                                break

        else:
            try:
                weight = int(array[3])                
            except:
                print("INVALID TYPE")
                self.view.edit_window.alertL.setText("Weight must be Integer")
            else:
                if (weight < 0 or weight > 100):
                    print("INVALID INPUT")
                    self.view.edit_window.alertL.setText("Weight must be between 0-100")
                elif not(title):
                    print("INVALID TITLE")
                    self.view.edit_window.alertL.setText("Invalid Title")
                elif (type == "Year"):
                    course = pStack[0]
                    for i in self.cM.get_courses():
                        if i.get_title() == course:
                            courseid = i.get_id()
                            for j in self.yM[1:]:
                                years = j.get_years()
                                if (years[0].get_cid() == courseid):
                                    for x in years:
                                        if x.get_title() == title and x.get_title() != prevTitle:
                                            exists = True
                                            print("Title already exists")
                                            self.view.edit_window.alertL.setText("Title name already exists")
                                    if not (exists):
                                        for x in years:
                                            if x.get_title() == prevTitle:
                                                x.update_title(title)
                                                x.update_weight(weight)
                                                j.edit_year(model.Year(x.get_id(),x.get_title(),x.get_weight(),x.get_grade(),courseid))
                                                self.displayData(currentS,years)
                                                self.updateGrade(years,len(pStack))
                                                self.view.edit_window.close()
                                                break
                elif (type == "Assessment"):
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
                                                                    if (title == "Coursework"):
                                                                        for x in assessments:
                                                                            if x.get_title() == "Coursework":
                                                                                x.update_weight(weight)
                                                                                n.edit_cw(model.Coursework(x.get_id(),x.get_weight(),x.get_grade(),moduleid))
                                                                                self.displayData(currentS,assessments)
                                                                                self.updateGrade(assessments,len(pStack))
                                                                                self.view.edit_window.close()
                                                                                break
                                                                    elif (title == "Exam"):
                                                                        for x in assessments:
                                                                            if x.get_title() == "Exam":
                                                                                x.update_weight(weight)
                                                                                n.edit_e(model.Exam(x.get_id(),x.get_weight(),x.get_grade(),moduleid))
                                                                                self.displayData(currentS,assessments)
                                                                                self.updateGrade(assessments,len(pStack))
                                                                                self.view.edit_window.close()
                                                                                break
                else:
                    try:
                        grade = float(array[4])                
                    except:
                        print("INVALID TYPE")
                        self.view.edit_window.alertL.setText("Grade must be Integer/Float")
                    else:
                        if (grade < 0 or grade > 100):
                            print("INVALID INPUT")
                            self.view.edit_window.alertL.setText("Grade must be between 0-100")
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
                                                                                            for x in assignments:
                                                                                                if x.get_title == title:
                                                                                                    exists= True
                                                                                                    print("Title already exists")
                                                                                                    self.view.edit_window.alertL.setText("Title name already exists")
                                                                                            if not(exists):
                                                                                                for x in assignments:
                                                                                                    if x.get_title() == prevTitle:
                                                                                                        x.update_title(title)
                                                                                                        x.update_weight(weight)
                                                                                                        x.update_grade(grade)  
                                                                                                        p.edit_assignment(model.Assignment(x.get_id(),x.get_title(),x.get_weight(),x.get_grade(),assessmentid))
                                                                                                        self.displayData(currentS,assignments)
                                                                                                        self.updateGrade(assignments,len(pStack))
                                                                                                        self.view.edit_window.close()
                                                                                                        break
                                                                             
                                 


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
                                    self.updateGrade(years,len(pStack))
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
                                                    self.updateGrade(modules,len(pStack))
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
                                                            self.updateGrade(assessments,len(pStack))
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
                                                                                    self.updateGrade(assignments,len(pStack))
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
                self.view.add_window.alertL.setText("Grade must be Integer/Real")
            else:
                if  grade <0 or grade > 100.0:
                    print("INVALID INPUTS")
                    self.view.add_window.alertL.setText("Grade must be between 0-100")
                elif not title:
                    print("INVALID TITLE")
                    self.view.add_window.alertL.setText("Invalid Title")
                else:
                    for i in self.cM.get_courses():
                        if i.get_title() == title:
                            exists = True
                            print("Title already exists")
                            self.view.add_window.alertL.setText("Title name already exists")
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
                self.view.add_window.alertL.setText("Grade must be Integer/Real\nCredits must be Integer")
            else:
                if (credits < 0 or credits > 180) or (grade < 0 or grade > 100.0):
                    print("INVALID INPUTS")
                    self.view.add_window.alertL.setText("Grade must be between 0-100\nCredits must be between 0-180")
                elif not(title):
                    print("INVALID TITLE")
                    self.view.add_window.alertL.setText("Invalid Title")
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
                                                    for x in modules:
                                                        if x.get_title() == title:
                                                            exists = True
                                                            print("Title already exists")
                                                            self.view.add_window.alertL.setText("Title name already exists")
                                                    if not(exists):
                                                        print("Found")
                                                        empty = False
                                                        l.add_module(model.Module(id,title,credits,grade,yearid))
                                                        self.displayData(self.view.getCurrentS(),modules)
                                                        self.updateGrade(modules,len(pStack))
                                                        self.view.add_window.close()
                                                        break
                                            if not(exists):
                                                if (empty):
                                                    self.mM.append(model.moduleModel(yearid))
                                                    modules = self.mM[-1].get_modules()
                                                    self.mM[-1].add_module(model.Module(id,title,credits,grade,yearid))
                                                    self.displayData(self.view.getCurrentS(),modules)
                                                    self.updateGrade(modules,len(pStack))
                                                    self.view.add_window.close()
                                                    break

        else:
            try:
                weight = int(array[2])
                grade = float(array[3])
            except:
                print("INVALID TYPE")
                self.view.add_window.alertL.setText("Grade must be Integer/Real\nWeight must be Integer")
            else:
                if (weight < 0 or weight > 100) or (grade < 0 or grade > 100):
                    print("INVALID INPUT")
                    self.view.add_window.alertL.setText("Grade and Weight must be between 0-100")
                elif not(title):
                    print("INVALID TITLE")
                    self.view.add_window.alertL.setText("Invalid Title")
                elif (type == "Year"):
                    id = self.yM[0].get_nextID()
                    course = pStack[0]
                    for i in self.cM.get_courses():
                        if i.get_title() == course:
                            courseid = i.get_id()
                            for j in self.yM[1:]:
                                years = j.get_years()
                                if (years[0].get_cid() == courseid):
                                    for x in years:
                                        if x.get_title() == title:
                                            exists = True
                                            print("Title already exists")
                                            self.view.add_window.alertL.setText("Title name already exists")
                                    if not (exists):
                                        empty = False
                                        j.add_year(model.Year(id,title,weight,grade,courseid))
                                        self.displayData(self.view.getCurrentS(),years)
                                        self.updateGrade(years,len(pStack))
                                        self.view.add_window.close()
                                        break
                            if not(exists):
                                if(empty):
                                    self.yM.append(model.yearModel(courseid))
                                    years = self.yM[-1].get_years()
                                    self.yM[-1].add_year(model.Year(id,title,weight,grade,courseid))
                                    self.displayData(self.view.getCurrentS(),years)
                                    self.updateGrade(years,len(pStack))
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
                                                                        self.updateGrade(assessments,len(pStack))
                                                                        self.view.add_window.close()
                                                                    elif (title == "Exam" and not ePres):
                                                                        n.add_e(model.Exam(id,weight,grade,moduleid))
                                                                        self.displayData(self.view.getCurrentS(),assessments)
                                                                        self.updateGrade(assessments,len(pStack))
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
                                                                    self.updateGrade(assessments,len(pStack))
                                                                    self.view.add_window.close()
                                                                else:
                                                                    self.aseM[-1].add_e(model.Exam(id,weight,grade,moduleid))
                                                                    self.displayData(self.view.getCurrentS(),assessments)
                                                                    self.updateGrade(assessments,len(pStack))
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
                                                                                    for x in assignments:
                                                                                        if x.get_title == title:
                                                                                            exists= True
                                                                                            print("Title already exists")
                                                                                            self.view.add_window.alertL.setText("Title name already exists")
                                                                                    if not(exists):
                                                                                        empty = False
                                                                                        p.add_assignment(model.Assignment(id,title,weight,grade,assessmentid))
                                                                                        self.displayData(self.view.getCurrentS(),assignments)
                                                                                        self.updateGrade(assignments,len(pStack))
                                                                                        self.view.add_window.close()
                                                                                        break
                                                                            if not(exists):
                                                                                if (empty):
                                                                                    self.asiM.append(model.assignmentModel(assessmentid))
                                                                                    assignments = self.asiM[-1].get_assignments()
                                                                                    self.asiM[-1].add_assignment(model.Assignment(id,title,weight,grade,assessmentid))
                                                                                    self.displayData(self.view.getCurrentS(),assignments)
                                                                                    self.updateGrade(assignments,len(pStack))
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
        
        return cValue
    
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
        
        return cValue
    

    def checkWeights(self,weights):
        valid = False
        weightSum = 0
        for i in weights:
            weightSum+=i
        
        if weightSum == 100:
            valid = True
        
        return valid

    def updateGrade(self,array,pStackL):
        pStack = self.view.pageStack.getStack()
        temp = []
        grades = self.getGrades(array)
        if(pStackL == 2):
            credits = self.getCredits(array)
            newGrade = self.calculateCumulativeScoreModules(credits,grades,temp)
        else:
            weights = self.getWeights(array)
            newGrade = self.calculateCumulativeScore(weights,grades,temp)
        
        if pStackL == 1:
            course = pStack[0]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    print(newGrade)
                    i.update_grade(newGrade)
                    self.cM.edit_course(model.Course(i.get_id(),i.get_title(),i.get_grade()))
        elif pStackL == 2:
            course = pStack[0]
            year = pStack[1]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        if j.courseId == courseid:
                            years = j.get_years()
                            for k in years:
                                if k.get_title() == year:
                                    k.update_grade(newGrade)
                                    j.edit_year(model.Year(k.get_id(),k.get_title(),k.get_weight(),k.get_grade(),courseid))
                                    self.updateGrade(years,pStackL - 1)
                                    break
        elif pStackL == 3:
            course = pStack[0]
            year = pStack[1]
            module = pStack[2]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        if j.courseId == courseid:
                            years = j.get_years()
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM[1:]:
                                        if l.yearId == yearid:
                                            modules = l.get_modules()
                                            for m in modules:
                                                if m.get_title() == module:
                                                    m.update_grade(newGrade)
                                                    l.edit_module(model.Module(m.get_id(),m.get_title(),m.get_credits(),m.get_grade(),m.get_yid()))
                                                    self.updateGrade(modules,pStackL - 1)
                                                    break
        elif pStackL == 4:
            course = pStack[0]
            year = pStack[1]
            module = pStack[2]
            assessment = pStack[3]
            for i in self.cM.get_courses():
                if i.get_title() == course:
                    courseid = i.get_id()
                    for j in self.yM[1:]:
                        if j.courseId == courseid:
                            years = j.get_years()
                            for k in years:
                                if k.get_title() == year:
                                    yearid = k.get_id()
                                    for l in self.mM[1:]:
                                        if l.yearId == yearid:
                                            modules = l.get_modules()
                                            for m in modules:
                                                if m.get_title() == module:
                                                    moduleid = m.get_id()
                                                    for n in self.aseM[1:]:
                                                        if n.moduleId == moduleid:
                                                            assessments = n.get_assessments()
                                                            for o in assessments:
                                                                if o.get_title() == assessment:
                                                                    o.update_grade(newGrade)
                                                                    n.edit_cw(model.Coursework(o.get_id(),o.get_weight(),o.get_grade(),o.get_mid()))
                                                                    self.updateGrade(assessments,pStackL -1)
                                                                    break
        pass
    
    
    def getWeights(self,model):
        weights = []
        for i in model:
            weights.append(i.get_weight())
        
        return weights
    
    def getGrades(self,model):
        grades = []
        for i in model:
            grades.append(i.get_grade())
        
        return grades
    
    def getCredits(self,model):
        credits = []
        for i in model:
            credits.append(i.get_credits())
        
        return credits


        

        


        



    
     
         

    

    
     