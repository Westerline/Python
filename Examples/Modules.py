# Importing Modules
import reqeusts
from custommodule import *
import math
math.sin(2)

# Module Call
print(timestwo(2))  # returns 4
print(timesthree(3))  # returns 9

# Pip Module Call, must PIP Install Requests

r = requests.get('http://www.google.com')
print(r.text)
