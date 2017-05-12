import pandas as pd
from Word_Probab import probab
import time

start = time.clock()
print "Loading dataset at - ", time.clock()-start

X = pd.read_csv("Data_Table.csv")

print "Loaded dataset at - ", time.clock()-start
print "Current number of features - ", len(X.columns)
X = X.drop(X.columns[0], axis=1)
y = X.class_label
X = X.drop(labels=["class_label"],axis=1)
print "Beginning feature selection at - ",time.clock()-start

from sklearn.feature_selection import SelectKBest
sel = SelectKBest(k=8100)
columns = X.columns
X = sel.fit_transform(X,y)
labels = []
bool_columns = sel.get_support()
for x in range(len(columns)):
    if bool_columns[x] == True:
        labels.append(columns[x])
X = pd.DataFrame(X, columns = labels)


print "Final number of features - ",len(X.columns), " at - ",time.clock()-start

X["class_label"]=y
print "Saving new dataframe at - ", time.clock()-start
X.to_csv("Feature_Selected_Data.csv")

print "\nGenerating probability dictionaries at - ",time.clock()-start

df1 = X[X.class_label == 'Sports']
df2 = X[X.class_label == 'Tech']
df3 = X[X.class_label == 'Entertainment']

df1 = df1.drop(labels = ['class_label'], axis=1)
df2 = df2.drop(labels = ['class_label'], axis=1)
df3 = df3.drop(labels = ['class_label'], axis=1)

print "creating sports dictionary at - ",time.clock()-start

word_probab_s, min_s, max_s = probab(df1)

print "creating tech dictionary at - ",time.clock()-start

word_probab_t, min_t, max_t = probab(df2)

print "creating enter dictionary at - ",time.clock()-start

word_probab_e, min_e, max_e = probab(df3)


df1 = pd.DataFrame(word_probab_s.items())
df2 = pd.DataFrame(word_probab_t.items())
df3 = pd.DataFrame(word_probab_e.items())

#Save the dictionaries here

print "\nSaving word dictionaries at - ",time.clock()-start

df1.to_csv("Sports_Dict_feature.csv")
df2.to_csv("Tech_Dict_feature.csv")
df3.to_csv("Enter_Dict_feature.csv")