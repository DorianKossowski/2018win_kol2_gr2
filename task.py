# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)

def add_student(name, surname, stu_class):
	names.append(name)
	surnames.append(surname)
	classes.append(stu_class)
	grades.append([])

def add_grade(name, surname, grade):
	this_student = [index for index in range(len(names)) if names[index]==name]
	for i in range(len(names)):
		if surnames[i] == surname:
			grades[i].append(grade)

def print_students():
	amount = len(names)
	print('-----------------------------------------')
	print('Amount of students: {}'.format(amount))	

	for index in range(amount):
		print ('Student: {} {} - class {}'.format(names[index], surnames[index], classes[index]))
		print ('Grades: {}'.format(grades[index]))
		if grades[index]:
			average = float(sum(grades[index])) / (len(grades[index]))
			print ('Average: {}'.format(average))
		else:
			print ('Average: None')



if __name__ == "__main__":
	names = []
	surnames = []
	classes = []
	grades = []


	add_student('imie', 'nazwisko', 'A')
	add_student('drugie', 'nazwiskodrugie', 'B')

	print_students()

	add_grade('drugie', 'nazwiskodrugie', 5)
	add_grade('drugie', 'nazwiskodrugie', 2)

	print_students()