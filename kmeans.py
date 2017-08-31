import models
import matplotlib.pyplot as plt
import csv
import numpy as np
from collections import defaultdict

#Matplotlib for graph yo


def dataHelper(fileName, delimiterChar):
    columns = defaultdict(list)

    with open(fileName, newline='') as dataFile:
        data = csv.DictReader(dataFile, delimiter=delimiterChar)
        for row in data:
            for (k,v) in row.items():
                columns[k].append(v)

    return columns

def getDistance(a, b):
    return np.linalg.norm(a-b) # Euclidean

def generateClusters(vectors, k):
    clusters = []

    for i in np.random.randint(len(vectors), size=k):
        cluster = models.Cluster(vectors[i].coordinates, (0,0))
        clusters.append(cluster)

    return clusters

if __name__ == "__main__":
    k = 4 # Number of clusters

    data = dataHelper('data_1024.csv', '\t')

    vectors = []

    for coord in zip(data['Distance_Feature'], data['Speeding_Feature']):
        vector = models.Point(coord, 0)
        vectors.append(vector)

    plt.plot(data['Distance_Feature'], data['Speeding_Feature'], 'ro')

    for i in generateClusters(vectors, k):
        plt.plot(i.x(), i.y(), 'bo')

    plt.show()
