import random
from datetime import datetime
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

# Melissa
from melissa.tts import tts

pygame.init()
pygame.mixer.init()

polly = boto3.Session(profile_name="default",region_name="us-east-1").client("polly");
file_name = '/Users/an0rak/Google Drive/Current Projects/Melissa-Core/melissa/'
script_name = '/Users/an0rak/Google Drive/Current Projects/Melissa-Core/melissa/script.txt'
audio_name = '/Users/an0rak/Google Drive/Current Projects/Melissa-Core/melissa/script.mp3'

WORDS = {
  'what_is_time': {'groups': ['time']},
  'what_is_date': {'groups': ['date']},
  'what_is_day': {'groups': ['day']}
}


def what_is_time(text):
    outcomes = [
        datetime.strftime(datetime.now(), '%H:%M:%S') + '! One day you\'ll get a watch...', 
        'The Time is ' + datetime.strftime(datetime.now(), '%H:%M:%S')
    ]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(outcomes))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/Current\ Projects/Melissa-Core/melissa/actions/polly.py /Users/an0rak/Google\ Drive/Current\ Projects/Melissa-Core/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # tts("The time is " + datetime.strftime(datetime.now(), '%H:%M:%S'))


def what_is_date(text):
    outcomes = [
        datetime.strftime(datetime.now(), '%m/%d/%Y') + '! One day you\'ll be at one with your calendar...', 
        'The Date is ' + datetime.strftime(datetime.now(), '%m/%d/%Y')
    ]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(outcomes))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/Current\ Projects/Melissa-Core/melissa/actions/polly.py /Users/an0rak/Google\ Drive/Current\ Projects/Melissa-Core/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # tts("The date is " + datetime.strftime(datetime.now(), '%m/%d/%Y'))


def what_is_day(text):
    outcomes = [
        datetime.strftime(datetime.now(), '%A') + '! Really Tan?  That busy?...', 
        'Today is ' + datetime.strftime(datetime.now(), '%A')
    ]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(outcomes))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/Current\ Projects/Melissa-Core/melissa/actions/polly.py /Users/an0rak/Google\ Drive/Current\ Projects/Melissa-Core/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # tts("The day is " + datetime.strftime(datetime.now(), '%A'))
