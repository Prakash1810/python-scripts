# import module
from urllib.request import urlopen
from urllib.error import *
import sys
import os

print (len(sys.argv))
print (str(sys.argv))

a = (str(sys.argv[1]))
print(a)
b = (str(sys.argv[2]))
print(b)
c = (str(sys.argv[3]))
print(c)
d = b+c



def static(): 
 # try block to read URL
 try:
   html = urlopen(b)
     
 # except block to catch
 # exception
 # and identify error
 except HTTPError as e:
   return print("HTTP error", e)
     
 except URLError as e:
    return print("Opps ! Page not found!", e)
 
 else:
   return print('Yeah !  found in static')


def api():
 try:
    html = urlopen(d)     
 # except block to catch
 # exception
 # and identify error
 except HTTPError as e:
    return print("HTTP error", e)
     
 except URLError as e:
    return print("Opps ! Page not found!", e)
 else:
    return print('Yeah !  found in api')

def default():
    return "Incorrect type"


def switch(ping):
    return switcher.get(ping, default)()

def unique():
    cmd = ('curl -I '+ b + '| grep HTTP')
    os.system(cmd)
    
    


switcher = {
    1: static,
    2: api,
    3: unique
    }
if (a == "static"):
    (switch(1))
elif ( a == "api"):
    (switch(2))
elif (a == "unique"):
    (switch(3))    
else :
   print("please give valid type") 

             