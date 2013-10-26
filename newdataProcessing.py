import csv
import dataRecovery

class readData:

	csvfile1=open('DATA/train.csv', 'rb');
	csvfile2=open('DATA/test.csv', 'rb');
	
	
	TrainCount=0;
	TestCount=0;
	
	TrainXtra=[];
	mainF=0;
	
	fMapTrain=[0,1,0,1,1,1,1,1,1,0,1];
	fMapTest=[1,0,1,1,1,1,1,1,0,1];
	
	TrainHeader=[];
	TestHeader=[];
	
	
	data=[];
	

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
		elif(col=='ticket'):
			if(val=='LINE'): 
				return '1024';
			return val.rpartition(" ")[2];
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
					temp+=[int(float(self.mapDefine((self.TrainHeader[i]),rows[i])))];
			self.data+=[temp];
			self.TrainXtra+=[int(rows[self.mainF])];
		self.TrainCount=len(self.data);
		
		
		csvreader = csv.reader(self.csvfile2, delimiter=',', quotechar='"');
		self.TestHeader=csvreader.next();
		for rows in csvreader:
			temp=[];
			for i in range(0,len(rows)):
				if(self.fMapTest[i]==1):
					temp+=[int(float(self.mapDefine((self.TestHeader[i]),rows[i])))];
			self.data+=[temp];
		self.TestCount=len(self.data)-self.TrainCount;
	
	


	def dump(self):
		HF=dataRecovery.holesFiller('LinearRegression');
		HF.feedData(self.featureFilter(self.fMapTrain,self.TrainHeader),self.data,'age');
		Y=HF.fillData();		
		
		with open('DATA/pnewtrain_v2.csv','wb') as csvfile:
			csvwriter=csv.writer(csvfile,delimiter=',',quotechar='"');
			self.fMapTrain[self.mainF]=1;
			pHeader=self.featureFilter(self.fMapTrain,self.TrainHeader);
			print(pHeader);
			csvwriter.writerow(pHeader);
			for i in range(0,self.TrainCount):
				csvwriter.writerow([self.TrainXtra[i]]+Y[i]);


		with open('DATA/pnewtest_v2.csv','wb') as csvfile:
			csvwriter=csv.writer(csvfile,delimiter=',',quotechar='"');
			pHeader=self.featureFilter(self.fMapTest,self.TestHeader);
			print(pHeader);
			csvwriter.writerows([pHeader]+Y[self.TrainCount:self.TestCount+self.TrainCount]);
			
			
		
		
		

	
	
	
	
	
	
	
	
	
	
	

