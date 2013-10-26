import csv

class pull:
	
	csvfile1=open('../DATA/pnewtrain_v2.csv', 'rb');
	csvfile2=open('../DATA/pnewtest_v2.csv', 'rb');
	
	
	TrainCount=0;
	TestCount=0;
	
	mainF=0;
	
	fMapTrain=[0,1,1,1,1,1,1,1,1];
	fMapTest=[1,1,1,1,1,1,1,1];
	
	TrainHeader=[];
	TestHeader=[];
	
	TrainXtra=[];
	trainData=[];
	testData=[];

	#Filtering relevant features and discarding rest
	def featureFilter(self,Fmap,rawHeader):
		temp=[];
		for i in range(0,len(rawHeader)):
			if(Fmap[i]==1):
				temp+=[rawHeader[i]];
		return temp;

	
	def mapDefine(self,col,val):
		if(col=='sex'):
			if(val=='male'): 
				return '0';
			elif(val=='female'):
				return '1';
		elif((col=='age') & (val!='')):
			age=int(float(val));
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

	
	

	def parse(self):
		csvreader = csv.reader(self.csvfile1, delimiter=',', quotechar='"');
		self.TrainHeader=csvreader.next();
		for rows in csvreader:
			temp=[];
			for i in range(0,len(rows)):
				if(self.fMapTrain[i]==1):
					temp+=[(float((rows[i])))];
			self.trainData+=[temp];
			self.TrainXtra+=[int(rows[self.mainF])];
		
		
		csvreader = csv.reader(self.csvfile2, delimiter=',', quotechar='"');
		self.TestHeader=csvreader.next();
		for rows in csvreader:
			temp=[];
			for i in range(0,len(rows)):
				if(self.fMapTest[i]==1):
					temp+=[(float((rows[i])))];
			self.testData+=[temp];
	
	


	
	
	
	
	
	
			
			
		
		
		

	
	
	
	
	
	
	
	
	
	
	

