# File objects

#with open ('test.txt','r') as f: 
 
 #for line in f:
 #     print(line, end ='')
# size_to_read =10
#
# f_contents = f.read(size_to_read)
##f_contents = f.readlines()
#print(f_contents,end='')
#f.seek(0)
#f_contents = f.read(size_to_read)
#print(f_contents)
#
#f = open('test.txt','r')
#
#
#print(f.mode)

#f.close()
#with open ('test2.txt','w') as f: 
# f.write('test2.txt')

with open('','rb') as rf:
    with open('','wb') as wf:
     chunk_size =4096
     rf_chunk = rf.read(chunk_size)