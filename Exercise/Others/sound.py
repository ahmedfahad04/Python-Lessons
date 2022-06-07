import pygame

import datetime
import time

hour = "23"
min = "37"
timer = f"{hour}:{min}"

#dt = datetime.today()
#newdatetime = dt.replace(hour=11, minute=10)
#print(newdatetime)
current_time = datetime.datetime.now()

pygame.mixer.init()
# Loading and playing a sound effect:
pygame.mixer.music.load('alarm.mp3')
pygame.mixer.music.play()


while True:
	now = current_time.strftime("%H:%M")
	print(now)

	if timer == now:
		print("OK!")
		
	print("Press 'p' to pause, 'r' to resume")
	print("Press 'e' to exit the program")
	query = input("  ")
	  
	if query == 'p':
  
		# Pausing the music
		pygame.mixer.music.pause()     
	elif query == 'r':
  
		# Resuming the music
		pygame.mixer.music.unpause()
	elif query == 'e':
  
		# Stop the mixer
		pygame.mixer.music.stop()
		break
