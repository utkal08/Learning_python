import logging


logging.basicConfig(filename='employee.log',level=logging.info)
'''def add(x,y):
    return x+y

def sub(x,y):
    return x-y


num_1=10
num_2=5
add_result=add(num_1,num_2)
logging.warning('Add: {}+{}={}'.format(num_1,num_2,add_result))
sub_result=add(num_1,num_2)
logging.warning('Add: {}-{}={}'.format(num_1,num_2,sub_result))'''
class Employee:
    def __init__(self,first,last) :
        self.first=first
        self.last=last
        print('Created Employee:{}-{}'.format(self.fullname,self.email))
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    

    @property 
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    

    emp_1=Employee('utkal','vats')
