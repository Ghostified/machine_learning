# %%
#Data Visualization
#Multivariate Plots
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


# %%
#load  datasets
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length','petal-width', 'class']
dataset=read_csv(url, names=names)

# %%
#multivariate: INteractions between variables 
# Scatter plots 
scatter_matrix(dataset)
plt.show()