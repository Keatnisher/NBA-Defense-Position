# Import packages
import re
import glob
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import Sci-Kit Learn
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from cluster import kmeans, agglom, find_best_cluster, feature_importance, plot_cluster

path1 = 'PosMerge_3.csv'

data = pd.read_csv(path1)

data = data.drop(data[data.MIN < 15].index)
data = data.drop(['GP', 'MIN'], axis=1)
data['6FREQ'] = data['6FREQ'].str.replace('\%', '')
data['15FREQ'] = data['15FREQ'].str.replace('\%', '')


X = data.drop(['id', 'POS', 'PLAYER'], axis=1)
Y = data['POS']

X = X.reset_index()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#perform PCA to find performance
pca = PCA(n_components=2)
pca.fit(X_scaled)

#measure performance
X_pca = pca.transform(X_scaled)
print("Cumulative Explained Variance:", pca.explained_variance_ratio_.sum())

#perform LDA for 2 axes, measure performance
LDA = LinearDiscriminantAnalysis(n_components=2, shrinkage='auto', solver='eigen')
LDA_reduced_df = LDA.fit(X_scaled,Y).transform(X_scaled)

print(LDA.score(X_scaled,Y))

#find all silhouette scores from 5-20
find_best_cluster("kmeans",LDA_reduced_df,5,20)

#perform kmeans on chosen K
kmeans = kmeans(LDA_reduced_df, 5)

# Assign labels
data['Cluster'] = kmeans['labels']

# Print silhouette score
print("silhouette score:", kmeans['silhouette_score'])

# Target labels
y = kmeans['labels']
df = pd.DataFrame({'X1':LDA_reduced_df[:,0],'X2':LDA_reduced_df[:,1], 'labels':y})

#plot the kmeans on given K
print("Now Clustering")
plot_cluster(LDA_reduced_df, "kmeans", k_clusters=5, plot_title="""K-Means Clustering on NBA Players in 2017-18""")


print(data.head())

#target the cluster
mask = (data['Cluster'] == 4)
data[mask][['PLAYER']].head()

cluster_data = data[mask].drop(['PLAYER', 'POS', 'Cluster', 'id'], axis=1)
league_data = data.drop(['PLAYER', 'POS', 'Cluster', 'id'], axis=1)

#perform PCA on given cluster to find highest discriminative features
print("Now performing PCA")
featureImportance = feature_importance(cluster_data, league_data, 23).reset_index().drop('index', axis=1)

#save fi to file
featureImportance.to_csv('fi_4.csv')


player_list = list(data['PLAYER'])
playerid_list = list(data['id'])

df['PLAYER'] = player_list
df['id'] = playerid_list

#determine class labels, titles found from feature importance above
df['labels'] = df['labels'].map({0: 'Ball-Handler Defender',
                                 1: 'Versatile Big',
                                 2: 'Perimeter Defender',
                                 3: 'Rim Protector',
                                 4: 'Versatile Wing'})

#For Seven Clusters
# =============================================================================
# df['labels'] = df['labels'].map({0: 'Rebounder?',
#                                  1: 'Longboi Perimeter D',
#                                  2: 'Perimeter D',
#                                  3: 'Versatile Defender',
#                                  4: 'Rim Protector'})
# =============================================================================
                                 #5: 'Ball Handler',
                                 #6: 'Mobile PF',})

print(df.head())

file1_loc = '5positions.csv'

df.to_csv(file1_loc)
