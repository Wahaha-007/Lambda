import requests
 
def download_file(file):
  res = requests.get(f'https://data.gharchive.org/{file}')
  return res

# -- Code to test Python function locally --
# res = download_file('2021-01-29-0.json.gz')
# print(res.status_code)