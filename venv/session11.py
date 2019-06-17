class login:

    def loginUser(self):
        print(">> login dear user!!")

class googlelogin(login):
    def loginUser(self,email,password):
        print(">> google login done")

class OTPlogin(login):
    def loginUser(self,phone):
        print(">> otp login done")

class facebooklogin(login):
    def loginUser(self,fbusername,password):
        print(">> fb login done")

class cab:
    def bookcab(self,source,destination):
        print(">> cab booked from {} to {}".format(source,destination))

class olamini:
    def bookcab(self,source,destination):
        print(">> olamini booked from {} to {}".format(source,destination))
class olasedan:
    def bookcab(self,source,destination):
        print(">> olasedan booked from {} to {}".format(source,destination))

login = login()
login.loginUser()

print()

login = googlelogin()
login.loginUser("john@example.com","pass123")
print()

login = OTPlogin()
login.loginUser("+91 99999 88888")
print()

cab = cab()
cab.bookcab("silver","mbd")

cab = olasedan()
cab.bookcab("silver","mbd")