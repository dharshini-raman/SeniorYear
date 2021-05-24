import pandas as pd # data processing
import numpy as np # working with arrays
import matplotlib.pyplot as plt # visualization
from matplotlib import rcParams # figure size
from termcolor import colored as cl # text customization

from sklearn.tree import DecisionTreeClassifier as dtc # tree algorithm
from sklearn.model_selection import train_test_split # splitting the data
from sklearn.metrics import accuracy_score # model precision
from sklearn.tree import plot_tree # tree diagram

rcParams['figure.figsize'] = (25, 20)
df = pd.read_csv('dog5.csv')
#df = pd.read_csv('dog5.csv')
#^^for test cases too
df.to_csv('output.csv', index=False)
df.drop('Unnamed: 0', axis = 1, inplace = True)

print(cl(df.head(), attrs = ['bold']))
df.info()

print(cl(df, attrs = ['bold']))
X_var = df[['HUNTING', 'WEIGHT', 'EXERCISE', 'LIFE EXPECTANCY', 'HEIGHT']].values # independent variable
y_var = df['GROUP'].values # dependent variable

print(cl('X variable samples : {}'.format(X_var[:5]), attrs = ['bold']))
print(cl('Y variable samples : {}'.format(y_var[:5]), attrs = ['bold']))
X_train, X_test, y_train, y_test = train_test_split(X_var, y_var, test_size = 0.3, random_state = 0)

print(cl('X_train shape : {}'.format(X_train.shape), attrs = ['bold']))
print(cl('X_test shape : {}'.format(X_test.shape), attrs = ['bold'] ))
print(cl('y_train shape : {}'.format(y_train.shape), attrs = ['bold']))
print(cl('y_test shape : {}'.format(y_test.shape), attrs = ['bold']))
model = dtc(criterion = 'gini', max_depth = 7)
#model = dtc(criterion = 'gini', max_depth = 7)
#change validation here
model.fit(X_train, y_train)

pred_model = model.predict(X_test)

print(cl('Accuracy of the model is {:.0%}'.format(accuracy_score(y_test, pred_model)), attrs = ['bold']))
feature_names = df.columns[:7]
target_names = df['GROUP'].unique().tolist()

plot_tree(model, 
          feature_names = feature_names, 
          class_names = target_names, 
          filled = True, 
          rounded = True)

plt.savefig('test2') 

