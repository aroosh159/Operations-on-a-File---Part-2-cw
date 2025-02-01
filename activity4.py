file2 = open('contentof2fileuedinactivity4.txt','r')
file1 = open('contentoffile1usedinactivity4.txt','r')
data1 = file1.read()
data2 = file2.read()
data1 += "\n"
data1 += data2
file3 = open('New_file.txt','w')
file3.write(data1)
