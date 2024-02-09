from datetime import datetime as dt
from datetime import timedelta as td

baseline_file = '2021-29-01-0.json.gz'


dt_part = baseline_file.split('.')[0]
# print(dt_part)


print(dt.strptime(dt_part, '%Y-%d-%m-%H') + td(hours =1)) 
print(dt.strftime(dt.strptime(dt_part, '%Y-%d-%m-%H') + td(hours =1), '%Y-%d-%m-%-H'))

# strptime is "string parse time" , e.g. String --0> Time
# strftime is reversed, e.g. Time --> String
# Print date time by stripping data from text using guided format
# The format here is of source text, not the print out format