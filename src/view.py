from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pathlib import Path
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import sys

from model import courseModel,yearModel,moduleModel,assessmentModel,assignmentModel
from controller import Controller

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = plt.Figure(figsize=(width,height), dpi = dpi)
        super(MplCanvas, self).__init__(fig)
        self.axes = fig.add_subplot(111)
        self.axes.axhline(y=40.0, color='r', linestyle='-')
        self.axes.axhline(y=50.0, color='orange', linestyle='-')
        self.axes.axhline(y=60.0, color='green', linestyle='-')
        self.axes.axhline(y=70.0, color='darkgreen', linestyle='-')
        self.draw()

         

class MainWindow(QMainWindow):
    itemClicked = pyqtSignal(str)
    previousClicked = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("University Progress Tracker")
        self.setWindowIcon(QIcon('./assets/mainP.jpg'))
        self.setGeometry(100,100,1000,800)

        self.stack = QStackedWidget()
        self.pageStack = Stack()
        self.setCentralWidget(self.stack)

        self.login_screen = LoginScreen(self)
        self.courses_screen = CoursesScreen(self)
        self.years_screen = YearsScreen(self)
        self.modules_screen = ModulesScreen(self)
        self.assessments_screen = AssessmentScreen(self)
        self.assignments_screen = AssignmentsScreen(self)

        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.courses_screen)
        self.stack.addWidget(self.years_screen)
        self.stack.addWidget(self.modules_screen)
        self.stack.addWidget(self.assessments_screen)
        self.stack.addWidget(self.assignments_screen)


        # TESTING IS hardcoded as controller would be responsible for determining and passing in correct values for functions 
        #======================================
        # TEST FOR DISPLAYING COURSES
        #print("TEST DISPLAY")
        #self.courses_screen.displayCourses(["Physics","Maths","CS","English","Physc"],['45.0','77.0','65.3','15.0','34.2'])

        # TEST FOR CLEARING COURSES
        print("TEST CLEAR")
        #self.courses_screen.clearCourses()
        #======================================
        #TEST FOR DISPLAYING YEARS
        print("TEST DISPLAY")
        #self.years_screen.displayYears(['Year 1','Year 2','Year 3'],['0','40','60'],['70','85.6','78.1'])

        #TEST FOR DISPLAYING GRAPH
        print("TEST GRAPH")
        #(0*70)+(85.6*0.4)=34.24 +(78.1*0.6)= 81.1
        #self.years_screen.displayGraph([0,34.24,81.1],['Year 1','Year 2','Year 3'])
        
        #TEST FOR CLEARING YEARS + GRAPH
        print("TEST CLEAR")
        #self.years_screen.clearYears()
        #=======================================
        #TEST FOR DISPLAYING MODULES + GRAPH
        print("TEST DISPLAY")
        self.modules_screen.displayModules(['Kinematics','Physic I','Physics II','Motions','Forces'],['10','10','20','10','10'],['34.2','60.4','56.0','89.4','73.0'])
        self.modules_screen.displayGraph([0,5.7,15.7,34.4,49.3,61.5],['_','Kinematics','Physic I','Physics II','Motions','Forces'])
        
        #TEST FOR CLEARING MODULES + GRAPH
        print("TEST CLEAR")
        #self.modules_screen.clearModules()
        #=======================================
        #TEST FOR DISPLAYING ASSESSMENTS + GRAPH
        print("TEST DISPLAY")
        self.assessments_screen.displayAssessments(['Coursework','Exam'],['70','30'],['86','75'])
        self.assessments_screen.displayGraph([0,60.2,82.7],['_','Coursework','Exam'])

        #TEST FOR CLEARING ASSESSMENTS + GRAPH
        #self.assessments_screen.clearAssessments()
        #=======================================
        #TEST FOR DISPLAYING ASSIGNMENTS + GRAPH
        self.assignments_screen.displayAssignments(['CW1','CW2','CW3a','CW3b'],['5','10','25','30'],['100','100','95','93'])
        self.assignments_screen.displayGraph([0,13,25.2,57,77],['_','CW1','CW2','CW3a','CW3b'])

        #TEST FOR CLEARING ASSIGNMENTS + GRAPH
        #self.assignments_screen.clearAssignments()
        #=======================================
        #TEST FOR PAGE STACK
        print("STACK TEST")
        #self.pageStack.push('Physics')
        #self.pageStack.push('Year 1')
        #self.pageStack.push('Motions')

        #self.pageStack.pop()
        #self.pageStack.pop()
        #self.pageStack.pop()
        #=======================================
         


        self.stack.setCurrentWidget(self.login_screen)

        prev_action = QAction(QIcon('./assets/arrowBack.jpg'),'Previous',self)
        prev_action.triggered.connect(self.setPrevWidget)
        add_action = QAction(QIcon('./assets/add.jpg'),'Add',self)
        add_action.triggered.connect(self.addItem)
        toolbar = QToolBar('Main Toolbar')
        self.addToolBar(toolbar)
        toolbar.addAction(prev_action)
        toolbar.addAction(add_action)
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("ProgressManager v1.0")

        self.show()

    def setPrevWidget(self):
        #Take values of stack to controller, determine what needs to be displayed on screen
        if (self.pageStack.isEmpty()):
            print("None in Stack")
            pass
        else:
            self.previousClicked.emit()
    
    def addItem(self):
        if(self.stack.currentWidget().getType()):
            self.add_window = addWindow(self.stack.currentWidget().getType())
            self.add_window.show()
        else:
            pass
    
    def getLoginS(self):
        return self.login_screen
    
    def getCourseS(self):
        return self.courses_screen
    
    def getYearS(self):
        return self.years_screen
    
    def getModuleS(self):
        return self.modules_screen
    
    def getAssessmentS(self):
        return self.assessments_screen
    
    def getAssignmentS(self):
        return self.assignments_screen
    
    def getCurrentS(self):
        return self.stack.currentWidget()
    
    def refreshView(self,widget,*args):
        #function to actually set the current widget, and display data
        # First clear current display of the chosen widget
        #Then display new data given on the chosen widget
        self.stack.setCurrentWidget(widget)

        arr1_str = [str(i) for i in args[1]]
        arr2_str = [str(i) for i in args[2]]
        if type(widget) == CoursesScreen:
            self.courses_screen.clearCourses()
            self.courses_screen.displayCourses(args[0],arr1_str)
        elif type(widget) == YearsScreen:
            self.years_screen.clearYears()
            self.years_screen.displayYears(args[0],arr1_str,arr2_str)
            args[0].insert(0,'_')
            self.years_screen.displayGraph(args[0],args[3])
        elif type(widget) == ModulesScreen:
            self.modules_screen.clearModules()
            self.modules_screen.displayModules(args[0],arr1_str,arr2_str)
            args[0].insert(0,'_')
            self.modules_screen.displayGraph(args[0],args[3])
        elif type(widget) == AssessmentScreen:
            self.assessments_screen.clearAssessments()
            self.assessments_screen.displayAssessments(args[0],arr1_str,arr2_str)
            args[0].insert(0,'_')
            self.assessments_screen.displayGraph(args[0],args[3])
        else:
            self.assignments_screen.clearAssignments()
            self.assignments_screen.displayAssignments(args[0],arr1_str,arr2_str)
            args[0].insert(0,'_')
            self.assignments_screen.displayGraph(args[0],args[3])
         

class addWindow(QWidget):
    def __init__(self,IType):
        super().__init__()
        self.setWindowTitle('Add '+ IType)
        self.setGeometry(100,100,300,200)
        layout = QVBoxLayout()
        self.setLayout(layout)

        titleL = QLabel("Enter "+IType+" Details")
        layout.addWidget(titleL)

        tLayout = QHBoxLayout()
        titleD = QWidget()
        titleD.setLayout(tLayout)
        tLabel = QLabel(" Enter Title")
        self.tBox = QLineEdit(
            self,
            placeholderText = 'Title',
            maxLength = 50
        )
        tLayout.addWidget(tLabel)
        tLayout.addWidget(self.tBox)
        layout.addWidget(titleD)

        if(IType == "Year" or IType == "Assessment" or IType == "Assignment"):
            wLayout = QHBoxLayout()
            weightD = QWidget()
            weightD.setLayout(wLayout)
            wLabel = QLabel("Enter Weight")
            self.wBox = QLineEdit(
                self,
                placeholderText = "Weight",
                maxLength = 2
            )
            wLayout.addWidget(wLabel)
            wLayout.addWidget(self.wBox)
            layout.addWidget(weightD)
        elif(IType == "Module"):
            cLayout = QHBoxLayout()
            creditD = QWidget()
            creditD.setLayout(cLayout)
            cLabel = QLabel("Enter Credits")
            self.cBox = QLineEdit(
                self,
                placeholderText = "Credits",
                maxLength = 3
            )
            cLayout.addWidget(cLabel)
            cLayout.addWidget(self.cBox)
            layout.addWidget(creditD)
        
        gLayout = QHBoxLayout()
        gradeD = QWidget()
        gradeD.setLayout(gLayout)
        gLabel = QLabel("Enter Grade")
        self.gBox = QLineEdit(
            self,
            placeholderText = 'Grade',
            maxLength = 3
        )
        gLayout.addWidget(gLabel)
        gLayout.addWidget(self.gBox)
        layout.addWidget(gradeD)

        oLayout = QHBoxLayout()
        optionsD = QWidget()
        optionsD.setLayout(oLayout)
        addB = QPushButton("Add")
        addB.clicked.connect(self.addNewItem)
        cancelB = QPushButton("Cancel")
        cancelB.clicked.connect(self.close)
        oLayout.addWidget(addB)
        oLayout.addWidget(cancelB)
        layout.addWidget(optionsD)
    
    def addNewItem(self):
        #function to check validity of entered data
        #connect to controller to add values to database
        #controller will then call refreshView again 
        pass


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self,item):
        self.stack.append(item)
        self.top += 1
        print(self.top)
    def pop(self):
        self.stack.pop(self.top)
        self.top -= 1

    def getSize(self):
        return self.top + 1
    
    def peak(self):
        return self.stack[self.top]
    
    def isEmpty(self):
        if self.top == -1:
            print("Empty")
            return True
        else:
            print("Not Empty")
            return False
        
    def getStack(self):
        return self.stack


class LoginScreen(QWidget):
    loginClicked = pyqtSignal(str,str)
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.type = None
 
        titleL = QLabel('Enter DB credentials')
        titleL.setObjectName("titleL")
        userP = QPixmap('./assets/userP.jpg')
        passP = QPixmap('./assets/passP.jpg')
        userP = userP.scaled(50,50)
        passP = passP.scaled(50,50)
        userL = QLabel()
        passL = QLabel()
        userL.setPixmap(userP)
        passL.setPixmap(passP)
        loginB = QPushButton('Login')
        loginB.clicked.connect(self.checkCred)

        username = QWidget()
        userLayout = QHBoxLayout()
        password = QWidget()
        passwLayout = QHBoxLayout()
        username.setLayout(userLayout)
        password.setLayout(passwLayout)
        self.user = QLineEdit(
            self,
            placeholderText = 'Username',
            maxLength = 20
        )

        self.passw = QLineEdit(
            self,
            placeholderText = 'Password',
            echoMode = QLineEdit.Password
        )
        userLayout.addWidget(userL)
        userLayout.addWidget(self.user)
        passwLayout.addWidget(passL)
        passwLayout.addWidget(self.passw)
        layout.addWidget(titleL)
        layout.addWidget(username)
        layout.addWidget(password)
        layout.addWidget(loginB)

    def getType(self):
        return self.type

    
    def checkCred(self):
        # Connect to controller, to check creds then load up correct course screen
        un = self.user.text()
        pw = self.passw.text()
        print(un,pw)
        self.loginClicked.emit(un,pw)
        pass

class CoursesScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.type = "Course"
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        titleL = QLabel('Courses')
        self.layout.addWidget(titleL,0,0,1,4,alignment=Qt.AlignmentFlag.AlignCenter)
         

    def displayCourses(self,titles,grades):
        count = 0
        row = 1
        buttons = []
         
        for course in range(len(titles)):
            tempGrade = QLabel("Grade: "+grades[course])
            tempB = QPushButton(titles[course])
            tempB.clicked.connect(lambda checked,course=titles[course]: self.handle_course_click(course))
            buttons.append(tempB)
            tempL = QVBoxLayout()
            tempC = QWidget()
            tempC.setLayout(tempL)
            tempL.addWidget(tempB)
            tempL.addWidget(tempGrade)
            if (count == 4):
                count = 0
                row += 1
            self.layout.addWidget(tempC,row,count)
            count += 1
    
    def clearCourses(self):
        # Code to clear all courses from screen, called before calling displayCourses so as to not overlap
        row = 1
        count = 0

        widgetItem = self.layout.itemAtPosition(row,count) 
        
        while widgetItem is not None:
            widget = widgetItem.widget()
            self.layout.removeWidget(widget)
            print(count)
            count += 1
            if(count == 4):
                count = 0
                row += 1
            widgetItem = self.layout.itemAtPosition(row,count)
    
    def handle_course_click(self,course):
        #Code to set current widget to the years screen of the passed in course, controller would access the chosen course,
        # then retrieve what needs to be displayed
        print(course)
        self.main_window.itemClicked.emit(course)
    
    def getType(self):
        return self.type
             
            
class YearsScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.type = "Year"
        self.first = True

        titleL = QLabel('Years')
        self.layout.addWidget(titleL,0,0,1,4,alignment=Qt.AlignmentFlag.AlignCenter)
    
    def displayYears(self,titles,weights,grades):
        if (self.first):
            self.first = False
        count = 0
        row = 1
        buttons = []
        # Code to display all years for the course
        for year in range(len(titles)):
            tempWeight = QLabel("Weight: "+weights[year])
            tempGrade = QLabel("Grade: "+grades[year])
            tempB = QPushButton(titles[year])
            tempB.clicked.connect(lambda checked,year=titles[year]: self.handle_year_click(year))
            buttons.append(tempB)
            tempL = QVBoxLayout()
            tempC = QWidget()
            tempC.setLayout(tempL)
            tempL.addWidget(tempB)
            tempL.addWidget(tempWeight)
            tempL.addWidget(tempGrade)
            if (count == 4):
                count = 0
                row += 1    
            self.layout.addWidget(tempC,row,count)
            count +=1

    def displayGraph(self,years,grades):
        # Code to display the graph of progress for the course
        # For all graphs, the grades array is the cumulative value of the grades as modules increase
        if (len(years) > 1):
            self.graph = MplCanvas(self,width=5,height=4,dpi=100)
            self.graph.axes.plot(years,grades)
            self.graph.axes.set_ylim([0,100])
            self.layout.addWidget(self.graph,1,4)

    def clearYears(self):
        # Code to clear all courses from screen, called before calling displayCourses so as to not overlap
        row = 1
        count = 0

        widgetItem = self.layout.itemAtPosition(row,count) 
        
        while widgetItem is not None:
            widget = widgetItem.widget()
            self.layout.removeWidget(widget)
            print(count)
            count += 1
            if(count == 4):
                count = 0
                row += 1
            widgetItem = self.layout.itemAtPosition(row,count)
        
        if (not self.first):
            self.layout.removeWidget(self.graph)
            self.graph.hide()
            self.graph.deleteLater()
            self.graph = None
        self.layout.update()

    def handle_year_click(self,year):
        #Code to set current widget to the modules screen of the passed in year
        self.main_window.itemClicked.emit(year)
        print(year)
    
    def getType(self):
        return self.type

        

class ModulesScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.type = "Module"
        self.first = True

        titleL = QLabel('Modules')
        self.layout.addWidget(titleL,0,0,1,4,alignment=Qt.AlignmentFlag.AlignCenter)
    
    def displayModules(self,titles,credits,grades):
        if (self.first):
            self.first = False
        # Code to display all modules for the year
        count = 0
        row = 1
        buttons = []

        for module in range(len(titles)):
            tempCredits = QLabel("Credits: "+credits[module])
            tempGrade = QLabel("Grades: "+grades[module])
            tempB = QPushButton(titles[module])
            tempB.clicked.connect(lambda checked,module=titles[module]: self.handle_module_click(module))
            buttons.append(tempB)
            tempL = QVBoxLayout()
            tempC = QWidget()
            tempC.setLayout(tempL)
            tempL.addWidget(tempB)
            tempL.addWidget(tempCredits)
            tempL.addWidget(tempGrade)
            if (count == 4):
                count = 0
                row += 1    
            self.layout.addWidget(tempC,row,count)
            count += 1

    def displayGraph(self,modules,grades):
        # Code to display the graph of progress for the year
        if(len(modules)>1):
            self.graph = MplCanvas(self,width=5,height=4,dpi=100)
            self.graph.axes.plot(modules,grades)
            self.graph.axes.set_ylim([0,100])
            self.layout.addWidget(self.graph,1,5)

    def clearModules(self):
        # Code to clear all courses from screen, called before calling displayCourses so as to not overlap
        row = 1
        count = 0

        widgetItem = self.layout.itemAtPosition(row,count) 
        
        while widgetItem is not None:
            widget = widgetItem.widget()
            self.layout.removeWidget(widget)
            print(count)
            count += 1
            if(count == 4):
                count = 0
                row += 1
            widgetItem = self.layout.itemAtPosition(row,count)

        if (not self.first):
            self.layout.removeWidget(self.graph)
            self.graph.hide()
            self.graph.deleteLater()
            self.graph = None
        self.layout.update()
    
    def handle_module_click(self,module):
        #Code to set current widget to the years screen of the passed in course
        self.main_window.itemClicked.emit(module)
        print(module)
    
    def getType(self):
        return self.type

class AssessmentScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.type = "Assessment"
        self.first = True

        titleL = QLabel('Assessments')
        self.layout.addWidget(titleL,0,0,1,4,alignment=Qt.AlignmentFlag.AlignCenter)
    
    def displayAssessments(self,titles,weights,grades):
        if (self.first):
            self.first = False
        # Code to display all assessments for the module
        count = 0
        row = 1
        buttons = []
        for assess in range(len(titles)):
            tempWeight = QLabel("Weight: "+weights[assess])
            tempGrade = QLabel("Grade: "+grades[assess])
            tempB = QPushButton(titles[assess])
            tempB.clicked.connect(lambda checked,assess=titles[assess]: self.handle_assessment_click(assess))
            buttons.append(tempB)
            tempL = QVBoxLayout()
            tempC = QWidget()
            tempC.setLayout(tempL)
            tempL.addWidget(tempB)
            tempL.addWidget(tempWeight)
            tempL.addWidget(tempGrade)
            if (count == 4):
                count = 0
                row += 1    
            self.layout.addWidget(tempC,row,count)
            count += 1

    def displayGraph(self,assessments,grades):
        # Code to display the graph of progress for the module
        if(len(assessments) > 1):
            self.graph = MplCanvas(self,width=5,height=4,dpi=100)
            self.graph.axes.plot(assessments,grades)
            self.graph.axes.set_ylim([0,100])
            self.layout.addWidget(self.graph,1,5)

    def clearAssessments(self):
        # Code to clear all courses from screen, called before calling displayCourses so as to not overlap
        row = 1
        count = 0

        widgetItem = self.layout.itemAtPosition(row,count) 
        
        while widgetItem is not None:
            widget = widgetItem.widget()
            self.layout.removeWidget(widget)
            print(count)
            count += 1
            if(count == 4):
                count = 0
                row += 1
            widgetItem = self.layout.itemAtPosition(row,count)
        
        if (not self.first):
            self.layout.removeWidget(self.graph)
            self.graph.hide()
            self.graph.deleteLater()
            self.graph = None
        self.layout.update()
    
    def handle_assessment_click(self,assessment):
        #Code to set current widget to the years screen of the passed in course
        self.main_window.itemClicked.emit(assessment)
        print(assessment)
    
    def getType(self):
        return self.type

class AssignmentsScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.type = "Assignment"
        self.first = True

        titleL = QLabel('Assignments')
        self.layout.addWidget(titleL,0,0,1,4,alignment=Qt.AlignmentFlag.AlignCenter)
    
    def displayAssignments(self,titles,weights,grades):
        if (self.first):
            self.first = False
        # Code to display all assignments for the coursework
        count = 0
        row = 1
        for year in range(len(titles)):
            tempTitle = QLabel(titles[year])
            tempWeight = QLabel("Weight: "+weights[year])
            tempGrade = QLabel("Grade: "+grades[year])
            tempL = QVBoxLayout()
            tempC = QWidget()
            tempC.setLayout(tempL)
            tempL.addWidget(tempTitle)
            tempL.addWidget(tempWeight)
            tempL.addWidget(tempGrade)
            if (count == 4):
                count = 0
                row += 1    
            self.layout.addWidget(tempC,row,count)
            count += 1

    def displayGraph(self,assignments,grades):
        # Code to display the graph of progress for the coursework
        if (len(assignments) > 1):
            self.graph = MplCanvas(self,width=5,height=4,dpi=100)
            self.graph.axes.plot(assignments,grades)
            self.graph.axes.set_ylim([0,100])
            self.layout.addWidget(self.graph,1,5)
    
    def clearAssignments(self):
        # Code to clear all courses from screen, called before calling displayCourses so as to not overlap
        row = 1
        count = 0

        widgetItem = self.layout.itemAtPosition(row,count) 
        
        while widgetItem is not None:
            widget = widgetItem.widget()
            self.layout.removeWidget(widget)
            print(count)
            count += 1
            if(count == 4):
                count = 0
                row += 1
            widgetItem = self.layout.itemAtPosition(row,count)
        
        if (not self.first):
            self.layout.removeWidget(self.graph)
            self.graph.hide()
            self.graph.deleteLater()
            self.graph = None
        self.layout.update()
    
    def getType(self):
        return self.type
    
        


