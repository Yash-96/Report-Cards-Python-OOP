class config(object):

    def __init__(self):
        self.course_path = "./data/courses.csv"
        self.student_path = "./data/students.csv"
        self.test_path = "./data/tests.csv"
        self.mark_path = "./data/marks.csv"

    def get_path(self):
        return self.course_path, self.student_path, self.test_path, self.mark_path
