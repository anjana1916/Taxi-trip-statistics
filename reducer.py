#!/usr/bin/env python3
import sys
from collections import defaultdict

# The reducer, it takes all the sorted data from the mapper and summarizes it.
# For each combination of taxi ID and trip type, it counts how many trips there were, 
# finds the highest and lowest fares, and calculates the average fare.

class TripStats:
    def __init__(self):
        self.count = 0
        self.max_fare = float('-inf')
        self.min_fare = float('inf')
        self.total_fare = 0.0

    def update(self, fare):
        # Every time we see a new trip, we update our stats
        self.count += 1
        self.max_fare = max(self.max_fare, fare)
        self.min_fare = min(self.min_fare, fare)
        self.total_fare += fare

    @property
    def avg_fare(self):
        return self.total_fare / self.count if self.count else 0.0

# This is our big collection of stats, organized by taxi and trip type
stats = defaultdict(TripStats)

for line in sys.stdin:
    try:
        # Each line has a key (taxi_id and trip_type) and a fare
        key, fare = line.strip().split('\t')
        taxi_id, trip_type = key.split(',')
        fare = float(fare)
    except (ValueError, IndexError):
        continue  
    
    stats[key].update(fare)

for key, data in stats.items():
    taxi_id, trip_type = key.split(',')
    # We finally have our taxi_id, trip type, count, min fare, max fare and average fare
    print(f"{taxi_id},{trip_type},{data.count},{data.max_fare:.2f},{data.min_fare:.2f},{data.avg_fare:.2f}")