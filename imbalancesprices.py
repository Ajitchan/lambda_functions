from urllib.request import urlopen
import json


def lambda_handler(event, context):
    url = event['url']
    element = event['element']
    element_1 = event['element_1']
    element_2 = event['element_2']
    response = urlopen(url)
    data_json = json.loads(response.read())

    if data_json[element] < 1:
        data_json[element] = None
    else:
        data_json[element] = 'Error: Power Short Term Imbalance Prices are missing'
        
    if data_json[element_1] < 1:
        data_json[element_1] = None
    else:
        data_json[element_1] = 'Error: GAS Imbalance Prices are missing'
        
        
    if data_json[element_2] < 1:
        data_json[element_2] = None
    else:
        data_json[element_2] = 'Error: Power Imbalance Prices are missing'
    
 
        
        
    return data_json[element],data_json[element_1], data_json[element_2]
        