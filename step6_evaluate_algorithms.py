#Algorithm validation
# load  liblaries 
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm  import SVC
from sklearn.naive_bayes import GaussianNB


# %%
#load  datasets
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length','petal-width', 'class']
dataset=read_csv(url, names=names)

# %%
#Split - out validation dataset
# data is split into 80 -20 
array = dataset.values
X = array[:, 0:4]
y = array [:, 4]
X_train, X_validation , Y_train , Y_validation = train_test_split(X, y, test_size=0.20, random_state= 1)

# %%
#build and evaluate  models 
#spot check algorithms
models = []
#models.append(('LR', LogisticRegression(solver='liblinear',multi_class='ovr')))
models.append(('LR',LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NV',GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# %%
#evaluate each model in turn 
results = []
names = []
for name , model in models:
  kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
  cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
  results.append(cv_results)
  names.append(name)
  print('%s: %f (%f)' %(name, cv_results.mean(), cv_results.std()))
# %%
