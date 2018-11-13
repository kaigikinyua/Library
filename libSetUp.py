import os
class MyFiles:
	def __init__(self):
	   if(os.path.isfile("details.txt")):
		d=open("details.txt","r")
		message=d.readlines()
		print message[0]
		d.close()
	   else:
		d=open("details.txt","w")
		d.write("username and password")
		d.close()
l=MyFiles()
