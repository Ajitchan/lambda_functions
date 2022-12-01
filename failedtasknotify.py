import json
import boto3
import requests

def lambda_handler(event, context):
    url_1 = 'https://trade.julesenergy.com/jtp/api/health/check/testapikey'
    url_2 = 'https://trading.smartestenergy.com/jtp/api/health/check/testapikey'
    url_3 = 'https://trading.flexitricity.com/jtp/api/health/check/testapikey'
    url_4 = 'https://engie-uk.julesenergy.com/jtp/api/health/check/testapikey'
    url_5 = 'https://endeal.nl/jtp/api/health/check/testapikey'
    url_6 = 'https://my.julesenergy.nl/jtp/api/health/check/testapikey'
    element = 'numberOfFailedTasks'
    
    request_1 = requests.get(url_1)
    response_1 = request_1.json()
    request_2 = requests.get(url_2)
    response_2 = request_2.json()
    request_3 = requests.get(url_3)
    response_3 = request_3.json()
    request_4 = requests.get(url_4)
    response_4 = request_4.json()
    request_5 = requests.get(url_5)
    response_5 = request_5.json()
    request_6 = requests.get(url_6)
    response_6 = request_5.json()
   
    
    if response_1[element] >= 5:
        sns_client = boto3.client("sns")
        sns_client.publish(TopicArn='arn:aws:sns:eu-west-2:072454366480:hms_failedtasks', Subject='Health Monitor System Notification', Message='Error Message: TGP Failed Task')
        return (response_1[element])
    
    
    elif response_2[element] >= 5:
        sns_client = boto3.client("sns")
        sns_client.publish(TopicArn='arn:aws:sns:eu-west-2:072454366480:hms_failedtasks', Subject='Health Monitor System Notification', Message='Error Message: Smartest Failed Task')
        return (response_2[element])
    
    elif response_3[element] >= 5:
        sns_client = boto3.client("sns")
        sns_client.publish(TopicArn='arn:aws:sns:eu-west-2:072454366480:hms_failedtasks', Subject='Health Monitor System Notification', Message='Error Message: Flexitricity Failed Task')
        return (response_3[element])
    
    
    elif response_4[element] >= 5:
        sns_client = boto3.client("sns")
        sns_client.publish(TopicArn='arn:aws:sns:eu-west-2:072454366480:hms_failedtasks', Subject='Health Monitor System Notification', Message='Error Message: Engie UK Failed Task')
        return (response_4[element])
    
    elif response_5[element] >= 5:
        sns_client = boto3.client("sns")
        sns_client.publish(TopicArn='arn:aws:sns:eu-west-2:072454366480:hms_failedtasks', Subject='Health Monitor System Notification', Message='Error Message: Engie NL Failed Task')
        return (response_5[element])

    
    elif response_6[element] >= 5:
        sns_client = boto3.client("sns")
        sns_client.publish(TopicArn='arn:aws:sns:eu-west-2:072454366480:hms_failedtasks', Subject='Health Monitor System Notification', Message='Error Message: Petawatts Failed Task')
        return (response_6[element])
    
    else:
        return 'No Failed Task'
    