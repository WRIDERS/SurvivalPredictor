import csv
import ../dataRecovery
class readData:
	
	csvfile= open('../DATA/ptrain_v2.csv', 'rb');
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"');


	pHeader=spamreader.next();
	pFeatures=[1,0,1,1,1,1,0,1,0,1]# 1 if the data in that column is to be taken into algorithm
	
	
	
	
	

	#Filtering relevant features and discarding rest
	def featureFilter(self,Fmap,rawHeader):
		temp=[];
		for i in range(0,len(rawHeader)):
			if(Fmap[i]==1):
				temp+=[rawHeader[i]];
		return temp;

	# Function for processing input parameters mapping them to integers so that they can be fed to Learning algorithm
	def mapDefine(self,col,val):
		if(col=='sex'):
			if(val=='male'): 
				return '0';
			elif(val=='female'):
				return '1';
		elif((col=='age') & (val!='')):
			age=int(float(val));
#			if(age<=20):
#				return '0';
#			elif(age>20 & age<=40):
#				return '1';	
#			elif(age>40 & age<=60):
#				return '2';	
#			elif(age>60 & age<=80):
#				return '3';				
			return age;
		elif(col=='embarked'):
			if(val=='C'):   #C-> Boarding at Cherbourg 	
				return '0';
			if(val=='Q'):	#Q-> Boarding at Queenstown
				return '1';
			if(val=='S'):	#S-> Boarding at Southampton
				return '2';	
		elif(val!=''):
			return val;			
		return '-1';


	
	pData=[] #List to hold the processed Data 
	
	def parse(self):
		# Data Processing
		for row in self.spamreader:
			temp=[]
			for i in range(0,len(row)):
				if(self.pFeatures[i]==1):
					temp+=[int(float(self.mapDefine((self.pHeader[i]),row[i])))]
			self.pData+=[temp]		


	def 

			
			

		
	
	def dump(self):	
		pData=self.parse();
		with open('DATA/ptest_v2.csv','wb') as csvfile:
			csvwriter=csv.writer(csvfile,delimiter=',',quotechar='"');
			pHeader=self.featureFilter(self.pFeatures,self.pHeader);
			print(pHeader);
			csvwriter.writerows([pHeader]+pData);
				
		

#n=input("Press Enter");		 
#print featureFilter(pFeatures,pHeader);
#print pData[n];



		 
		 