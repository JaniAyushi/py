# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y0ZAOl4Er72pIgZiXHdZRazUyWXQiupy
"""

import pandas as pd

cancer = pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Cancer.csv')

cancer.head()
cancer.info()
cancer.describe()

cancer.columns

y = cancer['diagnosis']

x = cancer.drop(['id','diagnosis','Unnamed: 32'],axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=2529)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=2000)

model.fit(x_train, y_train)

model.intercept_

model.coef_

y_pred = model.predict(x_test)

y_pred

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

confusion_matrix(y_test,y_pred)

accuracy_score(y_test,y_pred)

print(classification_report(y_test,y_pred))