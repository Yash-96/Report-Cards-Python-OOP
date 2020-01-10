# Software Assessment - Report Cards

How to run -

1. Install Python and pip installer on your system
2. pip install pandas to install pandas
3. extract the files and open the backend-assessment directory
4. type python app.py in command prompt
5. Check report directory for output or log on screen for error

Brief Overview -

1. Uses OOP principles and Hash_Map to store all data
2. First all data is loaded within objects from students.csv, courses.csv, tests.csv using the schema and respective python programs
3. Then computation of average and writing files take place
4. Separate components are implemented to make scaling and editing easy

Inputs

1. courses.csv
This file contains the courses that a student takes. Each course has a unique id, a
name, and a teacher.

2. students.csv
This file contains all existing students in the database. Each student has a unique id,
and a name.

3. tests.csv
This file contains all the tests for each course in the courses.csv file. The file has three
columns:
● id: the test’s unique id
● course_id: the course id that this test belongs to
● weight: how much of the student’s final grade the test is worth. For example, if a
test is worth 50, that means that this test is worth 50% of the final grade for this
course.

4. marks.csv
This file contains all the mark the student received for all the tests that they have
written.
The file has three columns:
● test_id: the test’s id
● student_id: the student’s id
● mark: The percentage grade the student received for the test (out of 100)
