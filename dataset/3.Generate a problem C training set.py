import pandas as pd
import numpy as np
import re
import csv

train_set=pd.read_csv('./olid-training-v1.0.tsv',sep='\t')
	
list_drop_index=[]

for index,value in enumerate(train_set['subtask_c']):
		if type(value) != str:
				list_drop_index.append(index)





train_set=train_set.drop(labels=list_drop_index, axis=0)
train_set.to_csv('Qc_olid-training-v1.0.tsv', index=False ,sep='\t')

