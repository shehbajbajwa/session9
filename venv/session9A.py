"""


 relationship mapping

 HAS-A MAPPING
 1 engineer who is working on 1 project
 1 engineer who is working on many project
 many engineer who is working on many project

  1 college has 1 course
  1 college has many courses
  many colleges have many courses
  college
        name
        phone
        email
   course
     type
     name
     time
"""

class college:
    #create a constructor for standardiszation
    def __init__(self, name, phone, email, course):
        self.name = name
        self.phone = phone
        self.email = email
        self.course = course
#function : update operation
    def updateCollegeDetails(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    #function : read operation
    def showCollegeDetails(self):
        print("=========")
        print("name:\t",self.name)
        print("phone:\t", self.name)
        print("email:\t", self.name)
        print("=========")

     # def __del__(self):
    #        print("this is optional as per requirement)








class course:
    # create a constructor for standardiszation
    def __init__(self, type, name, time):
        self.type = type
        self.name = name
        self.time = time

    # function : update operation
    def updateCourseDetails(self, type, name, time):
        self.type = type
        self.name = name
        self.time = time

    # function : read operation
    def showCourseDetails(self):
        print("=========")
        print("type:\t", self.type)
        print("name:\t", self.name)
        print("time:\t", self.time)
        print("=========")
a1 = course("degree", "btech", "four years")
a2 = course("diploma", "cse", "three years")
#cRef = a1
#cRef.showCourseDetails()
#cRef = a2
#cRef.showCourseDetails()
a1.showCourseDetails()
a2.showCourseDetails()


