
# coding: utf-8

# In[13]:

#2.1 Import libraries
#load libraries
import pandas
import sklearn
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# In[7]:

# 2.2 Load dataset
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
url = open('flowers.txt','r')
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)


# In[8]:

#3.1 Dimension of Dataset
#shape
print(dataset.shape)
#(150,5)


# In[9]:

#3.2 Peek at the Data
#head
print(dataset.head(20))


# In[10]:

#3.3 Statistical Summary

#descriptions
print(dataset.describe())


# In[11]:

#3.4 Class Distribution

#class distribution
print(dataset.groupby('class').size())


# In[14]:

# 4.Data Visualization
#4.1 Univariate Plots
#box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()


# In[15]:

# we can also create a histogram of each input variable to get an idea of the distribution
# histogram
dataset.hist()
plt.show()


# In[16]:

#4.2 Multivariate plots
scatter_matrix(dataset)
plt.show()


# In[ ]:

# 5 Evaluate Some Algorithms
# 5.1 Create a Validation DataSet


# In[17]:

# split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7 
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X,Y,test_size=validation_size,random_state=seed)


# In[ ]:

#5.2 Test Harness


# In[18]:

# test options and evaluations metric
seed = 7
scoring = 'accuracy'


# In[19]:

#5.3 Build Models
# spot check algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results =[]
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10,random_state=seed)
    cv_results = model_selection.cross_val_score(model,X_train,Y_train,cv=kfold,scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name,cv_results.mean(), cv_results.std())
    print(msg)


# In[ ]:

# 5.4 select best model
# we can see that it looks like KNN has the largest estimated accuracy score.


# In[20]:

# compare algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()


# In[21]:

# make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train,Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation,predictions))
print(confusion_matrix(Y_validation,predictions))
print(classification_report(Y_validation,predictions))


# In[ ]:


