#helpers will be here
import pygame

TS = 50

WIDTH = 22*TS #x goes from 0 to 1100
HEIGHT = 12*TS #y goes from 0 to 600
SIZE = (WIDTH, HEIGHT)

pygame.init()  #initializes a pygame object so that we can use font and noise -> looked this up
pygame.mixer.init() #lets us get noise

def background(fp, transform = 1.0):
    background_image = pygame.image.load(fp) #load welcome background image for later
    background_image = pygame.transform.rotozoom(background_image, 0, transform)
    return background_image


def write_message(screen, message, x , y , size = 100, color = (255, 255, 0)): #method to write on the screen 
    font_fn = r"HarryP-MVZ6w.ttf" #file with font on it 
    font = pygame.font.Font(font_fn, size) #pulls font from file name
    text_surface = font.render(message, True, color) #gets font ready to go on screen
    
    text_rect = text_surface.get_rect() #rect for text 
    text_rect.center= (x,y)
    
    shadow_rect = text_surface.get_rect() #rect for text 
    shadow_rect.center= (x+3,y+3)
    
    shadow = font.render(message, True, (45,20,10))
    screen.blit(shadow, shadow_rect)
    screen.blit(text_surface,text_rect) #blits font at center
    
    
def make_noise(file = 'bonk.mp3'): #uses the mixer from pygame to play sound when method called
    bonk_sound = pygame.mixer.Sound(file)
    bonk_sound.play()
    
def make_heart():
    heart_fp = r"C:\Users\m296240\Documents\EW200_AY27\Final project\final_proj_images\full_heart.png"
    heart = pygame.image.load(heart_fp)
    heart = pygame.transform.rotozoom(heart, 0, 0.03)
    return heart

def displayGameOver(screen, SIZE): #game over screen so can call at end of game
    bg = pygame.Surface(SIZE)
    red = (225,0,0)
    bg.fill(red)
    screen.blit(bg)
    
def get_level_background(level, screen, score): #works but makes game too slow
    lvl_fp = f"background_lvl({level}).jpg"
    level_screen = background(lvl_fp, 1.1)
    screen.blit(level_screen, (0,0))
    write_message(screen, f"Level {level}", 50, 20, 40, (218, 165, 32)) 
    write_message(screen, "Score", 40, 55, 40, (218, 165, 32))
    if abs(score) < 100:
        write_message(screen, f"{score}", 94, 55, 40, (218, 165, 32))
    elif abs(score) >= 100 and abs(score) < 1000:
        write_message(screen, f"{score}", 108, 55, 40, (218, 165, 32))
    elif abs(score) >=1000 and abs(score) < 10000:
        write_message(screen, f"{score}", 110, 55, 40, (218, 165, 32))
    else:
        write_message(screen, f"{score}", 120, 55, 40, (218, 165, 32))
            
            
    write_message(screen, f"Press 1 for How to Play!", 550, 580, 30, (218, 165, 32))
    
def load_level_assets(current_level):
    info_img =background(f"{current_level}info.jpg", 0.39)
    info_img = pygame.transform.scale(info_img, (WIDTH, HEIGHT))

    lvl_up = [background(f"{current_level}levelup_screen({i}).jpg", 0.4) for i in (1, 2, 3)]
    lvl_bg = background(f"background_lvl({current_level}).jpg", 1.1)

    return info_img, lvl_up, lvl_bg #if have 3 vars like a,b,c =method() will assign them respectively