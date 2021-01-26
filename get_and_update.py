import json

import requests

URL = 'https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_data'

r = requests.get(URL)

with open('vaccination_data.json', 'w') as outfile:
    json.dump(r.json(), outfile)
