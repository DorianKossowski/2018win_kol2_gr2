# Class diary  

from random import randint
from statistics import mean
import json

def add_class(classes, new_class):
	if new_class not in classes:
		classes.update({new_class:[]})

def add_student(classes, student_class, name, surname):
	if student_class not in classes:
		print('Class {} does not exist.'.format(student_class))
	else:
		string = name + ' ' + surname
		student_dict = {}
		student_dict.update({string:{'scores':[],'attendance':[]}})
		for s_dict in classes[student_class]:
			if string in s_dict:
				print('Student {} already in the class.'.format(string))
				break
		else:
			classes[student_class].append(student_dict)

def print_students(classes, proper_class = 'All'):
	if proper_class == 'All':
		for class_name in classes:
			print('Class {}:'.format(class_name))
			for student_dict in classes[class_name]:
				for student in student_dict:
					print('\t{}: grades: {}, attendance: {}'.format(student, student_dict[student]['scores'], student_dict[student]['attendance'] ))
	else:
		if proper_class not in classes:
			print('Class {} does not exist.'.format(proper_class))
		else:
			print('Class {}:'.format(proper_class))
			for student_dict in classes[proper_class]:
				for student in student_dict:
					print('\t{}: grades: {}, attendance: {}'.format(student, student_dict[student]['scores'], student_dict[student]['attendance'] ))

def be_present(classes, proper_class, name):
	if proper_class not in classes:
		print('Class {} does not exist.'.format(proper_class))
	else:
		for student_dict in classes[proper_class]:
			if name in student_dict:
				student_dict[name]['attendance'].append(True)
				break
		else:
			print('Student {} does not exist in class {}.'.format(name, proper_class))

def add_grade(classes, proper_class, name, grade):
	if proper_class not in classes:
		print('Class {} does not exist.'.format(proper_class))
	else:
		for student_dict in classes[proper_class]:
			if name in student_dict:
				student_dict[name]['scores'].append(grade)
				break
		else:
			print('Student {} does not exist in class {}.'.format(name, proper_class))

def stats_in_class(classes, proper_class):
	if proper_class not in classes:
		print('Class {} does not exist.'.format(proper_class))
	else:
		print('Statistics - class {}:'.format(proper_class))
		scores = []
		attendance = 0
		for student_dict in classes[proper_class]:
			for name in student_dict:
				print('\t{}: average = {}, attendance = {}'.format(name, mean(student_dict[name]['scores']), len(student_dict[name]['attendance'])))
				scores.extend(student_dict[name]['scores'])
				attendance += len(student_dict[name]['attendance'])
		print('\tAverage = {}, attendance = {}'.format(mean(scores), attendance))

def stats_in_school(classes):
	print('Statistics - school:')
	scores = []
	attendance = 0
	for class_name in classes:
		for student_dict in classes[class_name]:
			for name in student_dict:
				scores.extend(student_dict[name]['scores'])
				attendance += len(student_dict[name]['attendance'])
	print('\tAverage = {}, attendance = {}'.format(mean(scores), attendance))


def file_json(classes, file_name, operation = 'load'):
	if operation == 'save':
		with open(file_name, 'w') as outfile:
			json.dump(classes, outfile)
			return None
	else:
		with open(file_name, 'r') as infile:
			return json.load(infile)

if __name__ == "__main__":

	classes = {}

	# classes = file_json(classes, 'classes.json')

	add_class(classes, 'A')
	add_class(classes, 'B')

	add_student(classes, 'A', 'Eden', 'Hazard')
	add_student(classes, 'A', 'Eden', 'Hazard')
	add_student(classes, 'B', 'David', 'Luiz')
	add_student(classes, 'A', 'Juan', 'Mata')
	add_student(classes, 'C', 'Petr', 'Cech')

	be_present(classes, 'B', 'David Luiz')
	be_present(classes, 'A', 'Eden Hazard')

	add_grade(classes, 'A', 'Juan Mata', randint(2,5))
	add_grade(classes, 'A', 'Juan Mata', randint(2,5))
	add_grade(classes, 'A', 'Eden Hazard', randint(2,5))
	add_grade(classes, 'A', 'David Luiz', randint(2,5))
	add_grade(classes, 'B', 'David Luiz', randint(2,5))


	print_students(classes)
	stats_in_class(classes, 'A')
	stats_in_school(classes)

	file_json(classes, 'classes.json', 'save')