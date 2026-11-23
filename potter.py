import pygame

class Potter:
    def __init__(self, x = 200, y = 405):
        self.x = x
        self.y = y
        
        self.rect = pygame.Rect(x,y, 50,50)
        
        self.current_frame = 1 #stating image for idle animation
        self.frame_timer = pygame.time.get_ticks()
        self.frame_interval = 220 #controls speed of idle
        
        self.shooting = False #so we can cast spell
        
        self.dead = False
        
        self.hurting = False
        
        self.sheild = False
        
        #these handle the spell animation using ticks 
        self.spell_frame = 1
        self.spell_timer = 0
        self.spell_speed = 250 #milisec per frame for the spell
        
        #these handle the spell animation using ticks 
        self.end_frame = 1
        self.end_timer = 0
        self.end_speed = 300 #milisec per frame for the spell
        
        self.hurt_frame = 1
        self.hurt_timer = 0
        self.hurt_speed = 250
        
        self.health = 5
        
        self.hermione = False
        self.ron = False
        self.harry = True
        
        self.updateImage()
        
    def update(self):
        self.rect.center= (self.x, self.y) #center of rect is new cords to ensure hit box is preserved

        
    def updateImage(self, pose = 1, shoot = False, hurt = False):
        
        
        if self.hermione == True:
            if self.health == 0:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\hermione_hurt"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3) #makes smaller
                
            elif shoot == True:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\hspell"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3) #makes smaller
                
            elif hurt == True:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\hermione_hurt"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3)
                
            else:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\hermione"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3) #makes smaller
            
        elif self.ron == True:
            if self.health == 0:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\ron_hurt"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3) #makes smaller
                
            elif shoot == True:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\rspell"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3) #makes smaller
                
            elif hurt == True:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\ron_hurt"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3)
                
            else:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\ron"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3) #makes smaller
                
        elif self.harry == True:
            if self.health == 0:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\potter_dead"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3) #makes smaller
                
            elif shoot == True:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\spell"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3) #makes smaller
                
            elif hurt == True:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\potter_hurt"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.3)
                
            else:
                fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\potter"+f"({pose}).png"
                self.pimage = pygame.image.load(fp) 
                self.pimage = pygame.transform.rotozoom(self.pimage, 0, 0.8) #makes smaller
        
    def draw(self, screen): #blits to screen
        screen.blit(self.pimage, self.rect) #blits onto screen
        if self.sheild == True:
            sheild_fp= r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\sheild2.png"
            simage = pygame.image.load(sheild_fp) 
            simage = pygame.transform.rotozoom(simage, 0, 0.2)
            sheild_rect = pygame.Rect(self.x -50,self.y-50, 50,50)
            screen.blit(simage, sheild_rect) 
        
    def idle(self): #animation where all the different potter pngs are cycled through
        current_tick = pygame.time.get_ticks() #looked this up but gets current tick/ simiulates current time
        
        if self.shooting:
            if current_tick - self.spell_timer >= self.spell_speed:
                self.spell_frame += 1
                self.spell_timer = current_tick
                
                if self.spell_frame >3:
                    self.shooting = False
                    self.current_frame = 1
                    self.updateImage(self.current_frame, False)
                else:
                    self.updateImage(self.spell_frame, True)
                    
        elif self.health == 0:
            if current_tick - self.end_timer >= self.end_speed:
                self.end_frame += 1
                self.spell_timer = current_tick
                
                if self.end_frame >3:
                    self.dead = True
                    #self.current_frame = 1
                    #self.updateImage(self.current_frame, False)
                else:
                    self.updateImage(self.end_frame, False, False)
                    
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
                self.current_frame = (self.current_frame % 6) +1 #loops through 1-6 so go through all the images
                self.frame_timer = current_tick #reset frame timer 
                    
            self.updateImage(self.current_frame) #actually change the potters image
        
    def shoot(self, level = 1):
        self.shooting = True
        self.spell_frame = 1
        self.spell_timer = pygame.time.get_ticks()
        self.updateImage(self.spell_frame, True)
        
    def hurt(self):
        self.hurting = True
        self.hurt_frame = 1
        self.hurt_timer = pygame.time.get_ticks()
        self.updateImage(self.hurt_frame, False, True)
        
        
        
        
        
