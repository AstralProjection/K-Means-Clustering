import csv
import numpy as np
from collections import defaultdict

#Matplotlib for graph yo

class Point:
    coordinates = (0,0)
    distance = 0.0
    cluster = 0

def dataHelper(fileName, delimiterChar):
    columns = defaultdict(list)

    with open(fileName, newline='') as dataFile:
        data = csv.DictReader(dataFile, delimiter=delimiterChar)
        for row in data:
            for (k,v) in row.items():
                columns[k].append(v)

    return columns

def getDistance():


if __name__ == "__main__":
    data = dataHelper('data_1024.csv', '\t')

    vectors = []

    for coord in zip(data['Distance_Feature'], data['Speeding_Feature']):
        vector = Point()
        vector.coordinates = coord

        vectors.append(vector)



