from datetime import datetime as dt
from datetime import timedelta as td
import requests
 
# We konw that file name will increase +1 every hour beforehand, then utilize this fact.

next_file = '2024-01-31-20.json.gz'
 
while True:
    res = requests.get(f'https://data.gharchive.org/{next_file}') # 1. Process current file
    if res.status_code != 200:
        break
    print(f'The status code for {next_file} is {res.status_code}')
    dt_part = next_file.split('.')[0]                             # 2. Pre-process next file name
    next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%m-%d-%H') + td(hours=1), '%Y-%m-%d-%-H')}.json.gz"