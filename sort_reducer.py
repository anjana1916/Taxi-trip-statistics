#!/usr/bin/env python
import sys

# The reducer receives the sorted input, reverses the key-value pair back to the original
# format with the company name first, and outputs the results, thus completing the sorting process by count in descending order.
# Hadoop actually performs the sorting automatically between the map and reduce phases. 
for line in sys.stdin:
    count, company = line.strip().split('\t')
    print(f"{company}\t{int(count)}")