"""
Created on Sat May 14 09:31:26 2022

@author: brobe
"""
# -*- coding: utf-8 -*-
 
import os
import shutil
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


# We will check if the Virus Family Directory exists
#if it is not there,  then we will create a folder 
#with the same name 
thisdir="C://Users//brobe//Downloads//
malware-classification//train//pngFiles"
updir="C://Users//brobe//Downloads//
malware-classification//train"

Y=pd.read_csv("C://Users//brobe//Downloads//
malware-classification//trainLabels.csv")
total = len(Y)*1.
print('total ', total)
ax=sns.countplot(x="Class", data=Y)
source = 'pngFiles'
print('ax ', ax)
files=os.listdir(updir+'/'+source)
print('files ', files)
filenames=Y['Id'].tolist()
print('filenames ', filenames)
class_y=Y['Class'].tolist()
print('class_y ', class_y)
class_label=[]
class_png=[]
fnames=[]

for file in files:
# split the file name at '_' and take the first 
# and last part 
    
   file=file.split('_')[1] 
   file=file.split('.')[0]
   print('file ', file)
   if any(file == filename for filename in
       filenames): 
       i=filenames.index(file)
       print('i ', i)
       class_png.append(class_y[i])
       print('class_png ', class_png)
       if  class_y[i].__ne__(None) :
          print('class_y[i] ',class_y[i] )
          if not os.path.isdir(updir+'/'+
              class_y[i]):
             os.makedirs(updir+'/'+class_y[i])
          shutil.move(updir+'//'+source + '//' + 
            'VirusShare_' + file+'.png',updir+'/'
               +class_y[i] )
      
       fnames.append(file)
    
