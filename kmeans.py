import helpers
import models
import matplotlib.pyplot as plt
import numpy as np

def assignCluster(vectors, clusters):
    for i in vectors:
        for y in clusters:
            if i.cluster is None or helpers.distance(i, y) < helpers.distance(i, i.cluster):
                i.cluster = y

    for x in vectors:
        for z in clusters:
            if x.cluster == z:
                z.vectors.append(x)

    return moveClusters(clusters)

def generateClusters(vectors, k):
    for i in np.random.randint(len(vectors), size=k):
        cluster = models.Cluster(vectors[i].coordinates, [])
        clusters.append(cluster)

    return clusters

def moveClusters(clusters):
    for i in clusters:
       i.coordinates = (helpers.avg(i.getCoordinateList(0)), helpers.avg(i.getCoordinateList(1)))

    return clusters

def graph(vectors, clusters):
    for i in vectors:
        plt.plot(i.x(), i.y(), 'ro')

    for i in clusters:
        plt.plot(i.x(), i.y(), 'bo')

    plt.show()

def iterateClusters(vectors, clusters, old=[]):
    new = assignCluster(vectors, clusters)
    iterateClusters(vectors, new, clusters)

if __name__ == "__main__":
    vectors = []
    clusters = []
    k = 7 # Number of clusters
    data = helpers.readData('data_1024.csv', '\t')

    for coord in zip(data['Distance_Feature'], data['Speeding_Feature']):
        vector = models.Point(coord, None)
        vectors.append(vector)

    clusters = generateClusters(vectors, k)


    coordList = [] # Used for detecting duplicates, once a duplicate is shown the loop will break.

    while True:
        clusters = assignCluster(vectors, clusters)

        for y in clusters:
            coordList.append(y.coordinates)
            print(str(y.coordinates) + '\n -------')

        if len(helpers.listDuplicates(coordList)) != 0:
            break

    graph(vectors, clusters)
