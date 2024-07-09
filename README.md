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
- The graph is a line graph, which percentage on the y-axis and year on the x-axis
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
