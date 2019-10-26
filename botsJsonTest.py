import json
import gzip

jsonfilename ='C:\\Users\\tyler\\s3.amazonaws.com\\botsdataset\\botsv1\\botsv1.json.gz'

with gzip.GzipFile(jsonfilename, 'r') as fin:
    json_bytes = fin.read()

json_str = json_bytes.decode('utf-8')
data = json.loads(json_str)
