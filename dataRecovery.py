# import available Training models
import LinearRegression 
import math

class holesFiller:
	trainingY=[];
	trainingFeatures=[];
	
	dataHeader=[];
	originalData=[];
	incompleteColumnName='';
	
	trainingModel='';
	
	def __init__(self,model):
		self.trainingModel=model;
	
	
	def feedData(self,headerX,X,incompleteColumnName):
		self.incompleteColumnName=incompleteColumnName;
		self.originalData=X;
		self.dataHeader=headerX;		
		training=False;
		for i in range(0,len(X)):
			deck=X[i];
			tempF=[];
			tempY=[];		
			for j in range(0,len(headerX)):
				if(headerX[j]!=incompleteColumnName):
					tempF+=[deck[j]];
				elif(headerX[j]==incompleteColumnName):
					if(deck[j]!=-1):
						tempY+=[deck[j]];
						training=True;
					else: 
						training=False;
			if(training):		
				self.trainingFeatures+=[tempF];
				self.trainingY+=tempY;

	def fillData(self):
		model='';
		if(self.trainingModel=='LinearRegression'):
			model=LinearRegression.LinearRegression();
			print('Trained model');
			model.train(self.trainingFeatures,self.trainingY);			
			X=self.originalData;
			headerX=self.dataHeader;
			
			predict=False;
			features=[];
			index=0;
			for i in range(0,len(X)):
				temp=X[i];
				for j in range(0,len(headerX)):
					if(headerX[j]==self.incompleteColumnName):
						index=j;
						if(temp[j]==-1):
							predict=True;
						else:
							predict=False;
				if(predict):
					del temp[index];	
					temp[index:index]=[math.fabs(model.predict(temp).tolist()[0][0])];
				X[i]=temp;					
		return X;			
					
					
					