# import module
from urllib.request import urlopen
from urllib.error import *
import sys
import os
a = (str(sys.argv[1]))
b= (str(sys.argv[2]))
def static():
 try:
   html = urlopen(b)
 except HTTPError as e:
   return print(e)
 except URLError as e:
    return print(e)
 else:
   return print("200")
def api():
 try:
    html = urlopen(b)
 except HTTPError as e:
    return print(e)
 except URLError as e:
    return print(e)
 else:
    return print(int(200))
def default():
    return "Incorrect type"
def switch(ping):
    return switcher.get(ping, default)()
def unique():
    cmd = ('curl -I -s '+ b + '| grep HTTP')
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
   print("Please Give Valid Type")