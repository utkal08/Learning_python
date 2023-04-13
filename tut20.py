#try:
#    f= open('test_file.txt')
#except FileNotFoundError as e:
#    print(e)
#
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close
#   # print('Sorry .This file doesn not exist ')
#
#finally:
#    print("Executing Finally...")
try:
    f= open('curropt_file.txt')
    if f.name == 'currupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(e)
else:
    print(f.read())
    f.close
   # print('Sorry .This file doesn not exist ')

finally:
    print("Executing Finally...")