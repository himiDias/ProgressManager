
from getpass import getpass 
import mysql.connector
from mysql.connector import connect,Error

username = None
Password = None

#Initial database connection to create an empty database for user
def initialise_user(user,passw):
    global username, Password
    username = user
    Password = passw
    try:
        with connect(
            host="localhost",
            user = username,
            password = Password,

        ) as connection:
            create_db_query = "CREATE DATABASE IF NOT EXISTS `university-progress`"
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
                print("Database created/exists, login success")
    except Error:
        return "Error"



# function to change values in database, takes a sql query
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

# function to get values in database, takes sql query
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

# Function to initialise the database upon creation, creates necessary tables
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
    weight INT,
    grade FLOAT,
    course_id INT,
    FOREIGN KEY(course_id) REFERENCES courses(id) ON DELETE CASCADE
    )
    """
    create_module_table = """
    CREATE TABLE IF NOT EXISTS modules(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    credits INT,
    grade FLOAT,
    year_id INT,
    FOREIGN KEY(year_id) REFERENCES years(id) ON DELETE CASCADE
    )
    """

    create_cw_table = """
    CREATE TABLE IF NOT EXISTS coursework(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    weight INT,
    grade FLOAT,
    module_id INT,
    FOREIGN KEY(module_id) REFERENCES modules(id) ON DELETE CASCADE
    )
    """

    create_exam_table = """
    CREATE TABLE IF NOT EXISTS exam(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    weight INT,
    grade FLOAT,
    module_id INT,
    FOREIGN KEY(module_id) REFERENCES modules(id) ON DELETE CASCADE
    )"""

    create_assignments_table = """
    CREATE TABLE IF NOT EXISTS assignments(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    weight INT,
    grade FLOAT,
    coursework_id INT,
    FOREIGN KEY(coursework_id) REFERENCES coursework(id) ON DELETE CASCADE
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

def setup_db():
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
    except Error:
        return "Error"

# Classes for each part
class Course:
    def __init__(self,id,title,grd):
        self.id = id
        self.title = title
        self.grade = grd


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
    def __init__(self,id,title,weight,grd,cid):
        self.id = id
        self.title = title
        self.weight = weight
        self.grade = grd
        self.courseid = cid

    ### NOT.E UPDATE METHODS ARE PROBABLY REDUDANT GIVEN THE EDIT FUNCTIONS IN THE INDIVIDUAL MODELS
    ### REMOVE LATER FOR ALL
    def update_grade(self,grade):
        self.grade = grade
    
    def update_title(self,ntitle):
        self.title = ntitle

    def get_weight(self):
        return self.weight
    
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
    

# Models for each part, each model stores an array of its part for a specific parent of that part. E.g if there are two courses, there will be two yearModels for the years from course 1 and course 2
## NOTE appending to self.courses adn removing from self.courses is bit redundant as the load_data does this already
### COULD remove these and just re-load data each time there is a change at runtime, but i guess that would decrease
### performance as most of the data is would have not changed, DECIDE LATER PROBABLY DON'T
class courseModel:
    def __init__(self):
        self.courses = []
        s = f"SELECT * FROM courses"
        recs = db_get(s)

        i=0
        for record in recs:
            self.courses.append(Course(i,record[1],record[2]))
            i += 1

    def add_course(self,course):
        print(course.title)
        s = f"INSERT INTO courses (title,grade) VALUES ('{course.title}',{course.grade})"
        db_set(s)
        self.courses.append(course)
    
    def rem_course(self,id):
        c= self.courses[id]
        s = f"DELETE FROM courses WHERE title = '{c.title}'"
        db_set(s)
        del self.courses[id]

    def get_courses(self):
        return self.courses
    
    def edit_course(self,course,d_id):
        s=f"UPDATE courses SET title = '{course.title}', grade = {course.grade} WHERE id = {d_id}"
        db_set(s)
        self.courses[course.id] = course


  

class yearModel:
    def __init__(self,cid):
        self.years=[]
        self.courseId = cid
        s = f"SELECT * FROM years WHERE course_id = {cid}"
        recs = db_get(s)
        i = 0 
        for record in recs:
            ### NOT.E some params redundant also given the self.courseid attribute, instead of passing in record[4] which is same as cid
            ## FIX LATER FOR ALL
            self.years.append(Year(i,record[1],record[2],record[3],record[4]))
            i += 1

    def add_year(self,year):
        s = f"INSERT INTO years (year,weight,grade,course_id) VALUES ('{year.title}',{year.weight},{year.grade},{year.courseid})"
        db_set(s)
        self.years.append(year)

    def rem_year(self,id):
        y = self.years[id]
        s = f"DELETE FROM years WHERE year = '{y.title}' AND course_id = {self.courseId}"
        db_set(s)
        del self.years[id]

    def get_years(self):
        return self.years
    
    def edit_year(self,year,d_id):
        s=f"UPDATE years SET year = '{year.title}',weight = {year.weight}, grade = {year.grade}, course_id = {year.courseid} WHERE id = {d_id}"
        db_set(s)
        self.years[year.id] = year
    

class moduleModel:
    def __init__(self,yid):
        self.modules = []
        self.yearId = yid

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
    
    def rem_module(self,id):
        m = self.modules[id]
        s = f"DELETE FROM modules WHERE title = '{m.title}' AND year_id = {self.yearId}"
        db_set(s)
        del self.modules[id]
    
    def get_modules(self):
        return self.modules
    
    def edit_module(self,module,d_id):
        s=f"UPDATE modules SET title = '{module.title}', credits = {module.credits}, grade = {module.grade}, year_id = {module.yearid} WHERE id = {d_id}"
        db_set(s)
        self.modules[module.id] = module

class assessmentModel:
    def __init__(self,mid):
        self.assessments = []
        self.moduleId = mid

        s = f"SELECT * FROM coursework WHERE module_id = {mid}"
        s1 = f"SELECT * FROM exam WHERE module_id = {mid}"
        recs_c = db_get(s)
        recs_e = db_get(s1)

        for record in recs_c:
            self.assessments.append(Coursework(record[2],record[3],record[4]))
        for record in recs_e:
            self.assessments.append(Exam(record[2],record[3],record[4]))
    
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
        if isinstance(a,Coursework):
            s = f"DELETE FROM coursework WHERE module_id = {a.moduleid}" 
            db_set(s)
        else:
            s = f"DELETE FROM exam WHERE module_id = {a.moduleid}"
            db_set(s)

        del self.assessments[id]
    
    def edit_cw(self,coursework,d_id):
        s=f"UPDATE coursework SET weight = '{coursework.weight}', grade = {coursework.grade}, module_id = {coursework.moduleid} WHERE id = {d_id}"
        db_set(s)
        
    def edit_e(self,exam,d_id):
        s=f"UPDATE exam SET weight = '{exam.weight}', grade = {exam.grade}, module_id = {exam.moduleid} WHERE id = {d_id}"
        db_set(s)
    
class assignmentModel:
    def __init__(self,cid):
        self.assignments = []
        self.courseworkId = cid

        s = f"SELECT * FROM assignments WHERE coursework_id = {cid}"
        recs = db_get(s)
        i = 0 
        for record in recs:
            
            self.assignments.append(Assignment(i,record[1],record[2],record[3],record[4]))
            i += 1

    def add_assignment(self,assignment):
        s = f"INSERT INTO assignments (title,weight,grade,coursework_id) VALUES ('{assignment.title}',{assignment.weight},{assignment.grade},{assignment.courseworkid})"
        db_set(s)
        self.assignments.append(assignment)

    def rem_assignment(self,id):
        a = self.assignments[id]
        s = f"DELETE FROM assignments WHERE title = '{a.title}' AND coursework_id = {a.courseworkid}"
        db_set(s)
        del self.assignments[id]

    def get_assignments(self):
        return self.assignments
    
    def edit_assignment(self,assignment,d_id):
        s=f"UPDATE assignments SET title = '{assignment.title}', weight = {assignment.weight}, grade = {assignment.grade}, coursework_id = {assignment.courseworkid} WHERE id = {d_id}"
        db_set(s)
        self.assignments[assignment.id] = assignment
    
# Loads saved data during startup and updates    

def load_data(yearModels,moduleModels,assessmentModels,assignmentModels):
    #yearModels = []
    courseIds = []
    #moduleModels = []
    yearIds = []
    #assessmentModels = []
    moduleIds = []
    #assignmentModels = []
    cwIds = []

    recYears = db_get("SELECT * FROM years")
    recModules = db_get("SELECT * FROM modules")
    recExam = db_get("SELECT * FROM exam")
    recAssignments = db_get("SELECT * FROM assignments")

    for record in recYears:
        if record[-1] not in courseIds:
            courseIds.append(record[-1])
            yearModels.append(yearModel(record[-1]))
    for record in recModules:
        if record[-1] not in yearIds:
            yearIds.append(record[-1])
            moduleModels.append(moduleModel(record[-1]))
    for record in recExam:
        if record[-1] not in moduleIds:
            moduleIds.append(record[-1])
            assessmentModels.append(assessmentModel(record[-1]))
    for record in recAssignments:
        if record[-1] not in cwIds:
            cwIds.append(record[-1])
            assignmentModels.append(assignmentModel(record[-1]))

    for item in moduleModels:
        print(item.modules)
    



# TESTING FOR MODEL
def test_model():
    # TEST 1: Initialises a main courses model and a years model for 2 course 
    coursesM = courseModel()
    physicsYearsM= yearModel(1)
    mathsYearsM = yearModel(2)

    # TEST 2 : Add two courses
    coursesM.add_course(Course(0,"Physics",0))
    coursesM.add_course(Course(1,"Maths",0))

    # TEST 3 : Add 4 years to PhysicsYearsModel

    physicsYearsM.add_year(Year(0,"Year 1",0,0,1))
    physicsYearsM.add_year(Year(1,"Year 2",10,0,1))
    physicsYearsM.add_year(Year(2,"Year 3",30,0,1))
    physicsYearsM.add_year(Year(3,"Year 4",60,0,1))

    # TEST 4 : Add 3 years to MathsYearsModel

    mathsYearsM.add_year(Year(0,"Year 1",0,0,2))
    mathsYearsM.add_year(Year(1,"Year 2",40,0,2))
    mathsYearsM.add_year(Year(2,"Year 3",60,0,2))

    # TEST 5 : Add 2 Modules to first year physics
    pY1M = moduleModel(1)

    pY1M.add_module(Module(0,"Introduction to Physics",10,0,1))
    pY1M.add_module(Module(1,"Kinematics in Mechanics",20,0,1))

    # TEST 6 : Add 1 Module to second year physics

    pY2M = moduleModel(2)

    pY2M.add_module(Module(0,"Advanced Kinematics",20,0,2))

    # TEST 7 : Add 3 Modules to first year maths

    mY1M = moduleModel(5)

    mY1M.add_module(Module(0,"Advanced Algebra",10,0,5))
    mY1M.add_module(Module(1,"Linear Algebra",10,0,5))
    mY1M.add_module(Module(2,"Predicated",20,0,5))

    # TEST 8 : Add an exam and coursework section to all modules 
    py1m2M = assessmentModel(2)
    py1m1M = assessmentModel(1)
    py2m1M = assessmentModel(3)

    my1m1M = assessmentModel(4)
    my1m2M = assessmentModel(5)
    my1m3M = assessmentModel(6)

    py1m2M.add_cw(Coursework(70,0,2))
    py1m2M.add_e(Exam(30,0,2))

    py1m1M.add_cw(Coursework(50,0,1))
    py1m1M.add_e(Exam(50,0,1))

    py2m1M.add_cw(Coursework(75,0,3))
    py2m1M.add_e(Exam(25,0,3))

    my1m1M.add_cw(Coursework(0,0,4))
    my1m1M.add_e(Exam(100,0,4))

    my1m2M.add_cw(Coursework(25,0,5))
    my1m2M.add_e(Exam(75,0,5))

    my1m3M.add_cw(Coursework(25,0,6))
    my1m3M.add_e(Exam(75,0,6))

     

    #TEST 6 : Add 3 assignments to the coursework section of module 2 of physics year 1
    # and 2 assignments to the coursework sectino of module 3 of maths year 1
    py1m2cM = assignmentModel(1)
    my1m3cM = assignmentModel(6)

    py1m2cM.add_assignment(Assignment(0,"CW1",10,0,1))
    py1m2cM.add_assignment(Assignment(1,"CW2",40,0,1))
    py1m2cM.add_assignment(Assignment(2,"CW3",50,0,1))

    my1m3cM.add_assignment(Assignment(0,"CW1",50,0,6))
    my1m3cM.add_assignment(Assignment(1,"CW2",50,0,6))

def test_model2():

    cM = courseModel()
    yM = []
    mM = []
    aseM = []
    asiM = []

    load_data(yM,mM,aseM,asiM)
    
    print("Ym: ",yM)
    # TEST 1 : Edit a course 

    cM.edit_course(Course(0,"Physics and Engineering",53),1)

    # TEST 2 : Edit a year, change the grade of Maths year 1

    yM[1].edit_year(Year(0,"Year 1",0,78,2),5)

    # TEST 3 : Edit a module, change the credits of year 2 physics module Advanced Kinematics to 10

    mM[1].edit_module(Module(0,"Advanced Kinematics",10,0,2),3)

    # TEST 4 : Edit weight values of year 3 maths module Predicates to 50 50 split

    aseM[5].edit_cw(Coursework(50,0,6),6)
    aseM[5].edit_e(Exam(50,0,6),6)

    # TEST 5 : Edit assignment CW1 of physics year 1 module 2 coursework to change grade

    asiM[0].edit_assignment(Assignment(0,"CW1",10,90,1),1)
 

def test_model3():
    cM = courseModel()
    yM = []
    mM = []
    aseM = []
    asiM = []

    load_data(yM,mM,aseM,asiM)

    # TEST 1 : Delete an assignment (CW2) from maths year 1 coursework

    asiM[1].rem_assignment(1)

    # TEST 2 : Delete coursework from physics year 1 module 2, and exam from maths year 1 module 3

    aseM[0].rem_assessment(0)
    aseM[5].rem_assessment(1)

    # TEST 3 : Delete module from maths year 1 module 1

    mM[2].rem_module(0) 

    # TEST 4 : Delete physics year 4

    yM[0].rem_year(3)

    # TEST 5 : Delete maths

    cM.rem_course(1)




#test_model()
#test_model2()
#test_model3()
#load_data()