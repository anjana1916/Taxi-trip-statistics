#!/usr/bin/env python3
import sys

# The mapper here helps us sort out taxi trips into different categories. We go through each line and skip the ones whose length less than 4.
# then we check if it's a short, medium, or long trip based on the distance, and then organizes this information by taxi ID and trip type.

#This function is to classify the trip
def classify_trip(distance):
    if distance >= 200:
        return 'long'
    elif distance >= 100:
        return 'medium'
    return 'short'

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) < 4:
        continue  # skip malformed lines
    # We're interested in who drove, how much it cost, and how far they went
    taxi_id, fare, distance = parts[1:4]
    try:
        fare = float(fare)
        distance = float(distance)
    except ValueError:
        continue  # skip lines with non-numeric fare or distance
    
    #Here we pass teh distance to get the trip type
    trip_type = classify_trip(distance)
    
   
    print(f"{taxi_id},{trip_type}\t{fare}")