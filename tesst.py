import datetime
import time
import pygame
hours = input("give hours:")
minutes = input("give minutes:")
seconds = input("give seconds:")
alarm_time = hours+":"+minutes+":"+seconds
sound = "alarm.mp3.mp3"
is_ready = True
while is_ready:
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S")
    if now == alarm_time:
        print("wake up gng")
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        is_ready = False
    else:
        print (now)
        time.sleep(1)
