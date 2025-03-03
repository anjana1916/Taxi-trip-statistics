#!/usr/bin/env python
import sys

# Reference : Lab practical tutorial code - week 5, __authors__ = "Vaggelis Malandrakis, KLeio Fragkedaki"
#The reader script compares two sets of medoids (old and new) to check for convergence in the K-medoids clustering algorithm.
# It reads medoid coordinates from two files, compares them, and determines if the algorithm has converged based on a threshold.
# It outputs "1" if converged, "0" if not.

def get_medoids(filepath):
    medoids = []
    with open(filepath) as fp:
        for line in fp:
            x, y = map(float, line.strip().split('\t'))
            medoids.append((x, y))
    return medoids

def check_convergence(old_medoids, new_medoids, threshold=0.001):
    if len(old_medoids) != len(new_medoids):
        return False
    
    for old, new in zip(old_medoids, new_medoids):
        if abs(old[0] - new[0]) > threshold or abs(old[1] - new[1]) > threshold:
            return False
    return True

if __name__ == "__main__":
    old_medoids = get_medoids('medoid.txt')
    new_medoids = get_medoids('new_medoids.txt')
    
    if check_convergence(old_medoids, new_medoids):
        print("1")  # equal to 1 means Converged, this is passed to our run.sh
    else:
        print("0")  # equal to 0 means Not converged, this is passed to our run.sh