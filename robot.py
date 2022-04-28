import tkinter as tk
from tkinter import *
from Maestro import Controller
import _thread
import time
import speech_recognition as sr
import vlc
import pyttsx3

MOTORS = 1
TURN = 2
BODY = 0
HEADTURN = 3
HEADTILT = 4
#dead
ELBOW = 8
###
SHOULDER = 6
SHOULDER_OUT = 7
WRIST_UP = 9
WRIST_TURN = 10
HAND = 11


class KeyControl:
    def __init__(self):
    #def __init__(self, win):
        #self.root = win
        self.tango = Controller()
        self.body = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.motors = 6000
        self.turn = 6000
        self.elbow = 6000
        self.shoulder = 6000
        self.shoulder_out = 6000
        self.wrist_up = 6000
        self.wrist_turn = 6000
        self.hand = 6000
        
        self.tango.setTarget(MOTORS, 6000)
        self.tango.setTarget(TURN, 6000)
        self.tango.setTarget(ELBOW, 6000)
        self.tango.setTarget(SHOULDER, 6000)
        self.tango.setTarget(BODY, 6000)

    ############################################
    #TODO move forward a set distance
    def moveForward(self):
        self.motors = 5100
        self.tango.setTarget(MOTORS, self.motors)
        time.sleep(1)
        self.motors = 6000
        self.tango.setTarget(MOTORS, self.motors)
        time.sleep(1)

    #TODO turn right 90
    def turnRight(self):
        self.turn = 5100
        self.tango.setTarget(TURN, self.turn)
        time.sleep(2)
        self.turn = 6000
        self.tango.setTarget(TURN, self.turn)
        time.sleep(1)

    #TODO turn left 90
    def turnLeft(self):
        self.turn = 6900
        self.tango.setTarget(TURN, self.turn)
        time.sleep(2)
        self.turn = 6000
        self.tango.setTarget(TURN, self.turn)
        time.sleep(1)

    def turnAround(self):
        self.turn = 5100
        self.tango.setTarget(TURN, self.turn)
        time.sleep(4)
        self.turn = 6000
        self.tango.setTarget(TURN, self.turn)
        time.sleep(1)

    def headTiltCommand(self):
        self.headTilt = 6700
        self.tango.setTarget(HEADTILT, self.headTilt)
        time.sleep(0.5)
        self.headTilt = 5300
        self.tango.setTarget(HEADTILT, self.headTilt)
        time.sleep(0.5)
        self.headTilt = 6000
        self.tango.setTarget(HEADTILT, self.headTilt)
        time.sleep(0.5)

    def headTurnCommand(self, direction):
        self.headTurn = int(direction)
        self.tango.setTarget(HEADTURN, self.headTurn)
        time.sleep(1)

    def armMove(self):
        self.shoulder = 6700
        self.wrist_up = 7000
        self.tango.setTarget(SHOULDER, self.shoulder)
        time.sleep(0.5)
        self.tango.setTarget(WRIST_UP, self.wrist_up)
        time.sleep(0.5)
        self.shoulder = 6000
        self.wrist_up = 6000
        self.tango.setTarget(SHOULDER, self.shoulder)
        self.tango.setTarget(WRIST_UP, self.wrist_up)
        time.sleep(1)

    #TODO have this listen and return a word
    def speechCommand(self):
        listening = True
        while listening:
            with sr.Microphone() as source:
                r = sr.Recognizer()
                r.adjust_for_ambient_noise(source)
                r.energy_threshold = 3000
                r.pause_threshold = 0.6
                r.non_speaking_duration = 0.6

                try:
                    print("listening")
                    audio = r.listen(source)
                    print("Got audio")
                    word = r.recognize_google(audio)
                    print(word)
                    #TODO North, East, South, West, Fight, Run
                    if word != "":
                        return word
                        listening = False
                    #if word.lower().find('hello') > -1:
                    #    return word
                    #    listening = False
                except sr.UnknownValueError:
                    print("Don't know that word")

    #TODO this should remain the same
    def tts(self, word):
        engine = pyttsx3.init()
        voice_num = 2

        voices = engine.getProperty('voices')
        engine.setProperty('rate', 110)
        engine.setProperty('voice', voices[voice_num].id)

        engine.say(word)
        engine.runAndWait()
