# ProgressManager

Application which can be used to store data about how well the user is doing at uni.

# Requirements

## User Interaction

- The application should allow users to enter the name of course
- The application should allow users to enter the number of years studying the course and the weight of each year for the degree
- The application should allow users to enter the names of modules for each year, and the number of credits for each module
- The application should allow users to add 1/2 sections to each module (exam and coursework) and the weight of each section for the module
- The application should allow users to add subsections to the coursework section for individual assignments
- The application should allow users to enter the mark/ percentage recieved for each assignment
- The application should allow users to enter the mark/ percentage for the exam
- The user can edit the values of any of these at anytime but under a different mode

## Application Outputs

- There is a main screen which displays the courses undertaken
- There is a sub screen for each course with displays stats for each year as well as a graph which displays the progress of the course
- There is a sub screen for each year which displays stats for each module as well as a graph which displays the progress of the year
- There is a sub screen for each module which displays the stats for coursework and exam as well as a graph which displays the progress of the module
- There is a sub screen for courseworks which displays stats for each assignment as well as a graph which displays the progress of the courseworks

# Specifications

## User Interaction

### Main (Courses Screen)

- There is an add button on the main screen to add courses
  - Clicking this will add a widget to the screen with a default name
  - The widget will have an edit button which lets users change the name of the course
  - Clicking on the widget will open a new screen for the specific course

### Years Screen

- There is an add button on this screen to add years

- Clicking will add a widget to the screen with an incrementing name
  - Intially the widget will only have its name as there is no content
- There is an empty graph on the side which updates as years are added
- The graph is a line graph, which shows percentage on the y-axis and year on the x-axis
- The plot for each year is the weighted grade from that year for the course
- The line should have alternating colours between the years (black,white,black)
- There are 4 horizontal lines that cross the y-axis which represent pass, lower second, higher second and first grade lines.
- There is an edit button on year widget which lets users change the name of the year
- Clicking on a year widget will open a new screen for that year

### Modules Screen

- There is an add button on this scren to add a module

- Clicking this will open a window where the user has to enter some details of the module (name, credits, exam weight, coursework weight)

        - There will be a button on this window to save these details and add the module widget, or cancel

- The widget will display its name, then the number of credits, and then the current mark for this module.

- There is an empty graph on the side which updates as modules are added

- y-axis same, lines same, x-axis modules which diffeent colours

# Database Schema

There will be two databases used within the program, one is runtime in memory and the second is a persistant database held in MySQL. Reason for this is better performace during runtime, the database will be loaded in from MySQL at the start of the application and result in faster access during runtime for read only functions. I also started coding with a runtime database and once implementing the persistant database I could not be asked to change.

<b> Table : Course</b>

- id (PK)
- title
- grade

<b> Table : Year</b>

- id (PK)
- year(title)
- weight
- grade
- course_id (FK)

<b> Table : Module</b>

- id (PK)
- title
- credits
- grade
- year_id (FK)

<b> Table : Coursework</b>

- id (PK)
- title
- weight
- grade
- module_id (FK)

<b> Table : Exam </b>

- id (PK)
- title
- weight
- grade
- module_id (FK)

<b> Table : Assignments</b>

- id (PK)
- title
- weight
- grade
- coursework_id (FK)

## Problems

### Model

- Issue when deleting records (FIXED)

  - As the id of the individual objects are determined by which parent they belong to whilst the database tables have incrementing id regardless of what parent a record belongs to.
  - E.g If there are 2 modules in year 1 and 2 more in year 2. The modules will have IDs 1 and 2 for each year whilst in the database they will have IDs 1,2,3,4.
  - This makes it difficult to delete a record using the id attribute

- Limited exam and coursework for each module

  - Currently each module can only have 1 exam and functions have been implemented to manipulate databases given there is only 1 exam per module
    - However, it is easy to modify the code for multiple exams but will only implement in the future when it is required for other users as for now it is not needed for me

- CUrrently class attributes are public so the get and set methods in class are redundant, also some code is written using getter and setter, whilst some directly accesses attributes, will need to encapsulate and change code in future

### View

- Need to change code to set max columns when displaying the courses widgets

  - Currently max columns is hard coded as 4
  - Need to change this to be dynamic when the window width changes

- Problem with qss, not important right now but will be for final touches

- Graph asthetics need to be done (later), add functionality/buttons to remove boundary lines

- Improve code/performance by deleting widgte when refreshing

- Not sure whether the array of buttons is needed when displaying all courses/years...

-- Need to adjust size of buttons to fit content and no more, icon buttons sometimes take more space than needed

## To Do

- Need to retrieve data from database at the start of application but need to recreate all models without knowing how many courses,years,modules e.t.c were created. Could be tricky (Done)

- Need to test if works when multiple records of different parent records are added, may not work due to issue with different ids in the runtime models and the mysql database (DONE)

- Realised some code to do with manipulating the runtime database is redundant having the `load data` function can update the runtime at any point (DONE)

- Could add a further attribute to years,module etc which is the grade adjusted for the weight (FUTURE)

- View only skeleton, spruce up and do lot more styling

- Controller, grade should be "-" not 0 when when grade not given so graph does not show no grade change

- Controller should check if weights added up is equal to 100

- Controller should override typed in grades, if there are child items that contribute to grade

- Issue with deleting when item have same name, will instead delete first occurence of that name, need to add functinoality that checks whether item of same name already exists before adding (DONE)

- Issue with being able to add elements with no title (DONE)

- Possible redundant code in controller alerts, with `if not(exists)` being used for when there isn't even a model in the array to add to

- Issue with closing edit window after successful edit, issue with not refreshing display after edit

- (FUTURE) add an attribute to say whether year is a masters year, can put credits to 120 and 180 so as to get better graphs immediately instead of having to add all modules to get correct graph
