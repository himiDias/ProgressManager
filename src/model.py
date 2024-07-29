
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



def db_set(statement):
    try:
        with connect(
            host="localhost",
            user = username,
            password = Password,
            database="university-progress",
        ) as connection:
            print(connection)
            print("Successfully connected to database")
            try:
                with connection.cursor() as cursor:
                    cursor.execute(statement)
                    connection.commit()
                    print("Successfully adjusted database")
            except Error as e:
                print(e)
    except Error as e:
        print(e)

def db_get(statement):
    try:
        with connect(
            host = "localhost",
            user= username,
            password = Password,
            database="university-progress",
        ) as connection:
            print(connection)
            print("Successfully connected to database")
            try:
                with connection.cursor() as cursor:
                    cursor.execute(statement)
                    records = cursor.fetchall()
                    return records
            except Error as e:
                print(e)
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
    id INT AUTO_INCREMENT PRIMARY KEY,
    year VARCHAR(100),
    grade FLOAT,
    course_id INT,
    FOREIGN KEY(course_id) REFERENCES courses(id)
    )
    """
    create_module_table = """
    CREATE TABLE IF NOT EXISTS modules(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    credits INT,
    grade FLOAT,
    year_id INT,
    FOREIGN KEY(year_id) REFERENCES years(id)
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

username = input("Enter Username: ")
Password = getpass("Enter Password: ")
try:
    with connect(
        host="localhost",
        user = username,
        password = Password,
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
    
    def __repr__(self):
        return f"Course(id={self.id}, title={self.title}, grade={self.grade})"


class Year:
    def __init__(self,id,title,grd,cid):
        self.id = id
        self.title = title
        self.grade = grd
        self.courseid = cid

    def update_grade(self,grade):
        self.grade = grade
    
    def update_title(self,ntitle):
        self.title = ntitle

    def get_grade(self):
        return self.grade
    
    def get_title(self):
        return self.title
    
    def get_cid(self):
        return self.courseid
    
    def __repr__(self):
        return f"Year(id={self.id}, title={self.title}, grade={self.grade}, courseid={self.courseid})"

class Module:
    def __init__(self,id,title,credits,grd,yid):
        self.id= id
        self.title = title
        self.credits = credits
        self.grade = grd
        self.yearid = yid

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
    
    def get_yid(self):
        return self.yearid
    
    def __repr__(self):
        return f"Module(id={self.id}, title={self.title}, credits={self.credits}, grade={self.grade}, yearid={self.yearid})"

class Coursework:
    def __init__(self,weight,grd,mid):
        self.title = "Coursework"
        self.weight = weight
        self.grade = grd
        self.moduleid = mid

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
    
    def get_mid(self):
        return self.moduleid
    
    def __repr__(self):
        return f"Coursework(title={self.title}, weight={self.weight}, grade={self.grade}, moduleid={self.moduleid})"

class Exam:
    def __init__(self,weight,grd,mid):
        self.title = "Exam"
        self.weight = weight
        self.grade = grd
        self.moduleid = mid


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
    
    def get_mid(self):
        return self.moduleid
    
    def __repr__(self):
        return f"Exam(title={self.title}, weight={self.weight}, grade={self.grade}, moduleid={self.moduleid})"
    

class Assignment:
    def __init__(self,id,title,weight,grd,cid):
        self.id = id
        self.title = title
        self.weight = weight
        self.grade = grd
        self.courseworkid = cid

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
    
    def get_cid(self):
        return self.courseworkid
    
    def __repr__(self):
        return f"Assignment(id={self.id}, title={self.title}, weight={self.weight}, grade={self.grade}, courseworkid={self.cid})"
    


class courseModel:
    def __init__(self):
        self.courses = []

    def add_course(self,course):
        print(course.title)
        s = f"INSERT INTO courses (title,grade) VALUES ('{course.title}',{course.grade})"
        db_set(s)
        self.courses.append(course)
    
    def rem_course(self,title,id):
        s = f"DELETE FROM courses WHERE title = '{title}'"
        db_set(s)
        del self.courses[id]

    def get_courses(self):
        return self.courses

  

class yearModel:
    def __init__(self,cid):
        self.years=[]
        s = f"SELECT * FROM years WHERE course_id = {cid}"
        recs = db_get(s)
        i = 0 
        for record in recs:
            
            self.years.append(Year(i,record[1],record[2],record[3]))
            i += 1

    def add_year(self,year):
        s = f"INSERT INTO years (year,grade,course_id) VALUES ('{year.title}',{year.grade},{year.courseid})"
        db_set(s)
        self.years.append(year)

    def rem_year(self,year,cid,id):
        s = f"DELETE FROM years WHERE year = '{year}' AND course_id = {cid}"
        db_set(s)
        del self.years[id]

    def get_years(self):
        return self.years
    

class moduleModel:
    def __init__(self,yid):
        self.modules = []

        s = f"SELECT * FROM modules WHERE year_id = {yid}"
        recs = db_get(s)
        i = 0 
        for record in recs:
            
            self.modules.append(Module(i,record[1],record[2],record[3],record[4]))
            i += 1

    def add_module(self,module):
        s = f"INSERT INTO modules (title,credits,grade,year_id) VALUES ('{module.title}',{module.credits},{module.grade},{module.yearid})"
        db_set(s)
        self.modules.append(module)
    
    def rem_module(self,title,yid,id):
        s = f"DELETE FROM modules WHERE title = '{title}' AND year_id = {yid}"
        del self.modules[id]
    
    def get_modules(self):
        return self.modules
    

class assessmentModel:
    def __init__(self,mid):
        self.assessments = []

        s = f"SELECT * FROM coursework WHERE module_id = {mid}"
        s1 = f"SELECT * FROM exam WHERE module_id = {mid}"
        recs_c = db_get(s)
        recs_e = db_get(s1)

        for record in recs_c:
            self.assessments.append(Coursework(record[1],record[2],record[3],record[4]))
        for record in recs_e:
            self.assessments.append(Exam(record[1],record[2],record[3],record[4]))
    
    def add_cw(self,cw):
        s = f"INSERT INTO coursework (title,weight,grade,module_id) VALUES ('{cw.title}',{cw.weight},{cw.grade},{cw.moduleid})"
        db_set(s)
        self.assessments.append(cw)
    
    def add_e(self,e):
        s = f"INSERT INTO exam (title,weight,grade,module_id) VALUES ('{e.title}',{e.weight},{e.grade},{e.moduleid})"
        db_set(s)
        self.assessments.append(e)

    def get_assessments(self):
        return self.assessments
    
    def rem_assessment(self,id):
        a = self.assessments[id]
        if(a) == Coursework:
            s = f"DELETE FROM coursework WHERE module_id = {a.moduleid}" 
            db_set(s)
        else:
            s = f"DELETE FROM exam WHERE module_id = {a.moduleid}"
            db_set(s)

        del self.assessments[id]
    
    def get_length(self):
        return len(self.assessments)
    
class assignmentModel:
    def __init__(self,cid):
        self.assignments = []

        s = f"SELECT * FROM assignments WHERE coursework_id = {cid}"
        recs = db_get(s)
        i = 0 
        for record in recs:
            
            self.modules.append(Assignment(i,record[1],record[2],record[3],record[4]))
            i += 1

    def add_assignment(self,assignment):
        s = f"INSERT INTO assignments (title,weight,grade,coursework_id) VALUES ('{assignment.title}',{assignment.weight},{assignment.grade},{assignment.courseworkid})"
        db_set(s)
        self.assignments.append(assignment)

    def rem_assigments(self,id):
        a = self.assignments[id]
        s = f"DELETE FROM assignments WHERE title = '{a.title}' AND coursework_id = {a.courseworkid}"
        db_set(s)
        del self.assignments[id]

    def get_assignments(self):
        return self.assignments
    


def test_model():
    # TEST 1: Initialises a main courses model and a years model for 1 course 
    coursesM = courseModel()
    physicsYearsM= yearModel(1)

    # TEST 2 : Add two courses
    coursesM.add_course(Course(0,"Physics"))
    coursesM.add_course(Course(1,"Maths"))

    # TEST 3 : Add 4 years to PhysicsYearsModel

    physicsYearsM.add_year(Year(0,"Year 1",0,1))
    physicsYearsM.add_year(Year(1,"Year 2",0,1))
    physicsYearsM.add_year(Year(2,"Year 3",0,1))
    physicsYearsM.add_year(Year(3,"Year 4",0,1))

    #TEST 4 : Delete a course
    coursesM.rem_course("Maths",1)

    #TEST 5 : Delete year 4 of Physics
    physicsYearsM.rem_year("Year 4",1,3)

    #TEST 6 : Add 2 Modules to first year physics
    pY1M = moduleModel(1)

    pY1M.add_module(Module(0,"Introduction to Physics",10,0,1))
    pY1M.add_module(Module(1,"Kinematics in Mechanics",20,0,1))

    #TEST 7 : Add and exam and coursework section to module 2 of physics year 1
    py1m2M = assessmentModel(2)

    py1m2M.add_cw(Coursework(70,0,2))
    py1m2M.add_e(Exam(30,0,2))

    #TEST 8 : Add 3 assignments to the coursework section of module 2 of physics year 1
    py1m2cM = assignmentModel(1)

    py1m2cM.add_assignment(Assignment(0,"CW1",10,0,1))
    py1m2cM.add_assignment(Assignment(1,"CW2",40,0,1))
    py1m2cM.add_assignment(Assignment(2,"CW2",50,0,1))
 


test_model()
#coursesM = courseModel()
#physicsYearsM = yearModel(1)

#print(coursesM.courses)
#print(physicsYearsM.years)