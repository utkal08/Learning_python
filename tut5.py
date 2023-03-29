student = {'name':'john','age':'25','courses':['Math','CompSci']}#1

#print(student)#2
#print(student['name'])#3

#student.update({'name':'Jane','age':26,'phone':'349237'}) 8

#print(student['courses'])#4
#print(student[1])#5
#student['phone']='555-5555'#7
#print(student.get('phone'))#6
 #age =student.pop('age')10
#del student['age'] 9
#print(student)11
#print(len(student))12
#print(student.keys())13
#print(student.items())14

for key ,value in student.items():

    print(key,value)


