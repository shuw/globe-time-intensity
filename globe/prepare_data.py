import sys
import csv
import json
import optparse
import collections

parser = optparse.OptionParser()
parser.add_option(
  '-i', '--input', dest='input_file',
  help='input file name',
  default='globe/data/locations.tsv',
)
parser.add_option(
  '-c', '--coalesce_time_interval', type='int', dest='coalesce_time_interval',
  help='Interval (seconds) to coalesce points into. Expected input to be time sorted',
  default=60*5,
)
parser.add_option(
  '-t', '--minimum_count_threshold', type='int', dest='minimum_count_threshold',
  help='Removes points with magnitudes below threshold. Makes rendering performance better',
  default=1,
)

(options, args) = parser.parse_args()

time_cursor = 0

coalesced_points = collections.defaultdict(int)

reader = csv.reader(open(options.input_file, 'r'), delimiter='\t')
first_element = True
print('[')
for row in reader:
  time = int(row[0])
  latitude = float(row[1])
  longitude = float(row[2])

  coalesced_points[str(latitude) + ',' + str(longitude)] += 1

  if time > time_cursor + options.coalesce_time_interval:
    if len(coalesced_points) > 0:
      output_points = []
      for location, count in coalesced_points.items():
        if count >= options.minimum_count_threshold:
          [latitude, longitude] = location.split(',')
          output_points.append(float(latitude))
          output_points.append(float(longitude))
          output_points.append(count) 

      if not first_element:
        print(','),

      print([time, output_points])
      first_element = False

    time_cursor = time
    coalesced_points = collections.defaultdict(int)

print(']')

