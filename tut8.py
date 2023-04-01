#def hello_func(greeting,name='You'):
#   # print('hello Function!')
#   return ' {}  ,{}.'.format(greeting,name)  


#hello_func()
#print(hello_func('hi',name='Corey'))
#DRY

#print('Hello Function!')

#print(len('Test'))

def student_info(*args,**kwargs):
   print(args)
   print(kwargs)

courses = {'Math','Art'}
info ={'Name':'Johnwick','age':22}

#student_info('Math','Art',name='john',age=22)
student_info(*courses,**info)



