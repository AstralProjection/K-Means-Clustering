class Point:
    def __init__(self, coordinates, cluster):
        self.coordinates = coordinates
        self.cluster = cluster

class Cluster:
    def __init__(self, coordinates, vectors):
        self.coordinates = coordinates
        self.vectors = vectors

    def x(self):
        return self.coordinates[0]

    def y(self):
        return self.coordinates[1]
