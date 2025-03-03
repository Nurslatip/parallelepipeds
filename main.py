from utils.functions import process
from utils.statistics import stats
import json
with open('parallelepipeds.json', 'r') as file:
    parallelepipeds = json.load(file)

from time import sleep

pict_list = ['MY FIRST SCRIPT\n\n',
              '    *********',
              '   *       **',
              '  *       * *',
              ' *********  *',
              ' *       *  *',
              ' *       *  *',
              ' *       * *',
              ' *********',
             '\n\nI LOVE PYTHON']
for i in pict_list:
    sleep(.4)
    print(i)
print('')
print('')
print('')


#writing a cycle:
characteristics = {}
for key, val in parallelepipeds.items():
    a, b, c = int(val['a']), int(val['b']),int(val['c'])

    characteristics[key] = process(a, b, c)


with open('characteristics.json','w') as json_file:
    json.dump(characteristics, json_file, indent=4)


statistics = stats(parallelepipeds)
with open('statistics.json', 'w') as json_f:
    json.dump(statistics, json_f, indent=4)

# ___ Load files:
with open('outputs/characteristics.json','w') as json_file:
    json.dump(characteristics, json_file, indent=4)

with open('outputs/statistics.json', 'w') as json_f:
    json.dump(statistics, json_f, indent=4)

print('-----------------------------------------------------------------------------------------------')
print('You can see average characteristics of parallelepipeds below:')
print('-----------------------------------------------------------------------------------------------')


print(json.dumps(statistics, indent=4))
print('')
print('')
print('')
print('-----------------------------------------------------------------------------------------------')
print('We have created two files called: characteristics.json and statistics.json!')
print('-----------------------------------------------------------------------------------------------')

