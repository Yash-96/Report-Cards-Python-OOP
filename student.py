import pandas as pd
from collections import defaultdict
from schema.student import student

class student_data(object):

    def __init__(self,filename):
        self.students_dict = defaultdict()
        self.filename = filename

    def get_dict(self):
        return self.students_dict

    def read(self):
        if self.filename:
            try:
                students = pd.read_csv(self.filename)
                for ind in students.index:
                    self.students_dict[students['id'][ind]] = student(students['id'][ind],students['name'][ind])
            except:
                print("Not a valid student filename!")
        else:
            print("Enter a filename!")
