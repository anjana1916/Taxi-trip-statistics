#!/usr/bin/env python
import sys
# So here we want to count how many trips a company has. Therefor the mapper processes input lines,
#  extracts the company name, and emits key-value pairs with the company as the key and a count of 1 as the value.
for line in sys.stdin:
        company, _ = line.strip().split('\t')
        print(f"{company}\t1")