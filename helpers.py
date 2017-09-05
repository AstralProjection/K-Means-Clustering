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
    return float("%.2f" % round(sum(list)/float(len(list)), 3))

def listDuplicates(l): # Ugly but quick
    seen = set()
    seen2 = set()
    seen_add = seen.add
    seen2_add = seen2.add
    for i in l:
        if i in seen:
            seen2_add(i)
        else:
            seen_add(i)
    return list(seen2)

