# To register more APIs create a function which calls the joke API and
# append the function name to the jokeAPIRegister list. Which is used to
# randomly select one of the APIs

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

import requests
import json


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




# Melissa
from melissa.tts import tts

WORDS = {'tell_joke': {'groups': [['tell', 'joke']]}}


def chuck_norris():
    while (True):
        req = requests.get('http://api.icndb.com/jokes/random')
        json_joke = json.loads(req.text)['value']
        if json_joke[u'categories'] != u'explicit':
            return json_joke[u'joke']


def in_house():
    jokes = [
        'What happens to a frogs car when it breaks down? It gets toad away.',
        'Why was six scared of seven? Because seven ate nine.',
        'Why are mountains so funny? Because they are hill areas.',
        'Have you ever tried to eat a clock?'
        'I hear it is very time consuming.',
        'What happened when the wheel was invented? A revolution.',
        'What do you call a fake noodle? An impasta!',
        'Did you hear about that new broom? It is sweeping the nation!',
        'What is heavy forward but not backward? Ton.',
        'No, I always forget the punch line.'
    ]
    return random.choice(jokes)


jokeAPIRegister = [chuck_norris, in_house]


def tell_joke(text):

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n" + random.choice(jokeAPIRegister)())
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/Current\ Projects/Melissa-Core/melissa/actions/polly.py /Users/an0rak/Google\ Drive/Current\ Projects/Melissa-Core/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # tts(random.choice(jokeAPIRegister)())
