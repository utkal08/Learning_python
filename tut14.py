import os
from datetime import datetime
#print(os.getcwd())
os.chdir('C:\Users\utkal\Learning_python')

'''for dirpath, dirnames, filenames in os.walk('C:\Users\utkal\Learning_python'):
    print('Current Path:',dirpath)
    print('Directories:',dirnames)
    print('Files:',filenames)
    print()'''
#print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'),'test.txt')
print(file_path)
#os.makedirs('OS-Demo-2/Sub-Dir-1')
#os.removedirs('OS-Demo-2/Sub-Dir-1')

#os.rename('text.txt','_dem_')

#mod_time = os.stat('demo.txt').st_mtime
#print(datetime.fromtimestamp(mod_time))
#print(os.stat('demo.txt'))
#print(os.listdir())