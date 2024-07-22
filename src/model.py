
from getpass import getpass 
from mysql.connector import connect,Error


try:
    with connect(
        host="localhost",
        user = input("Enter Username: "),
        password = getpass("Enter Password: "),

    ) as connection:
        create_db_query = "CREATE DATABASE IF NOT EXISTS university-progress"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            print("Database created/exists, login success")
except Error as e:
    print(e)


try:
    with connect(
        host="localhost",
        user = input("Enter Username: "),
        password = getpass("Enter password: "),
        database="university-progress",
    ) as connection:
        print(connection)
except Error as e:
    print(e)



cursor = connection.cursor()

class Course:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.grade = 0


    def update_grade(self,grade):
        self.grade = grade

    def update_name(self,nName):
        self.name = nName

    def get_grade(self):
        return self.grade
    
    def get_name(self):
        return self.name


class Year:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.grade = 0

    def update_grade(self,grade):
        self.grade = grade
    
    def update_name(self,nName):
        self.name = nName

    def get_grade(self):
        return self.grade
    
    def get_name(self):
        return self.name

class Module:
    def __init__(self,id,name,credits):
        self.id= id
        self.name = name
        self.credits = credits
        self.grade = 0

    def update_name(self,nName):
        self.name = nName

    def update_credits(self,nCredits):
        self.credits = nCredits

    def update_grade(self,grade):
        self.grade= grade
    
    def get_name(self):
        return self.name
    
    def get_credits(self):
        return self.credits
    
    def get_grade(self):
        return self.grade

class Coursework:
    def __init__(self,weight):
        self.name = "Coursework"
        self.weight = weight
        self.grade = 0

    def update_weight(self,nWeight):
        self.weight = nWeight
    
    def update_grade(self,grade):
        self.grade = grade
    
    def get_weight(self):
        return self.weight
    
    def get_grade(self):
        return self.grade
    
    def get_name(self):
        return self.name

class Exam:
    def __init__(self,weight):
        self.name = "Exam"
        self.weight = weight
        self.grade = 0


    def update_weight(self,nWeight):
        self.weight = nWeight
    
    def update_grade(self,grade):
        self.grade = grade
    
    def get_weight(self):
        return self.weight
    
    def get_grade(self):
        return self.grade
    
    def get_name(self):
        return self.name
    

class Assignment:
    def __init__(self,id,name,weight):
        self.id = id
        self.name = name
        self.weight = weight
        self.grade = 0

    def update_weight(self,nWeight):
        self.weight = nWeight
    
    def update_grade(self,grade):
        self.grade = grade
    
    def get_weight(self):
        return self.weight
    
    def get_grade(self):
        return self.grade
    
    def get_name(self):
        return self.name
    


class courseModel:
    def __init__(self):
        self.courses = []

    def add_course(self,course):
        self.courses.append(course)
    
    def rem_course(self,id):
        del self.courses[id]

    def get_courses(self):
        return self.courses

  

class yearModel:
    def __init__(self):
        self.years = []

    
    def add_year(self,year):
        self.years.append(year)

    def rem_year(self,id):
        del self.years[id]

    def get_years(self):
        return self.years
    

class moduleModel:
    def __init__(self):
        self.modules = []

    def add_module(self,module):
        self.modules.append(module)
    
    def rem_module(self,id):
        del self.modules[id]
    
    def get_modules(self):
        return self.modules
    

class assessmentModel:
    def __init__(self):
        self.assessments = []
    
    def add_cw(self,cw):
        self.assessments.append(cw)
    
    def add_e(self,e):
        self.assessments.append(e)

    def get_assessments(self):
        return self.assessments
    
    def rem_assessment(self,id):
        del self.assessments[id]
    
    def get_length(self):
        return len(self.assessments)
    
class assignmentModel:
    def __init__(self):
        self.assignments = []

    def add_assignment(self,assignment):
        self.assignments.append(assignment)

    def rem_assigments(self,id):
        del self.assignments[id]

    def get_assignments(self):
        return self.assignments
    


    