import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
import pandas as pd
import xlrd
DATA=pd.read_excel("RetinalImagesDatasetStudents.xlsx")
print("Data: ")
print(DATA)
kmeans = KMeans(n_clusters=2)
kmeans.fit(DATA)
import numpy
ARRAY = numpy.array(DATA)
print("Data to array: ")
print(ARRAY)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print("Centroids: ")
print(centroids)
print("Lables: ")
print(labels)
colors = ["c.","y."]

for i in range(len(ARRAY)):
    #print("coordinate:",arr[i], "label:", labels[i])
    plt.plot(ARRAY[i][0], ARRAY[i][1], colors[labels[i]], markersize = 10)
    plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
plt.show()
#print("label:", labels[i])

dp = pd.read_excel("RetinalImagesDatasetStudents-1.xlsx")
dp
dp["MyTruth"]=labels
count = 0
for i in range(len(labels)):
    if labels[i] == 1:
        if dp["GNDTRUTH"][i] != "a":
            count+=1
        else:
            continue
    else:
        if dp["GNDTRUTH"][i] != "v":
            count+=1
        else:
            continue
Error =(count*100)/len(labels)
print("Error: ",Error)
print("Effectiveness: ",100 - Error)
dp.to_excel("Final.xlsx",sheet_name='sheet1',index=False)