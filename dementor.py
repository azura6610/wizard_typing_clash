import pygame
import final_helpers
from math import radians, sin, cos, atan2

class Dementor:
    def __init__(self, x = 1200, y = 405, speed = 2):
        self.x = x
        self.y = y
        
        self.updateImage()
        
        self.rect = pygame.Rect(x,y, 70,100)
        
        self.current_frame = 1 #stating image for idle animation
        self.frame_timer = pygame.time.get_ticks()
        self.frame_interval = 280 #controls speed of idle
        
        self.dead = False #so we can cast spell 
        
        #these handle the spell animation using ticks 
        self.spell_frame = 1
        self.spell_timer = 0
        self.spell_speed = 250 #milisec per frame for the spell
        
        self.speed =  speed
        
        self.done = False
        
        self.harryx = 200
        self.harryy = 405
        
        self.changex = self.harryx - self.x
        self.changey = self.harryy - self.y
        
        self.angle = atan2(self.changey, self.changex)
        #rad = radians(self.angle)
        #initialize values
        
    def update(self, screen):
        #self.speed += 0.02 #always increasing speed slowly but no player controls
        
        #rad = radians(self.angle) #convet deg into rads
        self.x += self.speed * cos(self.angle) #want angle
        self.y += self.speed * sin(self.angle)  # subtract for Pygame Y axis
        
        self.rect.center= (self.x, self.y) #updates rect too 
        
            
        
    def updateImage(self, pose = 1, dead = False):
        if self.x > 240:
            if dead == False:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\dement"+f"({pose}).png"
                self.pimage = pygame.image.load(fp)
                #self.pimage = pygame.transform.flip(self.pimage, False, False)
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.2) #makes smaller
                
            else:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\dement_hurt"+f"({pose}).png"
                self.pimage = pygame.image.load(fp)
                #self.pimage = pygame.transform.flip(self.pimage, False, False)
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.2) #makes smaller
        else:
            if dead == False:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\dement"+f"({pose}).png"
                self.pimage = pygame.image.load(fp)
                self.pimage = pygame.transform.flip(self.pimage, True, False)
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.2) #makes smaller
                
            else:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\dement_hurt"+f"({pose}).png"
                self.pimage = pygame.image.load(fp)
                self.pimage = pygame.transform.flip(self.pimage, True, False)
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.2) #makes smaller
        
    def draw(self, screen): #blits to screen
        screen.blit(self.pimage, self.rect) #blits onto screen
        
        
    def idle(self): #animation where all the different potter pngs are cycled through
        current_tick = pygame.time.get_ticks() #looked this up but gets current tick/ simiulates current time
        
        if self.dead:
            self.speed = 0 
            if current_tick - self.spell_timer >= self.spell_speed:
                self.spell_frame += 1
                self.spell_timer = current_tick
                
                if self.spell_frame >3:
                    self.done = True
                else:
                    self.updateImage(self.spell_frame, True)
                    
                
        
        else:
            if current_tick - self.frame_timer >= self.frame_interval: #makes sure inside of the interval
                self.current_frame = (self.current_frame % 3) +1 #loops through 1-6 so go through all the images
                self.frame_timer = current_tick #reset frame timer 
                    
            self.updateImage(self.current_frame) #actually change the potters image
        
    def die(self, level = 1):
        self.dead = True
        self.spell_frame = 1
        self.spell_timer = pygame.time.get_ticks()
        self.updateImage(self.spell_frame, True)