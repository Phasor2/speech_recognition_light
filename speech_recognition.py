# !/usr/bin/env python
#import pdb
# debug
# pdb.set_trace()
import rospy
from std_msgs.msg import String
import speech_recognition as sr
# import argparse
# import uuid
# import os

# import dialogflow_v2 as dialogflow
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/myturtlebot/Downloads/Robotic-5595bb2b581d.json'
# project_id = 'robotic-223705'
# session_id = str(uuid.uuid4())
# language_code='en-US'
r = sr.Recognizer()
m = sr.Microphone()

# prepare the microphone
try:
    print("A moment of silence, please...")
    while True:
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        print("Say something!")
        with m as source:
            audio = r.listen(source)
        print("Got it! Now to recognize it...")
        value = "r"
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            print(value)
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        # pos = 0
        # pos = value.find("done")
        # if pos:
        #     pass
