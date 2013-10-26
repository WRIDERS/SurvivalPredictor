from numpy import matrix
from numpy import linalg
class LinearRegression:
	theta=matrix([]);
	
	
	def orderIncrement(self,X):
		print(len(X));
		n=len(X[0]);
		nX=[];
		for i in range(0,len(X)):
			temp=[];
			for j in range(0,n):
				temp+=[X[i][j]];				
			for j in range(0,n):
				for k in range(0,n):
					ad=temp[j]*temp[k];
					if(j==k):
						pass;
						#temp+=[ad];
					elif(j!=k):
						if(j<k):
							pass;
							temp+=[ad/2.0];
						elif(j>k):
							pass;
							#print(j,k,len(temp),n+n*k-(k*(k+1)/2)+j);
							temp[n+n*k-((k*(k+1))/2)+j-k-1]+=ad/2.0;
			nX+=[temp];				
		return nX;

	#Caliberating input features to make it compatible with theta0
	def addOnes(self,X):
		for i in range(0,len(X)):
			temp=[1]+X[i];
			X[i]=temp;
		return X;		

	#Training using Normal Equation		
	def train(self,X,y):	
		Xn=X;
		Xn=self.orderIncrement(Xn);
		print('Order increment');
		print(len(Xn),len(Xn[0]));
		Xn=self.addOnes(Xn);
		mX=matrix(Xn);#m*n+1
		mY=matrix(y).T;#m*1
		print('prelims done');
		print(len(X),len(X[0]));
		test=mX.T*mX;
		print(mX);
		print(linalg.det(test));
		self.theta=(mX.T*mX).I*(mX.T*mY);		
		return ;
	
	#Predicting 		
	def predict(self,features):
		features=self.orderIncrement([features])[0];
		features=[1]+features;
		mfeatures=matrix(features);
		delta=mfeatures*self.theta;
		return delta;

