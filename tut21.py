#class Duck:
#    def quack(self):
#        print ('Quack, quark')
#
#    def fly(self):
#        print('Flap,Flap!')
#
#
#class person:
#    def quack(self):
#        print ("I,m Quarking Vike a Duck!")
#
#    def fly(self):
#        print('I,m Flapping my Arms!')
#
#
#def quack_and_fly(thing):
# #  #LBVL (Non-Pythonic)
# #  if hasattr(thing,'quack'):
# #   if callable(thing.quack):
# #       thing.quack()
##
# #  if hasattr(thing,'fly'):
# #   if callable(thing.fly):
#  #      thing.fly()
#
# try:
#    thing.quark()
#    thing.fly()
#    thing.bark()
# except AttributeError as e:
#    print(e)
#
#
#
#
#    print()

#    d= Duck()
#    quack_and_fly(d)
#
#p =person()
#quack_and_fly(p)


#person={'name':'Jess','age':'23','job':'Programmer'}
person={'name':'Jess','age':'23'   }

#LBYL (NOn-Pythonic)
#if 'name' in person and 'age' in person and 'job' in person:
 #   print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
#else:
 #
 #   print('Missing some keys')


#EARP (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print("Missing {}   key".format(e))