import helpers
import models
import matplotlib.pyplot as plt
import numpy as np

def assignCluster(vectors, clusters):
    for i in vectors:
        for y in clusters:
            if i.cluster is None or helpers.distance(i, y) < helpers.distance(i, i.cluster):
                i.cluster = y
                y.vectors.append(i)


def generateClusters(vectors, k):
    clusters = []

    for i in np.random.randint(len(vectors), size=k):
        cluster = models.Cluster(vectors[i].coordinates, [])
        clusters.append(cluster)

    return clusters

def moveClusters(vectors, clusters):
    for i in clusters:
       i.coordinates = (helpers.avg(i.getCoordinateList(0)), helpers.avg(i.getCoordinateList(1)))

def graph(vectors, clusters):
    for i in vectors:
        plt.plot(i.x(), i.y(), 'ro')

    for i in clusters:
        plt.plot(i.x(), i.y(), 'bo')

    plt.show()

if __name__ == "__main__":
    k = 4 # Number of clusters
    print("Reading data file")
    data = helpers.readData('data_1024.csv', '\t')

    vectors = []

    for coord in zip(data['Distance_Feature'], data['Speeding_Feature']):
        vector = models.Point(coord, None)
        vectors.append(vector)

    print("Generating clusters")
    clusters = generateClusters(vectors, k)
    print("Assigning clusters")
    assignCluster(vectors, clusters)
    print("Moving....")
    moveClusters(vectors, clusters)
    graph(vectors, clusters)
