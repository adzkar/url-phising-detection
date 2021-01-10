from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import numpy as np 
import pandas as pd

data = pd.read_excel('Detection.xlsx')

print('5 Data Pertama')
print(data.head())

training_set, test_set = train_test_split(data, test_size = 0.2, random_state = 1)
X = data.iloc[:,1:11].values
Y = data.iloc[:,11].values

X_train = training_set.iloc[:,1:11].values
Y_train = training_set.iloc[:,11].values
X_test = test_set.iloc[:,1:11].values
Y_test = test_set.iloc[:,11].values

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train,Y_train)

Y_pred = classifier.predict(X_test)
test_set["Predictions"] = Y_pred

print('Hasil Learning')
print(confusion_matrix(Y_test,Y_pred.round()))
print(classification_report(Y_test,Y_pred.round()))
print(accuracy_score(Y_test, Y_pred.round()))