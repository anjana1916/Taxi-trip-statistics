#!/usr/bin/env python
import sys
from itertools import groupby
from operator import itemgetter

# Reference : Lab practical tutorial code - week 5, __authors__ = "Vaggelis Malandrakis, KLeio Fragkedaki"

def calculate_total_distance(points, medoid):
    return sum(euclidean_distance(point, medoid) for point in points)

def euclidean_distance(point_1, point_2):
    dx = point_1[0] - point_2[0]
    dy = point_1[1] - point_2[1]
    return ((dx)**2 + (dy)**2)**0.5

#If the medoid index matches the present_medoid, add the point to the points list.
#If the medoid index changes: For the previous medoid (if it exists):Find the best medoid point among the collected points.
#The best medoid minimizes the total distance to all other points in the cluster.
#Print the coordinates of the best medoid.
#Reset for the new medoid:
#Update present_medoid to the new index.
#Clear points and add the current point.
def reduce_medoids():
    present_medoid = None
    points = [] #A list to store points belonging to the current medoid.

    for line in sys.stdin:
        medoid_index, point = line.strip().split('\t') #taking the index and points out
        x, y = map(float, point.split(','))

        if present_medoid == medoid_index: #checking if the previous medoid is the same as the medoid assigned by the mapper now, if yes we app
            points.append((x, y))
        else:
            if present_medoid is not None:
                best_medoid = min(points, key=lambda m: calculate_total_distance(points, m))
                print(f"{best_medoid[0]}\t{best_medoid[1]}")
            
            present_medoid = medoid_index
            points = [(x, y)]

    if present_medoid is not None:
        best_medoid = min(points, key=lambda m: calculate_total_distance(points, m))
        print(f"{best_medoid[0]}\t{best_medoid[1]}")

if __name__ == "__main__":
    reduce_medoids()