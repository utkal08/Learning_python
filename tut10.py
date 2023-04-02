'''
LEGB
Local,Enclosing,Global,built-in
'''

import builtins
#print(dir(builtins))

def outer():
    x = 'outer x'
    def inner():
        x= 'inner x'
        print(x)

    inner()
    print(x)

outer() 
       
        


m= min([3,56,7,3,5 ])