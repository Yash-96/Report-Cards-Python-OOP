import pandas as pd
from collections import defaultdict
from schema.test import test

class tests_data(object):

    def __init__(self,filename):
        self.tests_dict = {}
        self.filename = filename

    def get_dict(self):
        return self.tests_dict

    def read(self):
        if self.filename:
            try:
                tests = pd.read_csv(self.filename)
                for ind in tests.index:
                    self.tests_dict[tests['id'][ind]] = test(tests['id'][ind],tests['course_id'][ind],tests['weight'][ind])
            except:
                print("Not a valid test filename!")
        else:
            print("Enter a filename!")
