import os
import random
import pygame
from card import Card,Button,font as font2
import time


from utils import fade_in,fade_out,arrange_cards_evenly,draw_text

pygame.mixer.init()
pygame.init()
pygame.font.init()


# add in health and point system soon

# fonts
ari = pygame.font.SysFont("Arial",40)
path = "ThaleahFat\\ThaleahFat.ttf"
font = pygame.font.Font(path,40)



# colours
white = (255, 255, 255)
black = (0, 0, 0)
purple = (58, 38, 96)
electric_blue = (43, 111, 255)
gray = (127, 127, 127)
lime_green = (0, 255, 0)
darker_lime_green = (34, 139, 34)
green = (54, 115, 88, 255)
red = (255, 0, 0)
gold =  (255, 215, 0)

points = 20 # change to 20 when done
pl_hp = 0
pc_hp = None


# Global variables for overlay control

overlay_message = ""  


def draw_discard(lst):
    for card in lst:  # works
        window.blit(card.img1, (card.posx, card.posy))
    
def discard_pile(pc,player=None):
    
    
    if pc.heal:
      pc.posx = 700
      pc.posy = 300
      pc.img1 = pc.original_img1
    else:
        player.posx = 700
        player.posy = 300
        player.img1 = player.original_img1
        
        pc.posx = 700
        pc.posy = 300
        pc.img1 = player.original_img1
        
    
    
    
    
    

def setup(uni_cards, user):
    user_cards = uni_cards[:5]
    user.extend(user_cards)
    del uni_cards[:5]


    

def pc_setup(uni_cards,pc): #during setup rotate cards
    for c in range(5):
        pc.append(uni_cards[c])
        uni_cards.pop(c) # might do inner function
    
   
    

def damage_step(pc_color, user_color,pc,player,discard):
    global overlay_message,pl_hp
    user_attack = user_color.attack
    pc_attack = pc_color.attack

    if color_checker(pc_color.color, user_color.color):
        user_attack = user_color.attack * 2

    if color_checker(user_color, pc_color):
        pc_attack = pc_color.attack * 2

    """
    if user_attack > pc_attack:
        overlay_message = "PLAYER WINS"
        message_color = gold
    elif user_attack < pc_attack:
        overlay_message = "PC WINS"
        message_color = red
    else:
        overlay_message = "NULL"
        message_color = gray
    """
    
   
    discard.append(pc_color)
    discard.append(user_color)
    pc.remove(pc_color) # pc list
    player.remove(user_color) # player list
        
        
    
    
    # if will be here so if user attack higher than pc we do calculation pc take damage otherwise we calculate and player take damage
    
    discard_pile(player=pc_color,pc=user_color)

    

       


# make an if statement that checs if player cannot play any cards and if so they can collect points equal to highest card

def color_checker(attacker, defender):
    return (
        (attacker == "red" and defender == "green") or
        (attacker == "green" and defender == "blue") or
        (attacker == "blue" and defender == "red")
    )
    
def actions(ai_cards, card,pc):
    # AI for the computer will handle attack and elements - we need the color and the attack points
    
    
    # Filter out cards that are not healed
    fixed_ai = [_ for _ in ai_cards]
    #print(len(fixed_ai))
    
    highest = [fixed_ai[0]]
    
    if len(pc) != 0:
        if len(fixed_ai) == 1:
            for _ in range(4):
                choice = random.choice(pc)
                ai_cards.append(choice)
                pc.remove(choice)
    else:
        print("oops they lost")# will write code here to show that pc lost
        
        
    arrange_cards_evenly(ai_cards, start_x=100, end_x=700, y=100)
    
    # print(len(pc))
        
        
    for item in fixed_ai:  # loop through cards # will also have to check if pc has enough points to play
        if item.attack > card.attack:  # finds strongest monster
            if color_checker(card.color, item.color):
                atk = item.attack * 2
            else:
                atk = item.attack
        else:
            atk = item.attack

        if atk >= highest[0].attack:
            highest[0] = item
    
    
    return highest[0]
    # if ai hp is low then pick card with heal instead of returning card with highest value

    

    

def play(player_cards,pc_cards,card,discarded,pc): # this shall be the gamesetup probs gonna handle everything including damage step
    global pl_hp
    #pc_list is pc
    if card.heal == True:
        discard_pile(pc=card)
        discarded.append(card)
        player_cards.remove(card) # pc list
        pl_hp+= 4
        return
    
    
        

    
    

    
    
    #temp_img = card.enlarged.convert_alpha()
    #temp_img.set_alpha(240)
    #card.img1 = temp_img
    #card.posx = 200
    #card.posy = 250

    item = actions(pc_cards,card,pc) # best card returned by ai
   

    #temp_img = item.enlarged.convert_alpha()
    #temp_img.set_alpha(240)
    #item.img1 = temp_img
    #item.posx = 500
    #item.posy = 250
    
    
    damage_step(item,card,pc_cards,player_cards,discarded)
    


    
    #print(item.info)

    

    # pc will play its card and do its turn
    # pc will have functuon that will pick its card
    # then will choose the best card to counter with and if all its cards are weaker then it shall not play a card
    #i shall make a function called damage step to deal with it
    #player_cards.remove(card)

    


def draw_pc(pc_list, window):
    for card in pc_list:  # works
        window.blit(card.img1, (card.posx, card.posy))
       


    


def player(player_list, window, card_list, pile, font, red, shuffle, card_click, draw_text,discard,pc_list,pc,coins_pile,coin_click):
    global points,pl_hp
    


    for card in player_list:  # works
        window.blit(card.img1, (card.posx, card.posy))
        if card.touch() and not any(press.pressed for press in player_list):
            if card.img2: # check if img2 value
                if not card.pressed: # check if not been pressed
                  card.img1 = card.img2
                  card.draw_info(window,points)
                  if card.posy > 480:
                      card.posy -= 1

                if card.click() and  not card.pressed and not any(press.pressed for press in player_list) and points >= card.point:
                    points-= card.point
                    card.pressed = True #do not touch this
                    card_click.play()  # play sound or action
                    #print(points)  # wait will fix
                    play(player_list,pc_list,card,discard,pc) 
                    print(f"Your points:{points}")
                    print(pl_hp)
                    
                    #draw_text(overlay_message, window, font, gold, 300, 300)
                    
                else:
                    if points < card.point:
                        draw_text("insufficent points", window, font, red, 300, 240)
        else:
            if not card.pressed:
              card.img1 = card.original_img1
              card.posy = card.originalposy
              
        

    if pile.touch() and not any(press.pressed for press in player_list):
        pile.img1 = pile.img2
        if len(player_list) == 5:
            draw_text("Cannot add anymore cards", window, font, red, 240, 240)

    else:
        pile.img1 = pile.original_img
        # tomorrow do the poits and health bar system
        
    if coins_pile.touch() and not any(press.pressed for press in player_list):
        coins_pile.img1 = coins_pile.img2
    else:
        coins_pile.img1 = coins_pile.original_img
        
        
        
    # will write a point clicker system here
    
    if coins_pile.click() and not any(press.pressed for press in player_list) and len(player_list) == 5:
        if not any(card for card in player_list if card.point < points and card.heal == False):
            coin_click.play()
            points+= 8
            pl_hp-=4
            draw_text("POINTS ACQUIRED", window, font, lime_green, 400, 240)
            
            
            
            
    


    if pile.click() and not any(press.pressed for press in player_list):  
        if len(player_list) < 5:  # if u got less than 5 cards in hand u may draw else no
            points+=1
            rand = random.choice(card_list)
            player_list.append(rand)
            card_list.remove(rand)
            arrange_cards_evenly(player_list, start_x=100, end_x=700, y=500)
            shuffle.play()
        
            
         
    




def mains(): # shall take care of basically everything
    global window
    clock = pygame.time.Clock()
    fps = 60
    count = 0
    run = True

    w = 900
    h = 700
    
    
    
    


    # for text


 



    
    
    try: 
        #icon = pygame.image.load("")
        place = pygame.image.load("Assets\\shadow.png")

        shuffle = pygame.mixer.Sound("sound\\shuffle.wav")
        card_click = pygame.mixer.Sound("sound\\clicked.wav")
        coin_click  = pygame.mixer.Sound("sound\\coin_click.wav")


        icon = pygame.image.load("Assets\\soldier.png")
        red_button = pygame.image.load("Assets\\red_button1-1.png") # exit button thing 1
        red_button2 = pygame.image.load("Assets\\red_button2-2.png")# exit button thing 2
        click = pygame.mixer.Sound("sound\\clicked.wav")

    except Exception as e:
        print(e)

    pygame.display.set_caption("EPICORA")
    pygame.display.set_icon(icon)

    window = pygame.display.set_mode((w, h))
    window.fill(green)

    
    # rectangles
    place2 = pygame.transform.scale(place,(640,150))
    place3 = pygame.transform.scale(place,(640,150))
    button = pygame.transform.scale(red_button,(150,150))
    button2 = pygame.transform.scale(red_button2,(150,150))
    card_pile = pygame.transform.scale(place,(200,150))
    discard_pile = pygame.transform.scale(place,(150,150))
    
   

    card_list,pc = Card.generate() # universal card list for pc and card_list
    player_list = []           # player list#
    pc_list = []               # pc list
    
    discard = []               # discard pile
    setup(card_list,player_list)
    pc_setup(pc,pc_list)
    arrange_cards_evenly(player_list, start_x=100, end_x=700, y=500) # player cards
    arrange_cards_evenly(pc_list, start_x=100, end_x=700, y=100) # pc cards
    



    #raise Exception("eggs")
    


    # test
    pile = Button("Assets\\cards\\Deck_1.png","Assets\\cards\\Deck_2.png")
    coins_pile = Button("Assets\\coins1.png","Assets\\coins2.png",100,300,50,50)


    #fade_in(window,w,h)
    while run:
        key = pygame.key.get_pressed() # get key pressed

        window.fill(green)
        

        # draw card 
        

        window.blit(place2,(140,100))
        window.blit(place3,(140,500))
        window.blit(card_pile,(350,300))
        window.blit(discard_pile,(700,300))
        
       


        window.blit(pile.img1,(pile.posx,pile.posy))
        window.blit(coins_pile.img1,(coins_pile.posx,coins_pile.posy)) 

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    count +=1
                elif event.key == pygame.K_DOWN:
                    count-=1

                    
        
        if count == 1:
            window.blit(button2,(-10,-20))
            if key[pygame.K_RETURN]:
                click.play()
                #fade_out(window,w,h)
                run = False
        elif count == 0:
            window.blit(button,(-10,-20))
        else:
            if count > 1:
                count = 1
            elif count < 0:
                count = 0


        player(player_list=player_list, window=window, card_list=card_list, pile=pile,coins_pile=coins_pile, font=font, red=red, shuffle=shuffle, card_click=card_click,coin_click=coin_click, draw_text=draw_text,discard=discard,pc_list=pc_list,pc=pc)
        draw_discard(discard) # draw discard pile
        draw_pc(pc_list=pc_list,window=window)
        
        # code will be written here to check win conditions for hp and drawing  
        

        pygame.display.update()
        
        
        
    pygame.quit()
   

if __name__ == "__main__": 
    mains()