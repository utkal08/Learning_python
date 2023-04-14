# Python object-Orineted Programming


class Employee:
    def __init__(self,first,last,pay):
        self.first =first
        self.last = last
        self.pay = pay
        self.email =first+ '.' + last+ '@company.com'
    def fullname(self):
          return '{} {}'.format(self.first, self.last)
emp_1= Employee('corey','schefer',50000)
emp_2= Employee('Test','user',40000)




print(emp_1)
print(emp_2)


print(emp_1.fullname())
#print('{}{}'.format(emp_1.first,emp_1.last))


#emp_1.first = 'Utkal'
#emp_1.last = 'vats'
#emp_1.email= 'utkal.vats@gmail.com'
#emp_1.pay =50000
#
#emp_2.first = 'rahul'
#emp_2.last = 'vats'
#emp_2.email= 'rahul.vats@gmail.com'
#emp_2.pay =50000

#print(emp_1.email)
#print(emp_2.email)

