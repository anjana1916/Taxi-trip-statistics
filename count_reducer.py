#!/usr/bin/env python
import sys

# The reducer aggregates the counts for each company, keeping a running total and printing the
# final count for each unique company when all inputs have been processed.
prev_company = None
trip_count = 0

for line in sys.stdin:
    company, count = line.strip().split('\t')
    count = int(count)

    if prev_company == company:
        trip_count += count
    else:
        if prev_company:
            print(f"{prev_company}\t{trip_count}")
        prev_company = company
        trip_count = count

if prev_company:
    print(f"{prev_company}\t{trip_count}")