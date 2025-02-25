import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import numpy as np
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
DATA["Output(Y_means)"] = y_kmeans
DATA["MyTruth"] = label
DATA["Prediction"] = ['True' if label[i] == df1["GNDTRUTH"][i] else 'False' for i in range(0, len(label))]
DATA.to_excel("FINAL.xlsx",sheet_name='sheet1',index=False)
Error =(count*100)/len(labels)
print("Error: ",Error)
print("Effectiveness: ",100 - Error)


dp.to_excel("Final.xlsx",sheet_name='sheet1',index=False)


matrix = confusion_matrix(df1['GNDTRUTH'], label)
print(matrix)


tp, fn, fp, tn = matrix.reshape(-1);
print("True positive: {} False negative:{}, False Positive:{}, True Negative:{}".format(tp, fn, fp, tn))


plt.imshow(matrix, cmap='Blues')
for (i, j), z in np.ndenumerate(matrix):
    plt.text(j, i, z)
plt.xlabel("kmeans label")
plt.ylabel("truth label")
plt.show()


print("Senstivity: {}".format(tp / (tp + fn)))
print("Specificity: {}".format(tn / (tn + fp)))
print("Precision: {}".format(tp / (tp + fp)))
print("Recall: {}".format(tp / (tp + fn)))