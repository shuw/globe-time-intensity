Run the following commands in the checkout directory

# Format data
Put input data in: globe/data/locations.tsv

It should be in tab seperated table with the following columns: unixTime, latitude, longitude.

Additional columns will simply be ignored.

Prepare data by running
```
python globe/prepare_data.py \
  --input=globe/data/locations.tsv \
  --minimum_count_threshold=3 \
  > globe/data/coalesced_locations.json
```

# Visualization
Start HTTP Server in 8001
```
python -m SimpleHTTPServer 8001
```

In browser, visit http://localhost:8001/globe/

Note: If you want to adjust the magnitudes of the projections, lower NORMALIZE_MAGNITUDE in globe/index.html


