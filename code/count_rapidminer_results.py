import pandas as pd 

#df = pd.read_csv('svm_results.csv',  encoding="ISO-8859-1",sep=',', delimiter=None, header='infer',names=None, index_col=None, usecols=None)
#df.iloc[:,[18302,18303,18304,18305,18306,18307,18308]].to_csv('svm_results_filtered.csv')
#df.astype(bool).sum(axis=0).to_csv('count_svm_results.csv')
df.loc[df['prediction(sentiment)'] == 'positive'].astype(bool).sum(axis=0).to_csv('count_svm_pos_results.csv')
df.loc[df['prediction(sentiment)'] == 'negative'].astype(bool).sum(axis=0).to_csv('count_svm_neg_results.csv')

df = pd.read_csv('nb_results.csv',  encoding="ISO-8859-1",sep=',', delimiter=None, header='infer',names=None, index_col=None, usecols=None)
df.astype(bool).sum(axis=0).to_csv('nb_results.csv')
df.iloc[:,[18302,18303,18304,18305,18306,18307,18308]].to_csv('nb_results_filtered.csv')
df.loc[df['prediction(sentiment)'] == 'positive'].astype(bool).sum(axis=0).to_csv('count_nb_pos_results.csv')
df.loc[df['prediction(sentiment)'] == 'negative'].astype(bool).sum(axis=0).to_csv('count_nb_neg_results.csv')

#time to apply nb model Rapid miner 11 minutes
