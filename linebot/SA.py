import random 
from LineBot_basic import read_message, send_mesage, main

ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = 'class.iottalk.tw' # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'linebot007'
IDF_list = ['linebot_json_i']
ODF_list = ['linebot_json_o']
device_id = '12345678910' #if None, device_id = MAC address
device_name = 'linebot'
exec_interval = 1  # IDF/ODF interval

import requests, json
api_url = "http://127.0.0.1:8089/get_baby_state" # url to call api for getting baby state

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def linebot_json_i():
    message = read_message() # (userid, msg)
    response = requests.get(api_url)
    response = response.json()["state"]
    if response: # baby is crying
        selected_music = "babyshark.mp3" # select music name from 's3'
        if message:
            print("user_id: ", message[0], "\nmusic: ", selected_music)
            return {"user_id": message[0], "selected_music": selected_music}
        return None
    else:
        return None 

def linebot_json_o(data:list):
    print("data: ", data[0]) # {"user_id": message[0], "selected_music": selected_music}
    api_url = "http://127.0.0.1:8089/play_music" # url to call for playing music
    selected_music = data[0]["selected_music"]
    try:
        response = requests.post(api_url, json={'music_name': selected_music})
        if response.status_code == 200:
            print(f'Music {selected_music} play request sent successfully.')
        else:
            print('Failed to send music play request.')
    except Exception as e:
        print(f'Error: {e}')

    send_mesage(data[0]["user_id"], f"您的寶寶在哭泣! 正在為您撥放音樂: {selected_music}") # send notify to parent's line through linebot
