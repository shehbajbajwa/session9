
#====================================================================
class College:

    # Constructor for Standardization
    # def __init__(self, name, phone, email, address):
    #     self.name = name
    #     self.phone = phone
    #     self.email = email
    #     self.address = address # HAS-A | 1 to 1

    def __init__(self, name, phone, email, Courses):
        self.name = name
        self.phone = phone
        self.email = email
        self.Courses = Courses # HAS-A | 1 to many

    # Function : Update Operation
    def updateCollegeDetails(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # Function : Read Operation
    def showCollegeDetails(self):
        print("=================")
        print("Name:\t",self.name)
        print("Phone:\t", self.phone)
        print("Email:\t", self.email)
        print("=================")

        print(">> course List for {}:".format(self.name))

        # self.course.showCourseDetails() # 1 to 1
        for courses in self.Courses:         # 1 to *
            course.showCourseDetails()

        print(">>>>>>>>>>>>>>>>>>>>")

    # Business Function : Will have logical processing (Controller)
    def getTotalCourses(self):
        return len(self.Courses)


    # def __del__(self):
    #     print("This is optional as per requirement")

class Course:

    # Constructor for Standardization
    def __init__(self, type, name, time):
        self.type = type
        self.name = name
        self.time = time

    # Function : Update Operation
    def updateCourseDetails(self, type, name, time):
        self.type = type
        self.name = name
        self.time = time

    # Function : Read Operation
    def showCourseDetails(self):
        print("=================")
        print("type:\t",self.type)
        print("name:\t", self.name)
        print("time:\t", self.time)
        print("=================")


courseList = []
choice = "yes"
while choice == "yes":
    courseList = course(None, None, None)
    course.type = input("Enter typee: ")
    course.name = input("Enter name: ")
    course.time = input("Enter time: ")
    courseList.append(course)

    choice = input("Would you like to add another course (yes/no): ")

"""
a1 = Address(None, None, None)
a1.adrsLine = input("Enter Address Line: ")
a1.city = input("Enter City: ")
a1.state = input("Enter State: ")
a2 = Address("Country Homes", "Ludhiana", "Punjab")
# List of Addresses
adrsList = [a1, a2]
"""
# c1 = Customer("John", "+91 99999 88888", "john@example.com", a1)
c1 = College("John", "+91 99999 88888", "john@example.com", courseList)

# c1.showCustomerDetails()

cRef = c1
cRef.showCollegeDetails()

# a1.showAddressDetails()
# a2.showAddressDetails()



