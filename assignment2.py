import unittest
import numpy as np

####################################################
# Problem 1: Classes
####################################################
        
class Course:
    def __init__(self, course_number):
        ## Add code here ##
        self.course_number = course_number 
        self.roster = []                #list

    def get_course_number(self):
        ## Add code here ##
        return self.course_number
        
    def add_student(self, student):
        ## Add code here ##
        self.roster.append(student)
        
    def drop_student(self,student):
        ## Add code here ##
        self.roster.remove(student)

        
    def get_roster(self):
        ## Add code here ##
        sorted(self.roster)
        return self.roster


####################################################
# Problem 2: Root Finding
####################################################

def find_roots(a,b,c):
    ## Add code here ##
    #return []
    a = np.float128(a)
    b = np.float128(b)
    c = np.float128(c)
    if a == 0 and b !=0:
        return [-1*c/b]
    elif b == 0:
        return []
    
    delta = (b*b - 4*a*c)
    if delta < 0:
        return []
    elif delta == 0:
        return -1*b/2*a
    else:
        x1 = (-1*b - delta**0.5)/(2*a)
        x2 =  (-1*b + delta**0.5)/(2*a)
        return sorted([x1, x2])



   
  
