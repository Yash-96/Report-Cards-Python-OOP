from collections import defaultdict

class student(object):

    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.mark = defaultdict()
