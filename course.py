import pandas as pd
from collections import defaultdict
from schema.course import course

class course_data(object):

    def __init__(self,filename):
        self.courses_dict = defaultdict()
        self.filename = filename

    def get_dict(self):
        return self.courses_dict

    def read(self):
        if self.filename:
            try:
                courses = pd.read_csv(self.filename)
                for ind in courses.index:
                    self.courses_dict[courses['id'][ind]] = course(courses['id'][ind],courses['name'][ind],courses['teacher'][ind])
            except:
                print("Not a valid course filename!")
        else:
            print("Enter a filename!")
