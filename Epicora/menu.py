import pygame
import os # might use idk
import game
from utils import fade_out

# note: when doing the a level course work i shall add mroe stuff such as versions/diffuclty level
# more cards and maybe 2 player or multiple ais for now i will keep with the basic stuff

# colours

white = (255, 255, 255)
black = (0, 0, 0)
purple = (58, 38, 96)
electric_blue = (43, 111, 255)
gray = (127, 127, 127)
lime_green = (0, 255, 0)
darker_lime_green = (34, 139, 34)


pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.mixer.music.set_volume(0.1)

# font setup
path = "ThaleahFat\\ThaleahFat.ttf"  # font 1
path2 = "fff-forward\\FFFFORWA.TTF"  # second font
font = pygame.font.Font(path, 155)
font2 = pygame.font.Font(path2,15)


def fade_out(width=230, height=234,speed=1):
    new_screen = pygame.Surface((width, height)) # stuff here to just initialize the window
    new_screen.fill(black)

    
    for alpha in range(0, 257,speed):  
        new_screen.set_alpha(alpha)
        win.blit(new_screen, (0, 0))
        pygame.display.update()
        pygame.time.delay(20) # delay

def settings(): # program aftr making the game
    pass


def main():
    global win,pl1,pl2
    clock = pygame.time.Clock()
    fps = 60
    count = 0
    run = True

    w = 640  # width and height
    h = 480
    pygame.display.set_caption("Menu")
    win = pygame.display.set_mode((w, h))
    
    # Load images
    try:
        logo = pygame.image.load("Assets\\soldier.png")
        click = pygame.mixer.Sound("sound\\card_click.wav") # might change sound later
        setting = pygame.image.load("Assets\\gear.png")
        pl_1 = pygame.image.load("Assets\\play1.png")
        pl_2 = pygame.image.load("Assets\\play2.png")
        exit1 = pygame.image.load("Assets\\exit1.png")
        exit2 = pygame.image.load("Assets\\exit2.png")
    except pygame.error as e:
        print("Error loading images:", e)
        
    pygame.display.set_icon(logo) 

    # Scale images
    setting_new = pygame.transform.scale(setting, (150, 150))
    pl1 = pygame.transform.scale(pl_1, (170, 160))
    pl2 = pygame.transform.scale(pl_2, (170, 160))
    exit1 = pygame.transform.scale(exit1, (120, 110))  
    exit2 = pygame.transform.scale(exit2,(120,110))
 


   


    while run:
        win.fill(gray)  # fills background 
        text1 = font.render("EPICORA",False,white) # title
        text2 = font2.render("Made by MisterBemo",False,white)

        win.blit(text1,(74,4))
        win.blit(text2,(415,450))



        win.blit(setting_new, (-40,350))
        win.blit(exit1, (240, 350))

        key = pygame.key.get_pressed()



        if count == 1:
            win.blit(pl2, (220, 190))
            if key[pygame.K_RETURN]:
                click.play()
                fade_out(w,h)
                game.mains() # this essentially will run the whole game
                run = False
        elif count == 2:
            win.blit(pl1, (220, 190))
            win.blit(exit2, (240, 350))
            if key[pygame.K_RETURN]:
                run = False
       
            
        if count <= 0:
            count = 1
        elif count > 2:
            count = 2




        

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                   count += 1
                elif event.key == pygame.K_UP:
                    count -= 1
        #print(count)
        

       

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
  main()







