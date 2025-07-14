#%%
#load  liblaries 
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

#%%
#load  datasets
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length','petal-width', 'class']
dataset  = read_csv(url, names=names)

#%%
# Dimensions of the dataset 
#peek at the data 
print(dataset.head(20))

#%%
#statistical summary 
#data descriptions: count, min , max , mean
print()
print('statistical summary: ')
print(dataset.describe())

#%%
#class distribution
#It shows the number of rows that belong to each class as an absolute count
print()
print(dataset.groupby('class').size())
