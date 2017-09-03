class Point:
    def __init__(self, coordinates, cluster):
        self.coordinates = coordinates
        self.cluster = cluster

    def x(self):
        return float(self.coordinates[0])

    def y(self):
        return float(self.coordinates[1])

class Cluster:
    def __init__(self, coordinates, vectors):
        self.coordinates = coordinates
        self.vectors = vectors

    def x(self):
        return float(self.coordinates[0])

    def y(self):
        return float(self.coordinates[1])

    def getCoordinateList(self, coord): # 0 for X coord, 1 for Y coord
        list = []

        for i in self.vectors:
            list.append(float(i.coordinates[coord]))

        return list
