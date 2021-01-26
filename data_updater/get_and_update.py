from pprint import pprint
import requests

URL = 'https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_data'

r = requests.get(URL)

results = r.json()['vaccination_data']
for result in results:
    try:
        print(result['LongName'], int(result['Admin_Per_100K'])/100_0, '%')
    except KeyError:
        pass
