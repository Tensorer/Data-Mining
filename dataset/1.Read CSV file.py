import csv 
import scipy as sp
import numpy as np
import pandas as pd

features_rawdata=[] #features' list
labels_rawdata=[]   #labels' list

def openfile(file_name):  
        with open(file_name) as file_object:
                list_dataset_rows=file_object.readlines()
                for i in  list_dataset_rows:
                        i+=i.strip()
                print(list_dataset_rows)

def read_CSV(file_name):
        try:
                with open(file_name,'r') as file_object:                
                        reader_CSV=csv.reader(file_object)
                        num_lines = 0
                        for oneline in reader_CSV:
                                features_rawdata.append(oneline[0])
                                labels_rawdata.append(oneline[1])
                                num_lines += 1
        except FileNotFoundError:
                print('Cannot find the .csv file ' + file_name+'.') 
        else:
                print('The feature list is : \n\b'+str(features_rawdata)+'\n\n\n\nThe lable list is: \n\b'+str(labels_rawdata))
                print('\n\nSucceed to load the data set from '+file_name+'! The data set contains '+str(num_lines)+' samples in total.')    
                
if __name__== '__main__':
        read_CSV(file_name='labels-levela.csv')    #modify the csv file name here
    
