import pandas as pd
import numpy as np
import re
import csv

def filter(tweet_text):
		tweet_text_list=[]
		for content in tweet_text:
				content = content.lower()
				content=re.sub(r"[^A-Za-z0-9(),!?@&\'\`\"\_\n]"," ",content)
				content=re.sub(r"@user"," ",content)
				content=re.sub(r"what's","what is",content)
				content=re.sub(r"\'s"," ",content)
				content=re.sub(r"can't","can not",content)
				content=re.sub(r"n't"," not",content)
				content=re.sub(r"i'm","i am",content)
				content=re.sub(r"\'re"," are",content)
				content=re.sub(r"\'d","would",content)
				content=re.sub(r"\'ll","will",content)
				content=content.replace('&',' and')
				content=content.replace('@',' at')
				tweet_text_list.append(content)
		return tweet_text_list
train_set=pd.read_csv('./olid-training-v1.0.tsv',sep='\t')
test_set=pd.read_csv('./testset-levelc.tsv',sep='\t')
train_set["clean_tweet"]=filter(train_set['tweet'])
test_set["clean_tweet"]=filter(test_set['tweet'])
test_set.to_csv('cleaned_testset-levelc.csv')
