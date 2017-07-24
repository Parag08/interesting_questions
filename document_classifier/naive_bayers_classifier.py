from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier
import csv
import numpy as np
import linecache
import pandas as pd

traincsv = np.loadtxt ('../3.training_data/Training_Data.csv',skiprows=1, delimiter=",",dtype={'names':('documentID','category'),'formats':('S30','i4')})
testcsv = np.genfromtxt ('../4.test_data/Test_Data.csv' ,skip_header =1,delimiter=",",dtype=[('documentID','S30'),('category','i4')])
#datacsv = np.genfromtxt ('./2.document_set/document_set.csv',skip_header =1, delimiter=",")
documentTrainer = Trainer(tokenizer)

documentSet = []

def getTextBasedOnDocumentID(documentID):
  ID = int(documentID.split('_')[1])
  line = linecache.getline('../2.document_set/document_set.csv', ID + 2)
  text = line.split(',"')[1]
  return text

for i in range(0,len(traincsv)):
  documentSet.append({'text':getTextBasedOnDocumentID(traincsv[i][0]),'category': traincsv[i][1]})

for documents in documentSet:
  documentTrainer.train(documents['text'], documents['category'])

newsClassifier = Classifier(documentTrainer.data, tokenizer)

for i in range(0,len(testcsv)):
  data = getTextBasedOnDocumentID(testcsv[i][0])
  classification = newsClassifier.classify(data)
  testcsv[i][1] = int(classification[0][0])
df = pd.DataFrame(testcsv)
df.to_csv("../5.evaluation_file/predicted_cat.csv",index=False)
#np.savetxt("./5.evaluation_file/predicted_cat.csv", testcsv,header="document_id,category" ,delimiter=",")
