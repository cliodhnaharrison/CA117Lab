from collections import namedtuple

Student = namedtuple("Student", ["firstname", "surname", "id"])
		
def show_student(s):
	line1 = "First name: {}".format(s.firstname)
	line2 = "   Surname: {}".format(s.surname)
	line3 = "        ID: {}".format(s.id)
	print("\n".join([line1, line2, line3]))
	