#li =[9,4,53,53,4,3,5,2,1]
#
#s_li =sorted(li,reverse=True)
#print(s_li)
#
#li.sort()
#print(li)


#tup =(9,1,32,4,2,6,)
#s_tup = sorted(tup) # valid
##tup.sort()  Invalid
#
#print(s_tup)


#di ={'Bruce','Clark','peter','Logan','wade'}
#
#s_di=sorted(di)
#print("Dict\t",s_di)

'''li =[-6,-5,-4,1,2,3]
s_li= sorted(li,key=abs)
print(s_li)'''

class Employee():
    def __init__ (self,name,age,salary):
        self.name=name
        self.age =age
        self.salary=salary
    def __repr__(self) :
        return '({},{},${})'.format(self.name,self.age,self.salary)
from operator import attrgetter
e1= Employee('carl',37,70000)
e2= Employee('Sarah',29,80000)
e3= Employee('John',43,90000)

employees =[e1,e2,e3]

#def e_sort(emp):
#    return emp.age

s_employees= sorted(employees,key=attrgetter('age'))

print(s_employees)  






