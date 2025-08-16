import pygame

w = 640  # width and height
h = 480


white = (255, 255, 255)
black = (0, 0, 0)
purple = (58, 38, 96)
electric_blue = (43, 111, 255)
gray = (127, 127, 127)
lime_green = (0, 255, 0)
darker_lime_green = (34, 139, 34)
green = (54, 115, 88, 255)






# fade out
def fade_out(win,width=230, height=234,speed=1):
    new_screen = pygame.Surface((width, height)) 
    new_screen.fill(black)

    
    for alpha in range(0, 257,speed):  
        new_screen.set_alpha(alpha)
        win.blit(new_screen, (0, 0))
        pygame.display.update()
        pygame.time.delay(10) # delay

    win.fill((0, 0, 0)) # just to make sure screen fully black




# fade in
def fade_in(win,width=230, height=640,speed=-2):
    new_screen = pygame.Surface((width, height)) 
    new_screen.fill(black)
    new_screen.set_alpha(255)

    
    for alpha in range(255, -1,speed):  
        new_screen.set_alpha(alpha)
        win.fill(green)
        win.blit(new_screen, (0, 0))
        pygame.display.update()
        pygame.time.delay(20) 


def arrange_cards_evenly(cards, start_x, end_x, y):
    total_cards = len(cards)
    if total_cards == 0:
        return
    
    total_width = end_x - start_x
    spacing = total_width // (total_cards - 1) if total_cards > 1 else 0
    
    for index, card in enumerate(cards):
        card.posx = start_x + spacing * index
        card.posy = y

def draw_text(text,win,f,color,x,y):
    img = f.render(text,True,color)
    win.blit(img,(x,y))
    
class health_bar:
    def __init__(self,x,y,w,h,max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.max_hp = max_hp




if __name__ == "__main__":
    pygame.init()
    t = pygame.display.set_mode((w,h))
    fade_out(t) 
    pygame.quit()
   