import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

df = pd.read_csv('training_ultrasound.csv')
df.replace('?', -99999, inplace=True)
df.fillna(-99999,inplace=True)
df.drop(['STUDYID'],1,inplace=True)
# df.drop(['SUBJID'],1,inplace=True)
df.drop(['SEX'],1,inplace=True)
df.drop(['DELIVERY'],1,inplace=True)
df.drop(['BMI'],1,inplace=True)
df.drop(['BIRTHHC'],1,inplace=True)
df.drop(['BIRTHLEN'],1,inplace=True)
df.drop(['BAZ'],1,inplace=True)
df.drop(['BHC_40'],1,inplace=True)
df.drop(['BLEN_40'],1,inplace=True)
df.drop(['BWT_40'],1,inplace=True)

# df.drop(['AGEDAYS'],1,inplace=True) # Not sure what the difference of between this and GAGEDAYS, so removed this since GAGEDAYS looks better

df['WTKG'] = df['WTKG'] * 1000
df = df[df['SEXN']==1]

X = np.array(df.drop(['WTKG'],1))
y = np.array(df['WTKG'])

print(df)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

# example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,2,2,2,3,2,1]])
# example_measures = example_measures.reshape(2, -1)
#
# prediction = clf.predict(example_measures)
# print(prediction)