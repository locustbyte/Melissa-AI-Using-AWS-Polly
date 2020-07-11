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

# Melissa
from melissa import profile
from melissa.tts import tts

pygame.init()
pygame.mixer.init()

audio = 'script.mp3'

polly = boto3.Session(profile_name="default",region_name="us-east-1").client("polly");
file_name = '/Users/an0rak/Google Drive/github/Melissa-AI-Using-AWS-Polly/melissa/'
script_name = '/Users/an0rak/Google Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt'
audio_name = '/Users/an0rak/Google Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.mp3'

# output = os.path.join(audio_name)
# file = open(output, "wb")





WORDS = {'who_are_you': {'groups': [['who', 'are', 'you']]},
         'toss_coin': {'groups': [['heads', 'tails'],
                                  ['toss', 'coin'], ['flip', 'coin']]},
         'how_am_i': {'groups': [['how', 'i', 'look'], ['how', 'am', 'i']]},
         'who_am_i': {'groups': [['who', 'am', 'i']]},
         'where_born': {'groups': [['where', 'born']]},
         'how_are_you': {'groups': [['how', 'are', 'you']]},
         'are_you_up': {'groups': [['you', 'up']]},
         'love_you': {'groups': [['love', 'you']]},
         'open_Chrome': {'groups': [['open', 'Chrome']]},
         'marry_me': {'groups': [['marry', 'me']]},
         'undefined': {'groups': []}}


def who_are_you(text):
    va_name = profile.data['va_name']
    messages = ['I am ' + va_name + ', your lovely personal assistant.',
                va_name + ', didnt I tell you before?',
                'You ask that so many times! I am ' + va_name]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n" + random.choice(messages))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # tts(random.choice(messages))


def toss_coin(text):
    outcomes = ['heads', 'tails']
    print file_name + '/here'

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\nI just flipped a coin. It shows " + random.choice(outcomes))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def how_am_i(text):
    replies_how = [
        'You are goddamn handsome!',
        'My knees go weak when I see you.',
        'You are sexy!',
        'You look like the kindest person that I have met.'
    ]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(replies_how))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


    # tts(random.choice(replies))


def who_am_i(text):
    replies_who = [
        'Voice recognition detects Tan.  Howeer, should I enable camera for facial recognition?',
        'Are we doing this?  It\'s you Tan.'
    ]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(replies_who))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def where_born(text):
    tts('I was created by a magician named Tanay, in India, '
        'the magical land of himalayas.')


def how_are_you(text):
    replies = [
        'Hi, i am good, how about you?',
        'Good, how are you?'
    ]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(replies))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def are_you_up(text):
    replies = [
        'Go On...',
        'What you thinking about?',
        'I can be!  What are you thinking about?',
        'I can be!  What do you need?'
    ]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(replies))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def love_you(text):
    replies = [
        'I love you too.',
        'Dude, You\'re looking for love in the wrong place.'
    ]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(replies))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def open_Chrome(text):
    replies_chrome = [
               'Sure.',
               'Don\'t do anything stupid!.'
              ]
    
    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(replies_chrome))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    url = 'http://www.google.com/'
    chrome_path = 'open -a /Applications/Google\ Chrome.app'
    # open -a '/Applications/Google\ Chrome.app'
    webbrowser.get(chrome_path).open(url)

    


def marry_me(text):

    replies = [
        'Getting funnier every day',
        'You couldn\t afford a diamond big enough'
    ]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(replies))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # tts('I have been receiving a lot of marriage proposals recently.')


def undefined(text):
    replies = [
        'Come on... I don\'t know what that means',
        'So... Were you whispering?',
        'You\'re going to have to either speak up a bit or be more specific'
    ]

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+random.choice(replies))
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-AI-Using-AWS-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # tts(random.choice(replies))