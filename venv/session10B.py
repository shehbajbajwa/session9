class parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print(">>parent constructor executed")
    def showDetails(self):
        print(">>hello,",self.fname,self.lname)
class child(parent):
    def __init__(self,fname, lname, vehicles, salary):
        parent.__init__(self,fname,lname)
        self.vehicles = vehicles
        self.salary = salary
        print(">>child constructor executed")
    def show(self):
        print(">>hello,",self.fname,self.lname, self.vehicles, self.salary)   # u can remove fname and lname in this line and add parent.showdetails(self):

print("++++",parent.__dict__)
print("======",child.__dict__)

ch = child("john","watson",3,30000)
print(ch.__dict__)
ch.showDetails()