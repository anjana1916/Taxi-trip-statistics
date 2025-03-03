#!/usr/bin/env python
import sys

# Here we are sorting and matching for taxi trips.
# It takes in a jumbled mix of information about taxis and their trips.
# As it goes through this information, it groups everything related to a single taxi together.
# When it has all the info for one taxi – which includes the taxi's company and all its trips – it pairs up each trip with the company name

pre_taxi = None
comp = None
trips = []

for line in sys.stdin:
    taxi_id, value, record_type = line.strip().split('\t')

    if pre_taxi != taxi_id:
        if pre_taxi and comp and trips:
            for trip in trips:
                print(f"{comp}\t{trip}")
        pre_taxi = taxi_id
        comp = None
        trips = []

    if record_type == 'taxi':
        comp = value
    elif record_type == 'trip':
        trips.append(value)

if pre_taxi and comp and trips:
    for trip in trips:
        print(f"{comp}\t{trip}")

