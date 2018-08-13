import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

data =pd.read_csv('mushrooms.csv')
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
for col in data.columns:
    data[col]=labelencoder.fit_transform(data[col])
y=data['class']
X=data.drop('class',axis=1)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,random_state=0)
columns=X_train.columns

from sklearn.preprocessing import StandardScaler
ss_X =StandardScaler()
ss_y =StandardScaler()
X_train=ss_X.fit_transform(X_train)
X_test=ss_X.fit_transform(X_test)

from sklearn.tree import DecisionTreeClassifier
model_tree=DecisionTreeClassifier()
model_tree.fit(X_train,y_train)

y_prob=model_tree.predict_proba(X_test)[:,1]
y_pred=np.where(y_prob>0.5,1,0)
model_tree.score(X_test,y_pred)

#可视化树图
data_=pd.read_csv("mushrooms.csv")
data_feature_name=data_.columns[1:]
data_target_name=np.unique(data_['class'])

import graphviz
import pydotplus
from sklearn import tree
from IPython.display import Image
import os

os.environ['PATH']+= os.pathsep
dot_tree=tree.export_graphviz(model_tree,out_file=None,feature_names=data_feature_name,class_names=data_target_name,filled=True,special_characters=True)
graph=pydotplus.graph_from_dot_data(dot_tree)
img=Image(graph.create_png())
graph.write_png('out.png')