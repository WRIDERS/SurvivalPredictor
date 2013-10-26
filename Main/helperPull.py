from pullProcessedData import pull;
from sklearn import linear_model;
from sklearn import preprocessing;
from sklearn import cross_validation;
from sklearn import ensemble;
from sklearn import svm;
import numpy as np;
import csv;



X=pull();
X.parse();

#print(len(X.trainData),len(X.trainData[0]));
#print(len(X.testData),len(X.testData[0]));
#print(len(X.TrainXtra));
print();

TrainData=X.trainData;
TrainRes=X.TrainXtra;
TestData=X.testData;

def orderIncrement(X):
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
					temp+=[ad];
				elif(j!=k):
					if(j<k):
						pass;
						temp+=[ad];
					elif(j>k):
						pass;
						#print(j,k,len(temp),n+n*k-(k*(k+1)/2)+j);
						#temp[n+n*k-((k*(k+1))/2)+j-k-1]+=ad/2.0;
		nX+=[temp];				
	return nX;

	

oTrainData=(TrainData);
oTestData=(TestData);


	
scalar=preprocessing.Scaler().fit(oTrainData);
pTrainData=scalar.transform(oTrainData);
pTestData=scalar.transform(oTestData);



#LR1=svm.LinearSVC( C=1);
LR2=linear_model.LogisticRegression(penalty='l1', dual=False, tol=0.0001, C=100000.0, fit_intercept=True, intercept_scaling=1, class_weight=None);
LR1=ensemble.RandomForestClassifier(n_estimators=1, criterion='gini', max_depth=None, min_samples_split=1, min_samples_leaf=1, min_density=0.10000000000000001, max_features='auto', bootstrap=True, compute_importances=False, oob_score=False, n_jobs=1, random_state=0, verbose=0);
LR1.fit(pTrainData,TrainRes);
LR2.fit(pTrainData,TrainRes);
SurvivalRes1=LR1.predict_proba(pTestData);
SurvivalRes2=LR2.predict_proba(pTestData);

SurvivalResArr=SurvivalRes1*.4+SurvivalRes2*.6;
SurvivalRes=[x.index(max(x)) for x in SurvivalResArr.tolist()];

#SurvivalRes=LR2.predict(pTestData);

print(sum(SurvivalRes));




with open('../DATA/output_v2.csv','wb') as csvfile:
	csvwriter=csv.writer(csvfile,delimiter=',',quotechar='"');
	csvwriter.writerow(X.TrainHeader);
	for i in range(0,len(SurvivalRes)):
		tempo=([SurvivalRes[i]]+TestData[i]);
		csvwriter.writerow(tempo);


# Scoring code 

X=np.array(pTrainData);
Y=np.array(TrainRes);

kf=cross_validation.KFold(len(Y), k=10, indices=False);

Accuracy=[];

for train, test in kf:	
	X_train, X_test, y_train, y_test = X[train], X[test], Y[train], Y[test]
	#LR=svm.LinearSVC(C=1);
	#LR=linear_model.LogisticRegression(penalty='l1', dual=False, tol=0.0001, C=100000.0, fit_intercept=True, intercept_scaling=1, class_weight=None);
	LR=ensemble.RandomForestClassifier(n_estimators=1, criterion='gini', max_depth=None, min_samples_split=1, min_samples_leaf=1, min_density=0.10000000000000001, max_features='auto', bootstrap=True, compute_importances=False, oob_score=False, n_jobs=1, random_state=None, verbose=0);
	LR.fit(X_train,y_train);
	Accuracy+=[LR.score(X_test,y_test)];

print(Accuracy);
print(np.mean(Accuracy));	
print(np.std(Accuracy));




