import pandas as pd
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D

X = pd.read_csv("Feature_Selected_Data.csv")
X = X.drop(X.columns[0], axis=1)
y = X.class_label
X = X.drop(labels=["class_label"],axis=1)

from sklearn.feature_selection import SelectKBest
sel = SelectKBest(k=3)
df = pd.DataFrame(sel.fit_transform(X,y))

df["class_label"]=y
df.columns=['col1', 'col2', 'col3', 'class_label']

print "\nCreating scatter plot"

fig = pylab.figure()
ax = Axes3D(fig)

df1 = df[df.class_label == 'Sports']
df2 = df[df.class_label == 'Tech']
df3 = df[df.class_label == 'Entertainment']

ax.scatter(df1.col1, df1.col2, df1.col3, c='b', label='Sports')
ax.scatter(df2.col1, df2.col2, df2.col3, c='r', label='Tech')
ax.scatter(df3.col1, df3.col2, df3.col3, c='g', label='Entertainment')

plt.show()