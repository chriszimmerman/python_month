import os
pwd = os.getcwd()
myFile = open(pwd + '/testfile.txt')
print(myFile.read())
myFile.close()
