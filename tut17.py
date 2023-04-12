import os

os.chdir(r"C:\Users\utkal\OneDrive\Pictures\Camera Roll")

for f in os.listdir():
   
    file_name,file_ext=os.path.splitext(f)
   # print(f)
    #print(file_name.split(''))

    f_title, f_course,f_num =file_name.split('-')
    print(f_title)