import gzip
import json
with gzip.open('2015-01-01-15.json.gz', 'rb') as f:
  for line in f:
     parsed_json = json.loads(line)
     print(parsed_json['type'], parsed_json['actor']['login'], parsed_json['repo']['name'])	 	
