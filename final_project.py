#final project
import pygame 
import final_helpers
from potter import Potter
from ghost import Ghost
from snake import Snake
from dementor import Dementor
from voldemort import Voldemort
import random

filename = "typing_scores.txt"

#set up screen size
TS = 50

WIDTH = 22*TS #x goes from 0 to 1100
HEIGHT = 12*TS #y goes from 0 to 600
SIZE = (WIDTH, HEIGHT)

#music needs to be initialized from pygame and will always play music in the background
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Harry_Potter_-_Theme_Song_(mp3.pm).mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

inloop = True

while inloop:
    
    for e in pygame.event.get():
                    
        if e.type == pygame.QUIT:
            pygame.quit()
            inloop = 0 #exits game and playing loop
            
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #start with black screen

    level = 6
    


    #initial background image
    welcome_fps= [r"welcome(1).jpg", r"welcome(2).jpg", r"welcome(3).jpg" ]   #different file path for each frame bc each saved as jpg 
    welcome_images = [final_helpers.background(welcome_fps[0], 0.4), final_helpers.background(welcome_fps[1], 0.4), final_helpers.background(welcome_fps[2], 0.4)] #background method called 3 times using each fp
    
    info_image, levelup_images, level_screen = final_helpers.load_level_assets(level)

    #initial score
    score = 0

    #initialize harry potter
    harry = Potter()
    snake = Snake()
    voldemort = Voldemort()
    ghosts = []
    dements = []
    hearts = []
    snake_hearts = []
    vold_hearts = []
    for i in range(1,6): #makes 5 hearts for harry 
        heart=final_helpers.make_heart()
        hearts.append(heart)
       
    for i in range(1,6): #makes 5 hearts for the snake 
        heart=final_helpers.make_heart()
        snake_hearts.append(heart)
        
    for i in range(1,8): #makes 7 hearts for the voldemort 
        heart=final_helpers.make_heart()
        vold_hearts.append(heart)

    rand_time = random.randint(4,7)
    rand_time2 = random.randint(1000,2000)
    
    SPAWN_GHOST_EVENT = pygame.USEREVENT + 1
    SNAKE_ATTACK_EVENT = pygame.USEREVENT + 2 #the +2 makes it a different event id
    SPAWN_DEMENT_EVENT = pygame.USEREVENT + 3
    VOLD_ATTACK_EVENT = pygame.USEREVENT + 4
    pygame.time.set_timer(SPAWN_GHOST_EVENT, rand_time*1000) # make ghosts only appear every 3 secs
    pygame.time.set_timer(SNAKE_ATTACK_EVENT, 10000) #snake attack every 10 seconds
    pygame.time.set_timer(SPAWN_DEMENT_EVENT, rand_time2) # make ghosts only appear every 3 secs
    pygame.time.set_timer(VOLD_ATTACK_EVENT, 7000) #voldemort will attack every 7 secs
    #text input
    text = ""
    name = ""
    #logic
    playing = True
    starting_screen = True
    info_screen = False
    game_over = False
    intro = True #assume player needs into

    #controls animation for welcome screen
    clock = pygame.time.Clock() #need to make things look animated
    current_frame = 0 #start at first motion frame
    frame_timer = pygame.time.get_ticks() #gets ticks to use 
    frame_interval = 200 #controls speed of animation

    num_ghosts = 10
    ghosts_spawned = 0
    death_count = 0

    num_dementors = 40
    dements_spawned =0
    dement_death_count = 0
    expecto_cooldown = 10000  # 10,000 milliseconds = 10 seconds
    expecto_start_time = -expecto_cooldown
    
    sheild_cooldown = 10000
    sheild_start_time = -sheild_cooldown
    

    #screen for level change
    level_transitioning = False
    transition_start_time = 0
    transition_delay = 1000
    next_level = 1
    spells_remain = 2
    spells_remain2= 3
    
    health_spell = "reparo"
    


    #game loop 
    while playing:
        
        #info_image, levelup_images, level_screen = final_helpers.load_level_assets(level)
        
        #initial game screen 
        while starting_screen: #loop so screen stays while typing
                
            for e in pygame.event.get():
                    
                if e.type == pygame.QUIT:
                    pygame.quit()
                    playing = 0 #exits game and playing loop
                    inloop = 0
                    
               #if e.type == pygame.MOUSEMOTION:
                    #print(e.pos) #for us to check locations of mouse on screen
                    
                if e.type == pygame.KEYDOWN: #typing is keydown type
                    if e.key == pygame.K_RETURN: #makes it so can delete
                        starting_screen = False
                        print("Enter pressed!")
                        info_screen = True
                        
            #here is where we do the idle movement on the welcome screen          
            current_tick = pygame.time.get_ticks() #looked this up but gets the tick we are on
            if current_tick - frame_timer >= frame_interval: #checking if the ticks are in our interval
                current_frame = (current_frame +1) % len(welcome_images) #keeps the frames in a loop in our list length so will move through the three images
                frame_timer = current_tick #change the frame timer back
            
            screen.blit(welcome_images[current_frame], (0,0)) #blit using the current frame so they will appear to change
            pygame.display.flip()
            
            clock.tick(60) #controls fps/ looked up
            
        while info_screen: #loop so screen stays while typing
                
            for e in pygame.event.get():
                    
                if e.type == pygame.QUIT:
                    pygame.quit()
                    playing = 0 #exits game and playing loop
                    inloop = 0
                    
                #if e.type == pygame.MOUSEMOTION:
                    #print(e.pos) #for us to check locations of mouse on screen
                    
                if e.type == pygame.KEYDOWN: #typing is keydown type
                    if e.key == pygame.K_SPACE: #makes it so can delete
                        info_screen = False
                        print("Enter pressed!")
                        
    
            
            screen.blit(info_image, (0,0)) #blit using the current frame so they will appear to change
            pygame.display.flip()
            
        
        #main game now
        
        #gets level background 
        final_helpers.get_level_background(level, screen, score)

        
        final_helpers.write_message(screen, text if text else "-", WIDTH/2, 6*TS, 40, (218, 165, 32)) #writes as player writes on the screen in yellow to see input (if no txt in ammotxt string then display _)
        
        
        if level == 2:
            final_helpers.write_message(screen, f'Type "{health_spell}" to regenerate health! ({spells_remain}/2 spells remaining)', WIDTH/2, 1*TS, 40, (218, 165, 32))

        elif level == 3:
        
            
            final_helpers.write_message(screen, f'{spells_remain2}/3 "{health_spell}" remaining', WIDTH/2, 1*TS, 40, (218, 165, 32))
            #final_helpers.write_message(screen, 'Type "expecto patronum" to kill all dementors on screen!', WIDTH/2, 2*TS, 40, (218, 165, 32))
            current_time = pygame.time.get_ticks()
            time_passed = current_time - expecto_start_time

            if time_passed < expecto_cooldown:
            # Ceil the division so it counts down cleanly: 10, 9, 8... down to 1
                seconds_remaining = (expecto_cooldown - time_passed + 999) // 1000
                countdown_text = f"Expecto Patronum: {seconds_remaining}s"
                text_color = (220, 50, 50)  # Red while recharging
            else:
                countdown_text = "Expecto Patronum: READY!"
                text_color = (50, 220, 50)  # Green when ready

            
            final_helpers.write_message(screen, countdown_text, WIDTH // 2, 2*TS, 30, text_color)
       
       
        elif level == 4:
            
            final_helpers.write_message(screen, f'{spells_remain2}/3 "{health_spell}" remaining', WIDTH/2, 1*TS, 40, (218, 165, 32))
            #final_helpers.write_message(screen, 'Type "expecto patronum" to kill all dementors on screen!', WIDTH/2, 2*TS, 40, (218, 165, 32))
            current_time = pygame.time.get_ticks()
            time_passed = current_time - sheild_start_time

            if time_passed < sheild_cooldown:
            # Ceil the division so it counts down cleanly: 10, 9, 8... down to 1
                seconds_remaining = (sheild_cooldown - time_passed + 999) // 1000
                countdown_text = f"Protego: {seconds_remaining}s"
                text_color = (220, 50, 50)  # Red while recharging
            else:
                countdown_text = "Protego: READY!"
                text_color = (50, 220, 50)  # Green when ready

            
            final_helpers.write_message(screen, countdown_text, WIDTH // 2, 2*TS, 30, text_color)
        #get our events
        events = pygame.event.get()
            #check for a quit event
        
        for e in events:
                #quits
            if e.type == pygame.QUIT: #makes sure can still hit the x (should be redundent)
                print('Exiting')
                playing = 0
                inloop = 0
                
            #if e.type == pygame.MOUSEMOTION:
                #print(e.pos) #for us to check locations on screen
                
            if e.type == SPAWN_GHOST_EVENT:
                if level == 1 and ghosts_spawned < num_ghosts:
                    randspell = random.randint(1,10)
                    ghost = Ghost(spell_num = randspell)
                    ghosts.append(ghost)
                    ghosts_spawned += 1
                    
            if e.type == SNAKE_ATTACK_EVENT:
                if level == 2:
                    snake.attack()
                    harry.hurt()
                    harry.health-=1
                    score -=100
                    
            if e.type == VOLD_ATTACK_EVENT:
                if level == 4:
                    voldemort.attack()
                    if harry.sheild == False:
                        harry.hurt()
                        harry.health-=1
                        score -=100
                    else:
                        voldemort.hurt()
                    
            if e.type == SPAWN_DEMENT_EVENT:
                if level == 3 and dements_spawned < 10:
                    randlocationx = random.randint(50,1100)
                    randlocationy = random.randint(100,400)
                    randlocdetermine = random.randint(1,2)
                    randlocdetermine2 = random.randint(1,6)
                    
                    randspeed = random.randint(2,6)
                    if randlocdetermine2==1:
                        dement = Dementor(-200, randlocationy, randspeed)
                        
                    else:
                        if randlocdetermine == 1:
                            dement = Dementor(randlocationx, -200, randspeed)
                        else: 
                            dement = Dementor(1100, randlocationy, randspeed)
                    
                        
                    dements.append(dement)
                    dements_spawned += 1
                
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                        info_screen = True
                        
                if e.key == pygame.K_RETURN:
                    if (text.lower()).strip() == "hermione":
                        harry.hermione = True
                        harry.ron = False
                        harry.harry = False
                        text = ""
                    if (text.lower()).strip() == "ron":
                        harry.ron = True
                        harry.hermione = False
                        harry.harry = False
                        text = ""
                    if (text.lower()).strip() == "harry":
                        harry.harry = True
                        harry.ron = False
                        harry.hermione = False
                        text = ""
                        
                    if level == 6:
                        name = text
                    
                    if level ==1:
                        for i in range(len(ghosts)):
                            if (text.lower()).strip() == ghosts[i].spell:
                                harry.shoot()
                                ghosts[i].die()
                                score += 200
                                text = ""
                                death_count +=1
                    elif level == 2:
                        current_time = pygame.time.get_ticks()
                        
                        if text.lower() == snake.spell:
                            harry.shoot()
                            snake.health-=1
                            score += 100
                            snake.hurt()
                            text = ""
                            
                            if snake.health <= 0 and not level_transitioning and level ==2:
                                snake.done = True
                                level_transitioning = True
                                transition_start_time = pygame.time.get_ticks()
                                next_level = 3
                        
                        if harry.health < 5 and spells_remain > 0:
                            if text.lower() == health_spell:
                                harry.health += 1
                                spells_remain -= 1
                                text = ""
                        else:
                            if text.lower() == health_spell:
                                if harry.health >= 5:
                                    error_start_time = current_time
                                    final_helpers.write_message(screen, 'Health is full!', WIDTH/2, 2*TS, 40, (218, 165, 32))
                                    text = ""
                                    
                                elif spells_remain <= 0:
                                    final_helpers.write_message(screen, 'All spells used up!', WIDTH/2, 2*TS, 40, (218, 165, 32))
                                    text = ""
                                    
                               
                                
                    elif level == 3:
                        current_time = pygame.time.get_ticks()
        

                        # Check if 10 seconds have passed since the last cast
                        if current_time - expecto_start_time >= expecto_cooldown:
                            
                            if text.lower() == "expecto patronum":
                    
                                expecto_start_time = current_time  # Reset the 10-second timer
                                final_helpers.make_noise('expecto_patronum.mp3')
                                harry.shoot()
                                
                                text = ""
                                for dement in dements:
                                    dement.die()
                                    score += 200
                                    text = ""
                                    dement_death_count +=1
                                dements_spawned = 0
                                
                                if num_dementors == 0 and not level_transitioning and level ==3:
                                    level_transitioning = True
                                    transition_start_time = pygame.time.get_ticks()
                                    next_level = 4
                        
                        if harry.health < 5 and spells_remain2 > 0:
                            if text.lower() == health_spell:
                                harry.health += 1
                                spells_remain2 -= 1
                                text = ""
                        else:
                            if text.lower() == health_spell:
                                if harry.health >= 5:
                                    final_helpers.write_message(screen, 'Health is full!', WIDTH/2, 2*TS, 40, (218, 165, 32))
                                    text = ""
                                elif spells_remain2 <= 0:
                                    final_helpers.write_message(screen, 'All spells used up!', WIDTH/2, 2*TS, 40, (218, 165, 32))
                                    text = ""
                                
                    elif level == 4:
                        current_time = pygame.time.get_ticks()
                        if text.lower() == voldemort.spell:
                            harry.shoot()
                            voldemort.health-=1
                            score += 100
                            voldemort.hurt()
                            text = ""
                        

                        # Check if 10 seconds have passed since the last cast
                        if current_time - sheild_start_time >= sheild_cooldown:
                            
                                
                            if text.lower() == "protego":
                    
                                sheild_start_time = current_time  # Reset the 10-second timer
                                final_helpers.make_noise('expecto_patronum.mp3')
                                harry.shoot()
                                harry.sheild = True
                                text = ""
                                
                        if voldemort.health <= 0 and not level_transitioning and level == 4:
                            voldemort.done = True
                            level_transitioning = True
                            transition_start_time = pygame.time.get_ticks()
                            next_level = 6
                        
                        if harry.health < 5 and spells_remain2 > 0:
                            if text.lower() == health_spell:
                                harry.health += 1
                                spells_remain2 -= 1
                                text = ""
                        else:
                            if text.lower() == health_spell:
                                if harry.health >= 5:
                                    final_helpers.write_message(screen, 'Health is full!', WIDTH/2, 2*TS, 40, (218, 165, 32))
                                    text = ""
                                elif spells_remain2 <= 0:
                                    final_helpers.write_message(screen, 'All spells used up!', WIDTH/2, 2*TS, 40, (218, 165, 32))
                                    text = ""               
                                
                        
                    
                        
                if e.key == pygame.K_BACKSPACE: #makes it so can delete
                    text = text[:-1] #strings are lists so can do this method to get from the beggining to the 2nd to last string
                    
                elif e.unicode.isalpha() or e.unicode == " ": # checks if types a letter
                    text += e.unicode #unicode is the value typed and it is added to the end of the string
        
        
        if harry.sheild and pygame.time.get_ticks() - sheild_start_time >= 5000:
            harry.sheild = False
        #blits harry and snakes health onto screen (hearts) but only blits if they have the health 
        for i in range(0,harry.health):
            screen.blit(hearts[i], (i*20+100,3))
        if level == 2:   
            for i in range(0,snake.health):
                screen.blit(snake_hearts[i], (i*20+775,290))
        
        if level == 4:   
            for i in range(0,voldemort.health):
                screen.blit(vold_hearts[i], (i*20+775,280))        
                
        #they will have idle animations when sitting still or doing things
        harry.idle() #idle animation for harry potter
        snake.idle()
        voldemort.idle()
        for ghost in ghosts:
            ghost.idle()
            
        for dement in dements:
            dement.idle() 
        
        #goes through all ghosts and sees if they are close enough to harry to remove health 
        for ghost in ghosts:
            if ghost.x <= 280:#where harry is on x plane
                harry.hurt() #harry hurt animation when hit
                harry.health -=1
                score -=100
                ghost.done = True
                death_count +=1
            ghost.update(screen)
            
        for dement in dements:
            if dement.rect.colliderect(harry.rect):
                harry.hurt()
                harry.health -=1
                score -=100
                dement.done = True
            dement.update(screen)
            
        if level ==2:
            snake.update(screen)
            
        if level ==4:
            voldemort.update(screen)
        
        if harry.dead == False:
            harry.draw(screen) #blits him onto screen
        else:
            game_over=True
            level_transitioning = True
            
        for ghost in ghosts:
            if ghost.done == False:
                ghost.draw(screen)
            else:
                ghosts.remove(ghost)
                
        for dement in dements:
            if dement.done == False:
                dement.draw(screen)
            else:
                dements.remove(dement)
                
        if level == 2 and snake.done == False:
            snake.draw(screen)
        
        if level == 4 and voldemort.done == False:
            voldemort.draw(screen)
        
        #print(text)
            
        clock.tick(60) #controls fps/ looked up
        pygame.display.flip()#need so everything is in front
        
        if death_count >= num_ghosts and not level_transitioning and level ==1:
            level_transitioning = True
            transition_start_time = pygame.time.get_ticks()
            next_level = 2
            
        if dement_death_count >= num_dementors and not level_transitioning and level ==3:
            level_transitioning = True
            transition_start_time = pygame.time.get_ticks()
            next_level = 4
            
        
        
        if level_transitioning: #will wait so clean transition
            transitioning_screen = True
            if game_over == True:
                level = 6
            levelup_fps = [f"{level}levelup_screen(1).jpg", f"{level}levelup_screen(2).jpg", f"{level}levelup_screen(3).jpg" ]  
            levelup_images = [final_helpers.background(levelup_fps[0], 0.4), final_helpers.background(levelup_fps[1], 0.4), final_helpers.background(levelup_fps [2], 0.4)]
            
            while transitioning_screen:
                for e in pygame.event.get():
                    
                    if e.type == pygame.QUIT:
                        pygame.quit()
                        playing = 0 #exits game and playing loop
                        inloop = 0
                    
                    if e.type == pygame.KEYDOWN: #typing is keydown type
                        if e.key == pygame.K_RETURN: #makes it so can delete
                            if game_over == True:
                                #pygame.quit()
                                playing = 0
                                transitioning_screen= False
                                #break
                            else:
                                transitioning_screen = False
                                print("Enter pressed!")
                                info_screen = True
                
                
                current_tick = pygame.time.get_ticks() #looked this up but gets the tick we are on
                if current_tick - frame_timer >= frame_interval: #checking if the ticks are in our interval
                    current_frame = (current_frame +1) % len(welcome_images) #keeps the frames in a loop in our list length so will move through the three images
                    frame_timer = current_tick #change the frame timer back
                
                screen.blit(levelup_images[current_frame], (0,0)) #blit using the current frame so they will appear to change
                final_helpers.write_message(screen, f"{score}", 490, 310, 40, (218, 165, 32)) #writes as player writes on the screen in yellow to see input (if no txt in ammotxt string then display _)
                if level ==1:
                    final_helpers.write_message(screen, f"{num_ghosts}", 650, 250, 40, (218, 165, 32))
                elif level ==2:
                    final_helpers.write_message(screen, "1", 650, 250, 40, (218, 165, 32))
                elif level ==3:
                    final_helpers.write_message(screen, f"{num_dementors}", 650, 250, 40, (218, 165, 32))
                elif level == 6:
                    with open(filename) as file_object:
                        for line in file_object:
                            final_helpers.write_message(screen, f"{line}", 650, 250, 40, (218, 165, 32))
                    final_helpers.write_message(screen, text if text else "-", WIDTH/2, 6*TS, 40, (218, 165, 32)) 
                    with open(filename,'w') as file_object:
                        file_object.write(f"{name} {score}")
                    

                pygame.display.flip()
                clock.tick(60)
               
            level = next_level
            level_transitioning = False
            text = ""
            
            info_image, levelup_images, level_screen = final_helpers.load_level_assets(level)
            
            if level == 2:
                ghosts.clear()
                ghosts_spawned = 0
                    
pygame.quit() #exit 