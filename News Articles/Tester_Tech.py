from Tokenizer_Test import tokenize
import pandas as pd
from Article_Probab import art_probab
import time

sport = 0
tech = 0
enter = 0

df = pd.read_csv('Feature_Selected_Data.csv')
df = df.drop(df.columns[0], axis=1)

df1 = df[df.class_label == 'Sports']
df2 = df[df.class_label == 'Tech']
df3 = df[df.class_label == 'Entertainment']

df1 = df1.drop(labels = ['class_label'], axis=1)
df2 = df2.drop(labels = ['class_label'], axis=1)
df3 = df3.drop(labels = ['class_label'], axis=1)

#Calculate probabilities for Sports, Tech and Entertainment label by reading the saved dictionaries
    
word_probab_s = pd.read_csv("Sports_Dict_feature.csv")
word_probab_s = word_probab_s.drop(word_probab_s.columns[0], axis=1)
word_probab_s = word_probab_s.drop(df.index[0], axis=0)
word_probab_s = word_probab_s.set_index('0').to_dict()
word_probab_s = word_probab_s['1']
word_probab_t = pd.read_csv("Tech_Dict_feature.csv")
word_probab_t = word_probab_t.drop(word_probab_t.columns[0], axis=1)
word_probab_t = word_probab_t.drop(df.index[0], axis=0)
word_probab_t = word_probab_t.set_index('0').to_dict()
word_probab_t = word_probab_t['1']
word_probab_e = pd.read_csv("Enter_Dict_feature.csv")
word_probab_e = word_probab_e.drop(word_probab_e.columns[0], axis=1)
word_probab_e = word_probab_e.drop(df.index[0], axis=0)
word_probab_e = word_probab_e.set_index('0').to_dict()
word_probab_e = word_probab_e['1']

avg = 0

for i in range(900):
    start = time.clock()
    print "Article number " + str(i)
    file_name = "Tech_Test/Tech" + str(i) + ".txt"
    tokens = tokenize(file_name)
    print "Number of tokens - " + str(len(tokens))
    
    prob_s = art_probab(df, df1, word_probab_s, 1, tokens)
    prob_t = art_probab(df, df2, word_probab_t, 1, tokens)
    prob_e = art_probab(df, df3, word_probab_e, 1, tokens)
    
    if prob_s > prob_t:
        if prob_s > prob_e:
            sport += 1
            avg += prob_s
        else:
            enter += 1
            avg += prob_e
    elif prob_t > prob_e:
        tech += 1
    else:
        enter += 1
        avg += prob_e
        
    print "Sports - ",sport
    print "Tech - ",tech
    print "Enter - ",enter
    print "Time taken - ", time.clock() - start

print "Average P - ", float(float(avg)/(sport+enter))