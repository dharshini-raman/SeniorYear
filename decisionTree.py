import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics

from sklearn.tree import export_graphviz
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import randint
data = pd.read_csv('covtype.csv')
##data.head()
##data.info()
X = data.drop('Cover_Type', axis=1)
y = data['Cover_Type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
labels = ['Spruce/Fir', 'Lodgepole Pine', 'Ponderosa Pine',
'Cottonwood/Willow', 'Aspen', 'Douglas-fir', 'Krummholz']
y_train.index = [labels[i-1] for i in y_train]
y_train.index.value_counts()
##works till here
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train,
test_size=0.2)
clf = DecisionTreeClassifier()
cross_val_score(clf, X_train, y_train, cv=7)
clf.fit(X_train, y_train)
print(metrics.accuracy_score(y_valid, clf.predict(X_valid)))
clf.feature_importances_
def sortSecond(val):
    return val[1]
values = clf.feature_importances_
features = list(X)
importances = [(features[i], values[i]) for i in range(len(features))]
importances.sort(reverse=True, key=sortSecond)
importances
print ('All features:', X_train.memory_usage(index=True).sum()/1000000)
print ('Top 15 features:', X_train[[col[0] for col in
importances[:15]]].memory_usage(index=True).sum()/1000000)
X_train = X_train[[col[0] for col in importances[:15]]]
X_valid = X_valid[[col[0] for col in importances[:15]]]
cut_clf = DecisionTreeClassifier()
cut_clf.fit(X_train, y_train)
print(metrics.accuracy_score(y_valid, cut_clf.predict(X_valid)))
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
max_features=None, max_leaf_nodes=None,
min_impurity_decrease=0.0, min_impurity_split=None,
min_samples_leaf=1, min_samples_split=2,
min_weight_fraction_leaf=0.0, presort=False,
random_state=None, splitter='best')
params_dist = {
'criterion': ['gini', 'entropy'],
'max_depth': randint(low=4, high=40),
'max_leaf_nodes': randint(low=1000, high=20000),
'min_samples_leaf': randint(low=20, high=100),
'min_samples_split': randint(low=40, high=200)
}
best_tuned_clf = random_search.best_estimator_
print(metrics.accuracy_score(y_valid, best.predict(X_valid)))
print(metrics.classification_report(y_test, cut_clf.predict(X_test[[col[0] for col
in importances[:15]]])))
print(metrics.classification_report(y_test, best_tuned_clf.predict(X_test[[col[0]
for col in importances[:15]]])))
export_graphviz(
cut_clf,
out_file='forest.dot',
feature_names=list(X_train),
class_names=labels,
rounded=True,
filled=True
)
