import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

df = pd.read_csv("Data_Table.csv")
df = df.drop(df.columns[0], axis=1)
y = np.load("y_train.npy")
df['label'] = y
y = df.label
y = df.label
df = df.drop(labels=['label'],axis=1)

from sklearn.feature_selection import SelectKBest
sel = SelectKBest(k=3)
df = pd.DataFrame(sel.fit_transform(df,y))

df["class_label"]=y
df.columns=['col1', 'col2', 'col3', 'class_label']
  
df0 = df[df.class_label==0]
df1 = df[df.class_label==1]
df2 = df[df.class_label==2]
df3 = df[df.class_label==3]
df4 = df[df.class_label==4]
df5 = df[df.class_label==5]
df6 = df[df.class_label==6]
df7 = df[df.class_label==7]
df8 = df[df.class_label==8]
df9 = df[df.class_label==9]

fig = pylab.figure()
ax = Axes3D(fig)
colors = iter(cm.rainbow(np.linspace(0, 1, 10)))
ax.scatter(df0.col1, df0.col2, df0.col3, c=next(colors), label="0")
ax.scatter(df1.col1, df1.col2, df1.col3, c=next(colors), label="1")
ax.scatter(df2.col1, df2.col2, df2.col3, c=next(colors), label="2")
ax.scatter(df3.col1, df3.col2, df3.col3, c=next(colors), label="3")
ax.scatter(df4.col1, df4.col2, df4.col3, c=next(colors), label="4")
ax.scatter(df5.col1, df5.col2, df5.col3, c=next(colors), label="5")
ax.scatter(df6.col1, df6.col2, df6.col3, c=next(colors), label="6")
ax.scatter(df7.col1, df7.col2, df7.col3, c=next(colors), label="7")
ax.scatter(df8.col1, df8.col2, df8.col3, c=next(colors), label="8")
ax.scatter(df9.col1, df9.col2, df9.col3, c=next(colors), label="9")

plt.show()