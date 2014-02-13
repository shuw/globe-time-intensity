import sys
import csv
import json

csvfile = open(sys.argv[1], 'r')

# Use to take in TSV and turn it into JSON for usage in index.html
#
# Example usage: python csv_to_json.py data/points > data/points.json

# Right now it takes a series of (time, latitude, longitude, intensity) rows
# Rows are expected to be bucketed by time span (i.e. one minute, 5 minutes) and pre-sorted
reader = csv.reader(csvfile, delimiter='\t')
print(json.dumps([row for row in reader]))

