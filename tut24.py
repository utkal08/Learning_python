# First class Functions

#def square(x):
#    return x*x
#
#
#def my_map(func,arg_list):
#    result =[]
#    for i in arg_list:
#        result.append(func(i))
#    return result
#
#
#squares =my_map(square,[1,2,3,4,5])
#
#print(squares)

'''def logger(msg):

    def log_massage():
        print('Log:',msg)

    return log_massage

log_hi = logger('Hi!')
log_hi()
'''


'''def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')
'''


#Closures

'''def outer_func(msg):
   message= msg

   def inner_func():
      print(message)
   return inner_func
   

hi_func = outer_func("hi")
hello_func= outer_func("hello")

print(hi_func())
print(hello_func())
'''
# Decorators

# Decorators
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)

