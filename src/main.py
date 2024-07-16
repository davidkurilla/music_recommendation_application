# Music Recommendation Application System

# PAS4AI Team 2
# Josh C.
# Ema I.
# Ben K.
# David K.
# David O.

# Description: This is a Music Recommendation Application that is powered by AI.

# Imports

# Basic Modules
import numpy as np
import pandas as pd
import plotly.express as px

# AI Modules
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Import Data
data = pd.read_csv('../data/data.csv')

# KMeans Model
cluster_pipeline = Pipeline([('scaler', StandardScaler()), ('kmeans', KMeans(n_clusters=10))])
X = data.select_dtypes(np.number)
cluster_pipeline.fit(X)
data['cluster'] = cluster_pipeline.predict(X)

mood = input("Enter a mood: ")
while mood != "Quit":

    cluster = 0
    match mood:
        case "1":
            cluster = 0
        case "2":
            cluster = 1
        case "3":
            cluster = 2
        case "4":
            cluster = 3
        case "5":
            cluster = 4
        case "6":
            cluster = 5
        case "7":
            cluster = 6
        case "8":
            cluster = 7
        case "9":
            cluster = 8
        case "10":
            cluster = 9

    print(data.query(f"cluster == {cluster}")[['name', 'artists']].tail(2))

    mood = input("Enter a mood: ")
