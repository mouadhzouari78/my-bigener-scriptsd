import datetime
import time
import pygame
is_running = True
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S")
set_hours = input("Set hours: ")
set_minutes = input("Set minutes: ")
set_seconds = input("Set seconds: ")
set_alarm = set_hours + ":" + set_minutes + ":" + set_seconds
while is_running:
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S")
    if now == set_alarm:
        print("wake up")
        pygame.mixer.init()
        pygame.mixer.music.load("alarm.mp3.mp3")
        pygame.mixer.music.play()

        is_running = False
    else:
        print(now)
        time.sleep(1)
        print()