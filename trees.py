import numpy as np #numerical computation
import pandas as pd #data wrangling
import matplotlib.pyplot as plt #plotting package
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.datasets import make_circles
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LogisticRegression
#Next line helps with rendering plots
import matplotlib as mpl #add'l plotting functionality
mpl.rcParams['figure.dpi'] = 400 #high res figures
import graphviz #to visualize decision trees
df = pd.read_csv('cleaned_data.csv')
features_response = df.columns.tolist()
print (features_response)
items_to_remove = ['ID', 'SEX', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5','PAY_6', 'EDUCATION_CAT', 'graduate school', 'high school','none','others', 'university']
features_response = [item for item in features_response if item not in items_to_remove]
features_response
X_train, X_test, y_train, y_test = \
train_test_split(df[features_response[:-1]].values, df['default payment next month'].values, test_size=0.2, random_state=24)
dt = tree.DecisionTreeClassifier(max_depth=2)
dt.fit(X_train, y_train)
dot_data = tree.export_graphviz(dt, out_file=None, filled=True,
rounded=True, feature_names=features_response[:-1],
proportion=True, class_names=['Not defaulted', 'Defaulted'])
graph = graphviz.Source(dot_data)
graph.render('test document',view=True)
print(graph)
#step12
features_response[:-1]
print(features_response[:-1].index('PAY_1'))
X_train.shape
sum(X_train[:,4] <= 1.5)/X_train.shape[0]
np.mean(y_train)
dt.max_depth = None
dt.fit(X_train, y_train)
pm0 = np.linspace(0.01,0.99,99)
pm1 = 1 - pm0
#print(pm0)
#print(pm1)
misclassification_rate = np.minimum(pm0, pm1)
print(misclassification_rate)
mpl.rcParams['figure.dpi'] = 400
plt.plot(pm0, misclassification_rate, label='Misclassification rate')
plt.xlabel('$p_{m0}$')
plt.legend()
#plt.show()
gini = (pm0 * (1-pm0)) + (pm1 * (1-pm1))
mpl.rcParams['figure.dpi'] = 400
plt.plot(pm0, misclassification_rate, label='Misclassification rate')
plt.plot(pm0, gini, label='Gini impurity')
plt.xlabel('$p_{m0}$')
plt.legend()
#plt.show()
cross_ent = -1*( (pm0 * np.log(pm0)) + (pm1 * np.log(pm1)) )
mpl.rcParams['figure.dpi'] = 400
plt.plot(pm0, misclassification_rate, label='Misclassification rate')
plt.plot(pm0, gini, label='Gini impurity')
plt.plot(pm0, cross_ent, label='Cross entropy')
plt.xlabel('$p_{m0}$')
plt.legend()
#plt.show()
X_circ, y_circ = make_circles(n_samples = 300, shuffle=True, noise=0.1, random_state=1, factor=0.4)
cm = plt.cm.RdBu
cm_bright = ListedColormap(['#FF0000', '#0000FF'])
ax = plt.axes()
ax.scatter(X_circ[:,0], X_circ[:,1], c=y_circ, cmap=cm_bright)
ax.set_aspect('equal')
ax.set_title('Nonlinear data for classification')
ax.set_xticks([])
ax.set_yticks([])
#plt.show()
x_min, x_max = X_circ[:, 0].min() - .5, X_circ[:, 0].max() + .5
y_min, y_max = X_circ[:, 1].min() - .5, X_circ[:, 1].max() + .5
h = 0.02
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
classifiers = [tree.DecisionTreeClassifier(max_depth=4, random_state=4),
              LogisticRegression()]
titles = ['Decision tree', 'Logistic regression']
counter = 1
for classif in classifiers:
    ax = plt.subplot(1, 2, counter)
    classif.fit(X_circ, y_circ)
    Z = classif.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:,1]
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cm, alpha=0.8)
    ax.scatter(X_circ[:,0], X_circ[:,1], c=y_circ, cmap=cm_bright)
    ax.set_aspect('equal')
    ax.set_title(titles[counter-1])
    ax.set_xticks([])
    ax.set_yticks([])
    counter+=1
plt.show()
