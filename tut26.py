# Python object-Orineted Programming


class Employee:
    num_of_emps = 0
    raise_amt =1.4
    def __init__(self,first,last,pay):
        self.first =first
        self.last = last
        self.pay = pay
        self.email =first+ '.' + last+ '@company.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
        Employee.num_of_emps +=1
    def fullname(self):
          return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self,name):
        first , last = name.split('')
        self.first = first
        self.last = last
    def apply_raise(self):
         self.pay =int(self.pay * self.raise_amt)
    def __repr__(self) -> str:
        return "Employee ('{}','{}','{}',)".format(self.first,self.last,self.pay)
    def __str__(self) -> str:
        return '{}-{}'.format(self.fullname(),self.email)
    def __add__(self,other):
        return self.pay + other.pay
class Developer (Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay,prog_lang):
         super().__init__(first, last, pay)
         self.prog_lang = prog_lang

class Manager(Employee):
     def __init__(self, first, last, pay,employees =None):
         super().__init__(first, last, pay)
         if employees is None:
              self.employees =[]
         else:
              self.employees = employees

     def add_emp(self,emp):
      if emp not in self.employees:
          self.employees.append(emp)

     def remove_emp(self,emp):
         if emp not in self.employees:
             self.employees.remove(emp)
          
     def print_emps(self):
         for emp in self.employees:
             print('-->',emp.fullname())

dev_1= Developer('corey','schefer',50000,'python')
dev_2= Developer('Test','user',40000,'java')


mgr_1 = Manager('Sue','Smith',9000,[dev_1])

#print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

#print(dev_1.email)
# #print(dev_1.prog_lang)

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

    

'''  #@classmethod
    def set_raise_amt(cls,amount):
         cls.raise_amt =amount

    @classmethod
    def from_string(cls,emp_str):
         first, last , pay =emp_str.split('-')
         return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True'''


  
emp_1= Employee('corey','schefer',50000)
emp_2= Employee('Test','user',40000)


print(emp_1+emp_2)


'''import datetime
my_date = datetime.date(2023,4,15)


print(Employee.is_workday(my_date))
'''
'''emp_str_1= 'john-doe-70000'
emp_str_2= 'steve-doe-30000'
emp_str_3= 'jane-doe-90000'

new_emp_1 =Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)'''




#print(Employee.num_of_emps)
'''Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)'''
#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)
#print(emp_2)


#print(emp_1.fullname())
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

