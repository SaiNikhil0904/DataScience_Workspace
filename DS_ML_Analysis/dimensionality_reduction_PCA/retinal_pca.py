import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
import pandas as pd
import xlrd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df=pd.read_excel("C:/Users/NIKHIL/Downloads\RetinalImagesDatasetStudents.xlsx")
print(df)

#Standardization
variables = ['MG', 'VG', 'StdG', 'MR','VarR', 'StdR', 'MH','VarH','StdH']
x = df.loc[:, variables].values
y = df.loc[:,['GnDTruth']].values
x = StandardScaler().fit_transform(x)
x = pd.DataFrame(x)
x.head()

pca = PCA()
x_pca = pca.fit_transform(x)
x_pca = pd.DataFrame(x_pca)
x_pca.head()
plt.scatter(x_pca[0], x_pca[1], alpha=.1, color='black')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
explained_variance = pca.explained_variance_ratio_
print(explained_variance)
#features = range(pca.n_components_)
#plt.bar(features, pca.explained_variance_ratio_, color='black')
#plt.xlabel('PCA features')
#plt.ylabel('variance %')
model = KMeans(n_clusters=2)
model.fit(x_pca.iloc[:,:2])
labels = model.predict(x_pca.iloc[:,:2])
plt.scatter(x_pca[0], x_pca[1], c=labels)
plt.show()

data = {"PCA_0" : x_pca[0], "PCA_1" : x_pca[1], "PCA_2" : x_pca[2], "PCA_3" : x_pca[3],"o/t" : labels, "ground_truth" : np.array(df["GnDTruth"])}
Data = pd.DataFrame(data)
print(Data)

dsa = Data[Data["ground_truth"] == 'a']
dsv = Data[Data["ground_truth"] == 'v']
plt.scatter(dsa["PCA_0"], dsa["PCA_1"], label = "Arteries(a)", c = "yellow")
plt.scatter(dsv["PCA_0"], dsv["PCA_1"], label = "Veins(v)", c = "purple")
plt.legend()

count = 0
for i in range(len(labels)):
    if labels[i] == 1:
        if df["GnDTruth"][i] != "a":
            count+=1
        else:
            continue
    else:
        if df["GnDTruth"][i] != "v":
            count+=1
        else:
            continue
Error =(count*100)/len(labels)
print("% classification rate: ",100 - Error)
print("% Error: ",Error)