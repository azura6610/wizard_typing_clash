import pygame
import final_helpers

class Snake:
    def __init__(self, x = 800, y = 405):
        self.x = x
        self.y = y
        
        self.updateImage()
        
        self.rect = pygame.Rect(x,y, 40,40)
        
        self.current_frame = 1 #stating image for idle animation
        self.frame_timer = pygame.time.get_ticks()
        self.frame_interval = 220 #controls speed of idle
        
        self.attacking = False #so we can track attack
        self.hurting = False
        
        #these handle the attack animation using ticks 
        self.attack_frame = 1
        self.attack_timer = 0
        self.attack_speed = 250 #milisec per frame for the attack 
        
        self.hurt_frame = 1
        self.hurt_timer = 0
        self.hurt_speed = 250
        
        self.health = 5
        
        self.spell = "incantatem" #finite
        self.done = False
        
    def update(self, screen):
        if self.health == 4:
            self.spell = "serpensortia" #aguamenti
        elif self.health == 3:
            self.spell = "stupefy" #incendio
        elif self.health == 2:
            self.spell = "confundus" #flipendo
        elif self.health == 1:
            self.spell = "meteolojinx" #recanto
        else:
            spell = ""
        if self.health > 0:
            if self.done == False:
                final_helpers.write_message(screen, f"{self.spell}", self.x+40, self.y-50, 30, (255, 255, 255)) 
        self.rect.center= (self.x, self.y) #center of rect is new cords to ensure hit box is preserved

        
    def updateImage(self, pose = 1, attack = False, hurt = False):
        if hurt == True:
            fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\snake_hurt"+f"({pose}).png"
            self.pimage = pygame.image.load(fp) 
            self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.4)  #makes smaller
            
        elif attack == True:
            fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\snake_attack"+f"({pose}).png"
            self.pimage = pygame.image.load(fp) 
            self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.5) #makes smaller
        
        else:
            fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\snake"+f"({pose}).png"
            self.pimage = pygame.image.load(fp) 
            self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.5) #makes smaller

        
        
    def draw(self, screen): #blits to screen
        screen.blit(self.pimage, self.rect) #blits onto screen
        
        
    def idle(self): #animation where all the different potter pngs are cycled through
        current_tick = pygame.time.get_ticks() #looked this up but gets current tick/ simiulates current time
        
        if self.attacking:
            if current_tick - self.attack_timer >= self.attack_speed:
                self.attack_frame += 1
                self.attack_timer = current_tick
                
                if self.attack_frame >3:
                    self.attacking = False
                    self.current_frame = 1
                    self.updateImage(self.current_frame, False, False)
                else:
                    self.updateImage(self.attack_frame, True, False)
        elif self.hurting:
            if current_tick - self.hurt_timer >= self.hurt_speed:
                self.hurt_frame += 1
                self.hurt_timer = current_tick
                
                if self.hurt_frame >3:
                    self.hurting = False
                    self.current_frame = 1
                    self.updateImage(self.current_frame, False, False)
                else:
                    self.updateImage(self.hurt_frame, False, True)
        
        else:
            if current_tick - self.frame_timer >= self.frame_interval: #makes sure inside of the interval
                self.current_frame = (self.current_frame % 3) +1 #loops through 1-6 so go through all the images
                self.frame_timer = current_tick #reset frame timer 
                    
            self.updateImage(self.current_frame) #actually change the potters image
        
    def attack(self):
        self.attacking = True
        self.attack_frame = 1
        self.attack_timer = pygame.time.get_ticks()
        self.updateImage(self.attack_frame, True, False)
        
    def hurt(self):
        self.hurting = True
        self.hurt_frame = 1
        self.hurt_timer = pygame.time.get_ticks()
        self.updateImage(self.hurt_frame, False, True)
        
        
    
        
        
        
        

