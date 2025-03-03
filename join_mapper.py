#!/usr/bin/env python
import sys

# So here we are basically printing the taxi id and company id from the taxis.txt 
# and the trip id and taxi id from the trips.txt. We differentiate them based on the number of columns and while 
# printing them we also add from which text file it came from
for line in sys.stdin:
    line = line.strip()
    sec = line.split(',')
    if len(sec) == 4:  
        taxi_id, company_id = sec[0], sec[1]
        print(f"{taxi_id}\t{company_id}\ttaxi")
    elif len(sec) == 8:  
        trip_id, taxi_id = sec[0], sec[1]
        print(f"{taxi_id}\t{trip_id}\ttrip")


