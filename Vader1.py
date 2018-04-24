#Vader1.py -- Matthew Johnston
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

sent = input("Review a movie! ")

sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sent)
score = (ss['compound']+1)*5.0

print("IMDB Score: " + str(score) + "/10.")
