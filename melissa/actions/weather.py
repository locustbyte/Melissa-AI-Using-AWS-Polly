import random
import webbrowser
import boto3
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing

import os
import sys
import subprocess
from tempfile import gettempdir
import pygame

import pywapi


import requests
wjdata = requests.get('http://api.weatherapi.com/v1/current.json?key=754137ea593f41d28d525548200807&q=TW7 4RJ').json()
#print wjdata['data']['current_condition'][0]['temp_C']
print wjdata['location']['name']



# Melissa
from melissa import profile
from melissa.tts import tts

pygame.init()
pygame.mixer.init()

audio = 'script.mp3'

polly = boto3.Session(profile_name="default",region_name="us-east-1").client("polly");
file_name = '/Users/an0rak/Google Drive/Current Projects/Melissa-Core/melissa/'
script_name = '/Users/an0rak/Google Drive/Current Projects/Melissa-Core/melissa/script.txt'
audio_name = '/Users/an0rak/Google Drive/Current Projects/Melissa-Core/melissa/script.mp3'

WORDS = {'weather': {'groups': ['weather', ['how', 'weather'],
                                ['hows', 'weather']]}}


def weather(text):
    # weather_com_result = pywapi.get_weather_from_weather_com(
    #     profile.data['city_code'])

    # current_conditions = weather_com_result['current_conditions']
    # temperature = float(current_conditions['temperature'])
    # degrees_type = 'celcius'

    # if profile.data['degrees'] == 'fahrenheit':
    #     temperature = (temperature * 9 / 5) + 32
    #     degrees_type = 'fahrenheit'

    # weather_result = "Weather.com says: It is " + \
    #     weather_com_result['current_conditions']['text'].lower() + \
    #     " and " + str(temperature) + "degrees " + degrees_type + \
    #     " now in " + profile.data['city_name']


    
    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n The weather in '" + wjdata['location']['name'] + " is showing as ")
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/Current\ Projects/Melissa-Core/melissa/actions/polly.py /Users/an0rak/Google\ Drive/Current\ Projects/Melissa-Core/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


    # tts(weather_result)
