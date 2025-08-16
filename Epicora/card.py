import random
import pygame
from utils import draw_text


pygame.font.init()
path = "ThaleahFat\\ThaleahFat.ttf"
font = pygame.font.Font(path,12)
 
 # -- sunday
 # add point system later so that if they hovering over and have enough points the text green and says
 # you have enough points


 # sunday - i shall make the pc cards and start turn system
 #saturday health bar and game music
 
def revolve(cards,uni_cards):  # rotate/ helper function and correct card
      for x in range(25):
        temp = pygame.image.load("Assets\\cards.png")
        uni_cards[x].img1 = pygame.transform.scale(temp, (140, 140))
        uni_cards[x].original_img1 = pygame.transform.rotate(uni_cards[x].original_img1, 180)
        uni_cards[x].img2 = pygame.transform.rotate(uni_cards[x].img2, 180)
    
      cards_pc = uni_cards[:25]
      cards.extend(cards_pc)
      del uni_cards[:25]
      
      return cards
   


class Card:
    def __init__(self, name, color, attack, heal, points, img1, img2,enlarged,posx=140,posy=500):
        self.posx = posx
        self.posy = posy

        self.originalposy = posy # original position of the y
        self.original_img1 = img1 # original image that is needed when we change
        self.enlarged = enlarged # enlarged image

        self.clicked = False
        self.pressed = False 
        

    

        self.name = name
        self.color = color
        self.attack = attack
        self.heal = heal
        self.point = points
        self.img1 = img1
        self.img2 = img2
        self.rect = self.img1.get_rect()
        self.rect.topleft = (self.posx, self.posy)
        self.enough = True # at first user will have enough points for any card

        self.info = [self.name,f"Attack: {self.attack}",f"Points: {self.point}",f"Color: {self.color}",f"Sufficent points: {self.enough}"]


        
        




    def draw_info(self,win,pn): # will take self info as list and blit each text to screen# pn stands for points

        lst = self.info
        x = self.posx + 5 # add 5 to posx to move text slightly to right
        y = self.posy + 80 # will change the y so each time it moves down text
        color_pn = (0, 255, 127)
        

        if pn < self.point:
            color_pn = (255, 0, 0)
            self.enough = False
            lst[len(lst)-1] = f"Sufficent points: {self.enough}"
        else:
            self.enough = True
            lst[len(lst)-1] = f"Sufficent points: {self.enough}"

            
            
        

        
    
        for line in lst:
            if "Sufficent" in line:
                draw_text(line,win,font,color_pn,x,y)
            else:
              draw_text(line,win,font,(0,0,0),x,y)
              y += font.get_height() + 2

        
    
    def touch(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = (self.posx, self.posy)
        if self.rect.collidepoint(pos): # will add pressed later
            return True
        
    
    def click(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = (self.posx, self.posy)
        if self.rect.collidepoint(pos): # will add pressed later
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
               self.clicked = True
               return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
     



    def copy(self):
    
      return Card(
        name=self.name,
        color=self.color,
        attack=self.attack,
        heal=self.heal,
        points=self.point,
        img1=self.original_img1.copy(),  
        img2=self.img2.copy() if self.img2 else None,
        enlarged=self.enlarged.copy(),
        posx=self.posx,
        posy=self.posy
    )
   
   

        

    @staticmethod
    def generate():
        cards_data = {
            #Reds
            "red_ogre": {"Color": "red", "Attack": 7, "Points": 8, "Heal": False, "Image_1": "Assets\\cards\\red_ogre1.png", "Image_2": "Assets\\cards\\red_ogre2.png"},
            "red_mage": {"Color": "red", "Attack": 8, "Points": 10, "Heal": False, "Image_1": "Assets\\cards\\red_mage1.png", "Image_2": "Assets\\cards\\red_mage2.png"},
            "red_knight": {"Color": "red", "Attack": 5, "Points": 2, "Heal": False, "Image_1": "Assets\\cards\\red_knight1.png", "Image_2": "Assets\\cards\\red_knight2.png"},
            "red_Heal": {"Color": "red", "Attack": 0, "Points": 0, "Heal": True, "Image_1": "Assets\\cards\\red_heal1.png", "Image_2": "Assets\\cards\\red_heal2.png"},
            "red_Horse": {"Color": "red", "Attack": 4, "Points": 5, "Heal": False, "Image_1": "Assets\\cards\\red_Horse1.png", "Image_2": "Assets\\cards\\red_Horse2.png"},
            
            #blues
            "blue_ogre": {"Color": "blue", "Attack": 7, "Points": 8, "Heal": False, "Image_1": "Assets\\cards\\blue_ogre1.png", "Image_2": "Assets\\cards\\blue_ogre2.png"},
            "blue_mage": {"Color": "blue", "Attack": 8, "Points": 10, "Heal": False, "Image_1": "Assets\\cards\\blue_mage1.png", "Image_2": "Assets\\cards\\blue_mage2.png"},
            "blue_knight": {"Color": "blue", "Attack": 5, "Points": 2, "Heal": False, "Image_1": "Assets\\cards\\blue_knight1.png", "Image_2": "Assets\\cards\\blue_knight2.png"},
            "blue_Heal": {"Color": "blue", "Attack": 0, "Points": 0, "Heal": True, "Image_1": "Assets\\cards\\blue_heal1.png", "Image_2": "Assets\\cards\\blue_heal2.png"},
            "blue_Horse": {"Color": "blue", "Attack": 4, "Points": 5, "Heal": False, "Image_1": "Assets\\cards\\blue_Horse1.png", "Image_2": "Assets\\cards\\blue_Horse2.png"},
            
            #greens
            "green_ogre": {"Color": "green", "Attack": 7, "Points": 8, "Heal": False, "Image_1": "Assets\\cards\\green_ogre1.png", "Image_2": "Assets\\cards\\green_ogre2.png"},
            "green_mage": {"Color": "green", "Attack": 8, "Points": 10, "Heal": False, "Image_1": "Assets\\cards\\green_mage1.png", "Image_2": "Assets\\cards\\green_mage2.png"},
            "green_knight": {"Color": "green", "Attack": 5, "Points": 2, "Heal": False, "Image_1": "Assets\\cards\\green_knight1.png", "Image_2": "Assets\\cards\\green_knight2.png"},
            "green_Heal": {"Color": "green", "Attack": 0, "Points": 0, "Heal": True, "Image_1": "Assets\\cards\\green_heal1.png", "Image_2": "Assets\\cards\\green_heal2.png"},
            "green_Horse": {"Color": "green", "Attack": 4, "Points": 5, "Heal": False, "Image_1": "Assets\\cards\\green_Horse1.png", "Image_2": "Assets\\cards\\green_Horse2.png"},
            
            #Normals
            "Normal_ogre": {"Color": "white", "Attack": 7, "Points": 8, "Heal": False, "Image_1": "Assets\\cards\\Normal_ogre.png"},
            "Normal_knight": {"Color": "white", "Attack": 5, "Points": 2, "Heal": False, "Image_1": "Assets\\cards\\Normal_knight.png"},
            "Normal_Horse": {"Color": "white", "Attack": 4, "Points": 5, "Heal": False, "Image_1": "Assets\\cards\\Normal_Horse.png"},
        }

        cards = []
        pc_cards = []
        for _ in range(50):
            card_key = random.choice(list(cards_data.keys()))
            data = cards_data[card_key]
            t_img1 = pygame.image.load(data["Image_1"])
            desired_width, desired_height = 150, 150
            img1 = pygame.transform.scale(t_img1, (desired_width, desired_height))
            enlarged = pygame.transform.scale(t_img1, (200, 200)) # 200
            
            if data.get("Image_2"):
                img2 = pygame.transform.scale(pygame.image.load(data["Image_2"]), (desired_width, desired_height))
            else:
                img2 = img1

            
            card = Card(
                name=card_key,
                color=data["Color"],
                attack=data["Attack"],
                heal=data["Heal"],
                points=data["Points"],
                img1=img1,
                img2=img2,
                enlarged=enlarged
            )
            cards.append(card)
            
        fixed = revolve(pc_cards,cards)
       
            
        return cards,fixed
    
    
    
class Button(Card):
    def __init__(self,img,img2,x=380,y=300,scale1=140,scale2=140):
        temp = pygame.image.load(img) # load image
        temp2 = pygame.image.load(img2)
        
        self.original_img = pygame.transform.scale(temp,(scale1,scale2))
        self.img1 = pygame.transform.scale(temp,(scale1,scale2))
        self.img2 = pygame.transform.scale(temp2,(scale1,scale2)) # will change once i finish making the card for the pile


        self.posx = x
        self.posy = y
        self.clicked = False
        self.rect = self.img1.get_rect() 
        self.rect.topleft = (x,y)
        






if __name__ == "__main__":
    t = Card.generate()
