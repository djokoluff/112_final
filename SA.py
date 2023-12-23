import random 
from LineBot_basic import read_message, send_mesage, main

ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = 'class.iottalk.tw' # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'linebot007'
IDF_list = ['linebot_str_i']
ODF_list = ['linebot_str_o']
device_id = '1234567' #if None, device_id = MAC address
device_name = 'web'
exec_interval = 1  # IDF/ODF interval

import requests, json
api_url = "http://127.0.0.1:8089/get_baby_state" # url to call api for getting baby state

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def linebot_str_i():
    message = read_message()
    response = requests.get(api_url)
    response = response.json()["state"]
    if response:
        return message
    else:
        return None 

def linebot_str_o(data:list):
    print(data[0])
    return data
