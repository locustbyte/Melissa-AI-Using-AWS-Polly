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

import datetime
import psutil

import time

# Melissa
from melissa import profile
from melissa.tts import tts

pygame.init()
pygame.mixer.init()

audio = 'script.mp3'

polly = boto3.Session(profile_name="default",region_name="us-east-1").client("polly");
file_name = '/Users/an0rak/Google Drive/github/Melissa-With-Polly/melissa/'
script_name = '/Users/an0rak/Google Drive/github/Melissa-With-Polly/melissa/script.txt'
audio_name = '/Users/an0rak/Google Drive/github/Melissa-With-Polly/melissa/script.mp3'


WORDS = {
    'system_status': {
        'groups': [
            ['how', 'systems'],
            ['how', 'system'],
            'status'
        ]
    },
    'system_uptime': {
        'groups': ['uptime']
    }
}


def system_status(text):
    varOSName = os.name
    varOSVersion = os.version
    print varOS
    # os, name, version, _, _, _ = os.uname()
    # version = version.split('-')[0]
    # cores = psutil.cpu_count()
    # cpu_percent = psutil.cpu_percent()
    # memory_percent = psutil.virtual_memory()[2]
    # disk_usage = psutil.disk_usage('/')
    # disk_percent = disk_usage.percent
    response = "I am currently running on " + varOSVersion.split('-')[0] + "\n"
    # response = "I am currently running on %s version %s. " % (os, version) + "\n"
    # response += "This system is named %s and has %s CPU cores. " \
        # % (name, cores) + "\n"
    # response += "Current CPU utilization is %s percent. " % cpu_percent + "\n"
    # response += "Current memory utilization is %s percent. " % memory_percent + "\n"
    # response += "Current disk utilization is %s percent. " % disk_percent + "\n"


    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+response)
    f.close()

    # subprocess.call("/Users/an0rak/Google\ Drive/github/Melissa-With-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-With-Polly/melissa/script.txt", shell=True)

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-With-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-With-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # tts(response)


def system_uptime(text):
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    running_since = boot_time.strftime("%A %d. %B %Y")
    response = 'System has been running since ' + running_since

    f = open(file_name + "script.txt", "w")
    f.write("{Salli}\n"+response)
    f.close()

    os.system('python /Users/an0rak/Google\ Drive/github/Melissa-With-Polly/melissa/actions/polly.py /Users/an0rak/Google\ Drive/github/Melissa-With-Polly/melissa/script.txt')

    audio = file_name+'script.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # tts(response)
