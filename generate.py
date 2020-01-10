import pandas as pd
from collections import defaultdict

from tests import tests_data
from student import student_data
from course import course_data
from config import config

from schema.course import course
from schema.student import student
from schema.test import test

class generate(object):

    def __init__(self):
        config_obj = config()
        self.course_path, self.student_path, self.test_path, self.mark_path = config_obj.get_path()

    def start(self):
        self.course_obj = course_data(self.course_path)
        self.course_obj.read()
        self.test_obj = tests_data(self.test_path)
        self.test_obj.read()
        self.student_obj = student_data(self.student_path)
        self.student_obj.read()

    def update_mark(self):
        if self.mark_path:
            try:
                marks = pd.read_csv(self.mark_path)
                for ind in marks.index:
                    test_dict = self.test_obj.get_dict()
                    val = test_dict[marks['test_id'][ind]]
                    student_dict = self.student_obj.get_dict()
                    stu = student_dict[marks['student_id'][ind]]
                    if val.c_id not in stu.mark:
                        stu.mark[val.c_id] = marks['mark'][ind]*(val.weight/100)
                    else:
                        stu.mark[val.c_id] += marks['mark'][ind]*(val.weight/100)
            except:
                print("Not a valid mark filename!")
        else:
            print("Enter a filename!")

    def publish(self):
        self.student_data = self.student_obj.get_dict()
        for key,value in self.student_data.items():
            avg = (sum(value.mark.values())/len(value.mark.values()))
            file = open("./report/"+value.name+"_name.txt", "a")
            file.write("Student Id: "+str(value.id)+", name: "+value.name+"\n")
            file.write("Total Average:\t"+str(round(avg,2))+"%\n")
            file.write("\n")
            for k,v in value.mark.items():
                course_data = self.course_obj.get_dict()
                file.write("\tCourse: "+course_data[k].name+", Teacher: "+course_data[k].teacher+"\n")
                file.write("\tFinal Grade:\t"+str(round(v,2))+"%\n")
                file.write("\n")
            file.close()
