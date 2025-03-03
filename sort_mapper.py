#!/usr/bin/env python
import sys

# The mapper here takes input lines containing company names and counts, 
# then outputs the count (padded to 10 digits) as the key and the company name as the value,
#  effectively preparing the data for sorting by count
for line in sys.stdin:
    company, count = line.strip().split('\t')
    print(f"{int(count):010d}\t{company}")