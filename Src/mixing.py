import pygame as pygame
import time

pygame.mixer.init(frequency=22050,size=-16,channels=4)  #customize
sound1 = pygame.mixer.Sound('test.wav')  #first sound channel
sound2 = pygame.mixer.Sound('radiostören.wav')  #second sound channel
chan1 = pygame.mixer.find_channel()  #queue first channel
chan1.queue(sound1)  #play first sound in found channel
chan2 = pygame.mixer.find_channel()  #find next channel
chan2.queue(sound2)  #play second sound in found channel
time.sleep(10)
