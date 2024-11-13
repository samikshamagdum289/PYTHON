# #for read the content in smpl.txt
# file=open('smpl.txt','r')
# print(file.read())
# print(file)

# #only create the new file
# file=open('smpl2.txt','x') #for only creating the file use a,x,w
# print('file is created')

# create and read the file
# f1=open('example.txt','w')
# print('file is created')
# print(f1.write("My name is samiksha.")) #here the file is created and the new content is write in file

# #Append the file in existing file
# f2=open('example.txt','a')
# print(f2.write("My age is 20."))
# print(f2.read())

# #to read and write data in file 
# file=open('smpl2.txt','r+')
# print(file.write('Good Morning.'))
# file.seek(6)    #O/P-> orning
# print(file.read())

# #read and write data and overite 
# file=open('smpl2.txt','w+')
# print(file.write('My name is samiksha magdum.'))
# print(file.read())

# # append and read in file
# file=open('smpl2.txt','a+')
# print(file.write('I am studing is DYPCET.'))
# print(file.read())