print("Hello!")

import time

def set_procname(newname):
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
	buff = create_string_buffer(len(newname)+1) #Note: One larger than the name (man prctl says that)
	buff.value = bytes(newname, "UTF-8")                 #Null terminated string as it should be
	libc.prctl(15, byref(buff), 0, 0, 0)

set_procname("helloworldloop")

while True:
	time.sleep(0.125)
	print("Hello world!")