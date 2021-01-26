import csv
import json

state_population_sums = {}
state_population_totals = {}

with open('sc-est2019-agesex-civ.csv') as population_file:
    reader = csv.DictReader(population_file)

    for row in reader:
        if row['NAME'] == 'United States':
            continue
        if int(row['SEX']) != 0:
            continue
        if int(row['AGE']) < 16:
            continue
        if int(row['AGE']) == 999:
            state_population_totals[row['NAME']] = int(row['POPEST2019_CIV'])
            continue
        state_population_sums.setdefault(row['NAME'], 0)
        state_population_sums[row['NAME']] += int(row['POPEST2019_CIV'])

with open('state_pops_16.json', 'w') as out_json:
    json.dump(state_population_sums, out_json)
