#Importing Modules
import math
math.sin(2)

#Module Call
from custommodule import *
print timestwo(2) #returns 4
print timesthree(3) #returns 9

#Pip Module Call, must PIP Install Requests
import reqeusts

r = requests.get('http://www.google.com')
print r.text