import sys
import calendar

def birthday():
	day = int(sys.argv[1])
	month = int(sys.argv[2])
	year = int(sys.argv[3])
	bday = calendar.weekday(year, month, day)
	if bday == 0:
		print("You were born on a Monday and Monday's child is fair of face.")
	elif bday == 1:
		print("You were born on a Tuesday and Tuesday's child is full of grace.")
	elif bday == 2:
		print("You were born on a Wednesday and Wednesday's child is full of woe.")
	elif bday == 3:
		print("You were born on a Thursday and Thursday's child has far to go.")
	elif bday == 4:
		print("You were born on a Friday and Friday's child is loving and giving.")
	elif bday == 5:
		print("You were born on a Saturday and Saturday's child works hard for a living.")
	else:
		print("You were born on a Sunday and Sunday's child is fair and wise and good in every way.")
	
birthday()