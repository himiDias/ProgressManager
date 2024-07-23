
from getpass import getpass 
import mysql.connector
from mysql.connector import connect,Error


try:
    with connect(
        host="localhost",
        user = input("Enter Username: "),
        password = getpass("Enter Password: "),

    ) as connection:
        create_db_query = "CREATE DATABASE IF NOT EXISTS `university-progress`"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            print("Database created/exists, login success")
except Error as e:
    print(e)




def initialise_db(con):
    create_course_table = """
    CREATE TABLE IF NOT EXISTS courses(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    grade FLOAT
    )
    """
    create_years_table = """
    CREATE TABLE IF NOT EXISTS years(
    year INT AUTO_INCREMENT PRIMARY KEY,
    grade FLOAT,
    course_id INT,
    FOREIGN KEY(course_id) REFERENCES courses(id)
    )
    """
    create_module_table = """
    CREATE TABLE IF NOT EXISTS modules(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    grade FLOAT,
    year INT,
    FOREIGN KEY(year) REFERENCES years(year)
    )
    """

    create_cw_table = """
    CREATE TABLE IF NOT EXISTS coursework(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    weight INT,
    grade FLOAT,
    module_id INT,
    FOREIGN KEY(module_id) REFERENCES modules(id) 
    )
    """

    create_exam_table = """
    CREATE TABLE IF NOT EXISTS exam(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    weight INT,
    grade FLOAT,
    module_id INT,
    FOREIGN KEY(module_id) REFERENCES modules(id)
    )"""

    create_assignments_table = """
    CREATE TABLE IF NOT EXISTS assignments(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    weight INT,
    grade FLOAT,
    coursework_id INT,
    FOREIGN KEY(coursework_id) REFERENCES coursework(id)
    )
    """


    try:
        with con.cursor() as cursor:
            cursor.execute(create_course_table)
            cursor.execute(create_years_table)
            cursor.execute(create_module_table)
            cursor.execute(create_cw_table)
            cursor.execute(create_exam_table)
            cursor.execute(create_assignments_table)

            con.commit()
            print("Successfully initialised database")
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
        print("Successfully connected to database")
        initialise_db(connection)
except Error as e:
    print(e)

class Course:
    def __init__(self,id,title):
        self.id = id
        self.title = title
        self.grade = 0


    def update_grade(self,grade):
        self.grade = grade

    def update_title(self,ntitle):
        self.title = ntitle

    def get_grade(self):
        return self.grade
    
    def get_title(self):
        return self.title


class Year:
    def __init__(self,id,title):
        self.id = id
        self.title = title
        self.grade = 0

    def update_grade(self,grade):
        self.grade = grade
    
    def update_title(self,ntitle):
        self.title = ntitle

    def get_grade(self):
        return self.grade
    
    def get_title(self):
        return self.title

class Module:
    def __init__(self,id,title,credits):
        self.id= id
        self.title = title
        self.credits = credits
        self.grade = 0

    def update_title(self,ntitle):
        self.title = ntitle

    def update_credits(self,nCredits):
        self.credits = nCredits

    def update_grade(self,grade):
        self.grade= grade
    
    def get_title(self):
        return self.title
    
    def get_credits(self):
        return self.credits
    
    def get_grade(self):
        return self.grade

class Coursework:
    def __init__(self,weight):
        self.title = "Coursework"
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
    
    def get_title(self):
        return self.title

class Exam:
    def __init__(self,weight):
        self.title = "Exam"
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
    
    def get_title(self):
        return self.title
    

class Assignment:
    def __init__(self,id,title,weight):
        self.id = id
        self.title = title
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
    
    def get_title(self):
        return self.title
    


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
    


    