# code for sentiment analysis

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


def getSentiments(text):
    blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    print(blob.sentiment)


training_data = [('it is good 1', 'pos'), ('it is good 3', 'pos'),
                 ('it is good 2', 'pos'), ('it is good 4', 'pos')]

txt2 = 'Service robot implementation a theoretical framework and research agenda'
txt1 = 'He is really hateful hateful hateful'

getSentiments(txt2)
getSentiments(txt1)
