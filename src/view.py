from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pathlib import Path
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import sys

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = plt.Figure(figsize=(width,height), dpi = dpi)
        super(MplCanvas, self).__init__(fig)
        self.axes = fig.add_subplot(111)
        self.axes.axhline(y=40.0, color='r', linestyle='-')
        self.axes.axhline(y=50.0, color='orange', linestyle='-')
        self.axes.axhline(y=60.0, color='green', linestyle='-')
        self.axes.axhline(y=60.0, color='darkgreen', linestyle='-')
        self.draw()

         

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("University Progress Tracker")
        self.setWindowIcon(QIcon('./assets/mainP.jpg'))
        self.setGeometry(100,100,1000,800)
        self.stack = QStackedWidget()
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


        #======================================
        # TEST FOR DISPLAYING COURSES
        #print("TEST DISPLAY")
        #self.courses_screen.displayCourses(["Physics","Maths","CS","English","Physc"],['45.0','77.0','65.3','15.0','34.2'])

        # TEST FOR CLEARING COURSES
        #print("TEST CLEAR")
        #self.courses_screen.clearCourses()
        #======================================
        #TEST FOR DISPLAYING YEARS
        print("TEST DISPLAY")
        self.years_screen.displayYears(['Year 1','Year 2','Year 3'],['0','40','60'],['70','85.6','78.1'])

        #TEST FOR DISPLAYING GRAPH
        print("TEST GRAPH")
        #(0*70)+(85.6*0.4)=34.24 +(78.1*0.6)= 81.1
        self.years_screen.displayGraph([0,34.24,81.1],['Year 1','Year 2','Year 3'])
         
        self.stack.setCurrentWidget(self.years_screen)
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("ProgressManager v1.0")

        self.show()


class LoginScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()
        self.setLayout(layout)
 
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

    
    def checkCred(self):
        un = self.user.text()
        pw = self.passw.text()
        print(un,pw)
        pass

class CoursesScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        titleL = QLabel('Courses')
        self.layout.addWidget(titleL,0,0,1,4,alignment=Qt.AlignmentFlag.AlignCenter)
         

    def displayCourses(self,titles,grades):
        count = 0
        row = 1
         
        for course in range(len(titles)):
            tempTitle = QLabel(titles[course])
            tempGrade = QLabel(grades[course])
            tempL = QVBoxLayout()
            tempC = QWidget()
            tempC.setLayout(tempL)
            tempL.addWidget(tempTitle)
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
             
            
class YearsScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        titleL = QLabel('Years')
        self.layout.addWidget(titleL,0,0,1,4,alignment=Qt.AlignmentFlag.AlignCenter)
    
    def displayYears(self,titles,weights,grades):
        count = 0
        row = 1
        # Code to display all years for the course
        for year in range(len(titles)):
            tempTitle = QLabel(titles[year])
            tempWeight = QLabel(weights[year])
            tempGrade = QLabel(grades[year])
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
            count +=1

    def displayGraph(self,grades,years):
        # Code to display the graph of progress for the course
        # For all graphs, the grades array is the cumulative value of the grades as modules increase
        g = MplCanvas(self,width=5,height=4,dpi=100)
        g.axes.plot(years,grades)
        self.layout.addWidget(g,1,5)

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

        

class ModulesScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        titleL = QLabel('Modules')
        self.layout.addWidget(titleL,0,0,1,4,alignment=Qt.AlignmentFlag.AlignCenter)
    
    def displayModules(self,titles,credits,grades):
        # Code to display all modules for the year
        count = 0
        row = 1
        for module in range(len(titles)):
            tempTitle = QLabel(titles[module])
            tempCredits = QLabel(credits[module])
            tempGrade = QLabel(grades[module])
            tempL = QVBoxLayout()
            tempC = QWidget()
            tempC.setLayout(tempL)
            tempL.addWidget(tempTitle)
            tempL.addWidget(tempCredits)
            tempL.addWidget(tempGrade)
            if (count == 4):
                count = 0
                row += 1    
            self.layout.addWidget(tempC,row,count)
            count += 1

    def displayGraph(self,grades,modules):
        # Code to display the graph of progress for the year
        g = MplCanvas(self,width=5,height=4,dpi=100)
        g.axes.plot(modules,grades)
        self.layout.addWidget(g,1,5)

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

class AssessmentScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        titleL = QLabel('Assessments')
        self.layout.addWidget(titleL,0,0,1,4,alignment=Qt.AlignmentFlag.AlignCenter)
    
    def displayAssessments(self,titles,weights,grades):
        # Code to display all assessments for the module
        count = 0
        row = 1
        for assess in range(len(titles)):
            tempTitle = QLabel(titles[assess])
            tempWeight = QLabel(weights[assess])
            tempGrade = QLabel(grades[assess])
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

    def displayGraph(self,grades,assessments):
        # Code to display the graph of progress for the module
        g = MplCanvas(self,width=5,height=4,dpi=100)
        g.axes.plot(assessments,grades)
        self.layout.addWidget(g,1,5)

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

class AssignmentsScreen(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        titleL = QLabel('Assignments')
        self.layout.addWidget(titleL,0,0,1,4,alignment=Qt.AlignmentFlag.AlignCenter)
    
    def displayAssignments(self,titles,weights,grades):
        # Code to display all assignments for the coursework
        count = 0
        row = 1
        for year in range(len(titles)):
            tempTitle = QLabel(titles[year])
            tempWeight = QLabel(weights[year])
            tempGrade = QLabel(grades[year])
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

    def displayGraph(self,grades,assignments):
        # Code to display the graph of progress for the coursework
        g = MplCanvas(self,width=5,height=4,dpi=100)
        g.axes.plot(assignments,grades)
        self.layout.addWidget(g,1,5)
    
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
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
