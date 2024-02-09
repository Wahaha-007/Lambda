from datetime import datetime as dt
from datetime import timedelta as td
import requests
 
# We konw that file name will increase +1 every hour beforehand, then utilize this fact.

next_file = '2024-01-31-20.json.gz'
''' 
# Type I : Bookmark file todo next 

while True:
    # Read file name from bookmark (it is here until processed)
    res = requests.get(f'https://data.gharchive.org/{next_file}') # 1. Process current file
    if res.status_code != 200:
        break
    print(f'The status code for {next_file} is {res.status_code}')
    # Write file to S3
    dt_part = next_file.split('.')[0]                             # 2. Pre-process next file name
    next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%m-%d-%H') + td(hours=1), '%Y-%m-%d-%-H')}.json.gz"
    # Write next file name to bookmark
'''

# Type II : Bookmark last done file 

while True:
    # Read file name from bookmark (it is here until processed)
    dt_part = next_file.split('.')[0]                             # 1. Process next file name
    next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%m-%d-%H') + td(hours=1), '%Y-%m-%d-%-H')}.json.gz"

    res = requests.get(f'https://data.gharchive.org/{next_file}') # 1. Process current file
    if res.status_code != 200:
        break
    print(f'The status code for {next_file} is {res.status_code}')
    # Write file to S3
    # Write next file name to bookmark

