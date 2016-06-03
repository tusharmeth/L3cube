import sys

class SVC:
	def __init__(self):
		if(len(sys.argv)==1):
			print "svc is Simple Version Control System. which keep track on single file ."
			print "Options Available : "
			print "1) svc FILENAME commit file"	#python svc.py xyz.txt 
			print "2) svc N display version number"		#python svc.py number
			exit(0)
		elif(len(sys.argv)==2):
				if(sys.argv[1].isdigit()):
					self.display()
				else:
					self.commit()
	def commit(self):
			print "commiting"
			file1=open(sys.argv[1],"r+")	
			fileTemp=""			
			try:
				fileTemp=open("temp","r")
			except:
				fileTemp=open("temp","w")	
				fileTemp.close()
				fileTemp=open("temp","r")
			oldData=fileTemp.readlines()
			newData=file1.readlines()
		#	print len(oldData)			
			count=0
			fileTemp.close()
			fileTemp=open("temp","a")
			temptemp=" "
			for i in range(len(newData)):
				temptemp+=newData[i].rstrip('\n')
				temptemp+=" "
			temptemp+="\n"
			if(len(oldData)>=2):
				
				print oldData[-2]		
			
			print temptemp
			if(len(oldData)>=2):
				if(oldData[-2]==temptemp):
					print "already commited!!!"		
					exit(0)
			else:
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
				
			
	def display(self):
				i=int(sys.argv[1])
				temp=open("temp","r")	
				totVersion=0
				for version,data in enumerate(temp):
					if(version==i):
						print version,data
						exit(0)
					totVersion+=1	
				else:
					print "available versions :"+str(totVersion)
				temp.close()	
				
				
trackFile=SVC()				
