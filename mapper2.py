#!/usr/bin/env python

import sys
from math import sqrt
# Reference : Lab practical tutorial code - week 5, __authors__ = "Vaggelis Malandrakis, KLeio Fragkedaki"
# The mapper script reads medoid points from a file, then processes input data (trip information) from stdin. 
# For each trip, it calculates the closest medoid to the dropoff location using Euclidean distance. 
# It then outputs the medoid index and the dropoff coordinates as key-value pairs.

def get_medoids(filepath):
    medoids = []
    with open(filepath) as fp:
        for line in fp:
            x, y = map(float, line.strip().split('\t'))
            medoids.append((x, y))
    return medoids

def euclidean_distance(point_1, point_2):
    dx = point_1[0] - point_2[0]
    dy = point_1[1] - point_2[1]
    return ((dx)**2 + (dy)**2)**0.5

def map_to_medoids(medoids):
    for line in sys.stdin:
        try:
            trip_id, taxi_id, fare, distance, pickup_x, pickup_y, dropoff_x, dropoff_y = line.strip().split(',')
            dropoff = (float(dropoff_x), float(dropoff_y))
            
            min_dist = float('inf') # we initialize this to infinity to compare the first value
            closest_medoid = None
            
            for i, medoid in enumerate(medoids):
                dist = euclidean_distance(dropoff, medoid)
                if dist < min_dist:
                    min_dist = dist
                    closest_medoid = i
            
            print(f"{closest_medoid}\t{dropoff_x},{dropoff_y}")
        except ValueError:
            continue 

if __name__ == "__main__":
    medoids = get_medoids('medoid.txt')
    map_to_medoids(medoids)