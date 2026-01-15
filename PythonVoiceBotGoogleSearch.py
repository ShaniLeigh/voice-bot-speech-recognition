# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 08:45:51 2025
VoiceBotSearchSR
@author: Shannon Leigh Comeaux
"""

import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print(f'Heard command: {command}')

                    if "search" in command:
                        search_query = command.split("search")[-1].strip()
                        driver = webdriver.Chrome()
                        driver.get("https://www.google.com")
                        search_box = driver.find_element("name", "q")
                        search_box.send_keys(search_query)
                        search_box.send_keys(Keys.RETURN)
            except sr.UnknownValueError:
                print("Sorry, I did not catch that.")
            except Exception as e:
                print(f"An error occurred: {e}")


listener = Voice()

# %%

import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print(f'Heard command: {command}')

                    if "search" in command:
                        search_query = command.split("search")[-1].strip()
                        driver = webdriver.Chrome()
                        driver.get("https://www.google.com")
                        search_box = driver.find_element("name", "q")
                        search_box.send_keys(search_query)
                        search_box.send_keys(Keys.RETURN)

                    elif "stop listening" in command:
                        print("Stopping...")
                        break

            except sr.UnknownValueError:
                print("Sorry, I did not catch that.")
            except Exception as e:
                print(f"An error occurred: {e}")


listener = Voice()
'''
### Key Updates:
- Added a condition to check if the command contains "stop listening".
- If the command is "stop listening", the loop breaks, and the program stops listening.

'''

