person ={'name':'john','age':23}

#sentence = 'My name is '+ person['name'] + 'and I am' + str(person['age']) +'years old.'
#sentence = 'My name is {}  and I am {} years old.'.format(person['name'],person['age'])


'''tag = 'hi'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence)'''


'''class Person():
     def __init__(self, name,age) :
        self.name =name
        self.age =age
p1= Person('jack','23')

sentence= 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)'''



'''person = {'name':'jehn','age':23}
sentence= 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)'''

'''for i in range(1,11):
     sentence = 'This value is {:2f}'.format(i)
     print(sentence)'''
'''pi = 3.14159265

sentence ="Pi is equal to {:.2f}".format(pi)
print(sentence)'''

import datetime
my_date = datetime.datetime(2023,4,3,4,51,50)
print (my_date)

#sentence ='{:%B %d, %Y}'.format(my_date)
#print(sentence)

sentence ='{:%B %d, %Y}'.format(my_date)
print(sentence)

sentence='{:%B %d ,%Y} fell on a {:%A} and was the {:%j} day of the year'.format(my_date)
print(sentence)



