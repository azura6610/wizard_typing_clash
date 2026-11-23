import pygame
import final_helpers

class Ghost:
    def __init__(self, x = 1200, y = 405, spell_num = 1):
        self.x = x
        self.y = y
        
        self.updateImage()
        
        self.rect = pygame.Rect(x,y, 40,40)
        
        self.current_frame = 1 #stating image for idle animation
        self.frame_timer = pygame.time.get_ticks()
        self.frame_interval = 280 #controls speed of idle
        
        self.dead = False #so we can cast spell 
        
        #these handle the spell animation using ticks 
        self.spell_frame = 1
        self.spell_timer = 0
        self.spell_speed = 250 #milisec per frame for the spell
        
        self.speed = 1.5
        
        if spell_num == 1:
            self.spell = "expelliarmus"
        elif spell_num ==2:
            self.spell = "obliviate"
        elif spell_num == 3:
            self.spell = "alohomora"
        elif spell_num ==4:
            self.spell = "wingardium"
        elif spell_num ==5:
            self.spell = "incendio"
        elif spell_num ==6:
            self.spell = "totalus"
        elif spell_num ==7:
            self.spell = "leviosa"
        elif spell_num ==8:
            self.spell = "muffliato"
        elif spell_num ==9:
            self.spell = "lapifors"
        else:
            self.spell = "petrificus"
        
        self.done = False
        
    def update(self, screen):
        
        if self.x >= 280:
            self.x -= self.speed
            self.rect.center= (self.x, self.y) #center of rect is new cords to ensure hit box is preserved
            if self.done == False:
                final_helpers.write_message(screen, f"{self.spell}", self.x+40, self.y-50, 35, (255, 255, 255)) #writes spell above head
        
            
        
    def updateImage(self, pose = 1, dead = False):
        if dead == False:
            fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\knight"+f"({pose}).png"
            self.pimage = pygame.image.load(fp)
            self.pimage = pygame.transform.flip(self.pimage, True, False)
            self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.35) #makes smaller
            
        else:
            fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\knight_hit"+f"({pose}).png"
            self.pimage = pygame.image.load(fp)
            self.pimage = pygame.transform.flip(self.pimage, True, False)
            self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3) #makes smaller
        
        
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