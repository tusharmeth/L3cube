import sys
import os
class SVC:
	def __init__(self):
		if(len(sys.argv)==1):
			print "svc is Simple Version Control System. which keep track on single file ."
			print "Options Available : "
			print "1) txtfs SOURCE NAMEOFFILE"
			print "2) txtfs ls"		
			print "3) txtfs FILENUMBER"			
			exit(0)
		elif(len(sys.argv)==2):
				if(sys.argv[1]=="ls"):
					self.display()
				elif(sys.argv[1].isdigit()):
					self.filedisplay()
				else:
					self.create()
	def create(self):
			print "creating"
			file1=open(sys.argv[1],"r+")	
			fileTemp=""			
			try:
				fileTemp=open("temp","r")
				filename=open("name","r")
			except:
				fileTemp=open("temp","w")
				filename=open("name","w")	
				fileTemp.close()
				filename.close()
				fileTemp=open("temp","r")
			oldData=fileTemp.readlines()
			newData=file1.readlines()
		#	print len(oldData)			
			count=0
			fileTemp.close()
			filename=open("name","a")
			current=sys.argv[1]+"\n"
			filename.write(current)
			filename.close()
			fileTemp=open("temp","a")
			temptemp=" "
			for i in range(len(newData)):
				temptemp+=newData[i].rstrip('\n')
				temptemp+=" "
			temptemp+="\n"
			#if(len(oldData)>=2):
				
				#print oldData[-2]		
			
			print temptemp
			
			fileTemp.write(" ")		
			for i in range(len(newData)):
					newData[i]=newData[i][0:-1]
			newData.append("\n")
			#totLines=20
			#if(len(newData)<20):
			totLines=len(newData)
			for i in range(totLines):
					#print newData[i]
					fileTemp.write(newData[i]+" ")
			file1.close()		
			fileTemp.close()
			os.remove(sys.argv[1]);
	def display(self):
			filename=open("name","r")
			readdata=filename.read()
			print readdata
			filename.close()			
			
	def filedisplay(self):
				temp=open("temp","r")	
				for version,data in enumerate(temp):
					if(version==int(sys.argv[1])-1):
						print data
						exit(0)
				temp.close()	
trackFile=SVC()				
