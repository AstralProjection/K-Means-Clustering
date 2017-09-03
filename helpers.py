import csv
import math
from collections import defaultdict

def readData(fileName, delimiterChar):
    columns = defaultdict(list)

    with open(fileName, newline='') as dataFile:
        data = csv.DictReader(dataFile, delimiter=delimiterChar)
        for row in data:
            for (k,v) in row.items():
                columns[k].append(v)

    return columns


def distance(a, b):
    return math.sqrt((b.x() - a.x())**2 + (b.y() - a.y())**2)

def avg(list):
    return sum(list)/float(len(list))
