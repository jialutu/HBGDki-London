import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_csv('ads.csv')
df.replace('?', -99999, inplace=True)
df.fillna(-99999,inplace=True)
df.drop(['STUDYID'],1,inplace=True)
#df.drop(['SUBJID'],1,inplace=True)
df.drop(['SEX'],1,inplace=True)
df.drop(['FEEDING'],1,inplace=True)
df.drop(['MMARIT'],1,inplace=True)
df.drop(['BMI'],1,inplace=True)

print(df.head())

# X = np.array(df.drop(['class'],1))
# y = np.array(df['class'])
#
# X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)
#
# clf = neighbors.KNeighborsClassifier()
# clf.fit(X_train, y_train)
#
# accuracy = clf.score(X_test, y_test)
# print(accuracy)
#
# example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,2,2,2,3,2,1]])
# example_measures = example_measures.reshape(2, -1)
#
# prediction = clf.predict(example_measures)
# print(prediction)