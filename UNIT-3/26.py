import os
import sys


f=open("demo.txt","w")
f.write("Hello...Here Example of file handling function")
f.close()


print('current directory is:',os.getcwd())
print('List of  directory is',os.listdir())

print('Path',os.path.abspath('demo.txt'))

print('Version',sys.version)
print('Arguement:',sys.argv)

os.remove('demo.txt')
print('removed successfully')
