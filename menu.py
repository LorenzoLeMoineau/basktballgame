import pygame as p
import boutons as b
from pygame.locals import *

p.init()

p.display.set_caption("BASKETBALL_GAME")

hauteur = 800  #taille de la hauteur de l'ecran
longueur =800  #taille longueur de la fenetre

screen = p.display.set_mode((longueur, hauteur))  # Taille Ecran

#---------------------------COLORS THAT WE MIGHT USE---------------------------------------------------------------------------------------------------------------
fond=p.image.load("terrain.jpg")
fond=fond.convert()
gris = (127, 127, 127)
yellow = (255,255,0)
red = (255,0,0)
black=(0,0,0)
pink=(255,20,147)
blue=(30,144,255)
green=(0,201,87)
orange=(255,128,0)

#---------------CONVERTING THE IMAGES(to have their width and everything...)-----------------------------------
rules_img=p.image.load("images/RULES.png").convert_alpha()
play_img=p.image.load("images/PLAY.png").convert_alpha()
men_img=p.image.load("images/HOMME.png").convert_alpha()
women_img=p.image.load("images/FEMME .png").convert_alpha()
red_img=p.image.load("images/ROUGE.png").convert_alpha()
orange_img=p.image.load("images/ORANGE.png").convert_alpha()
yellow_img=p.image.load("images/JAUNE.png").convert_alpha()
green_img=p.image.load("images/VERT.png").convert_alpha()
purple_img=p.image.load("images/VIOLET.png").convert_alpha()
blue_img=p.image.load("images/BLEU.png").convert_alpha()

#-------------CONVERTING THE IMAGES INTO BUTTONS(AND GIVE THEIR PLACE)-------------------------------------------
#back_button=b.Boutons(400,100,"images/button_back.png",1)
#keys_button=b.Boutons(400,200,"images/button_keys.png",1)
#options_button=b.Boutons(400,300,"images/button_options.png",1)
rules_button=b.Boutons(350,300,rules_img,1)
play_button=b.Boutons(350,200,play_img,1)
men_button=b.Boutons(100,100,men_img,1)
women_button=b.Boutons(600,100,women_img,1)
red_button=b.Boutons(200,100,red_img,1)
orange_button=b.Boutons(400,100,orange_img,1)
yellow_button=b.Boutons(600,100,yellow_img,1)
purple_button=b.Boutons(200,300,purple_img,1)
green_button=b.Boutons(400,300,green_img,1)
blue_button=b.Boutons(600,300,blue_img,1)


police = p.font.SysFont("arialblack", 20) #on defini la police de caractere avec le type de police et la taille des caracteres

def texte(text,police,couleur_text,x,y):
    img= police.render(text,True,couleur_text)
    screen.blit(img,(x,y))

bouton=p.image.load("resume.png")

rules=False
pause=False
state="menu"
Open=True
gender="men"
ballcolor="red"
while Open:
    screen.fill(gris)
    if state=="menu":
        texte("BASKETBALL",police,black,330,100)
        if rules_button.placer(screen):
            state="rules"
        if play_button.placer(screen):
            state="play"
    if state=="rules":
        texte("RULES",police,black,100,200)
        texte("EASY MODE: SCORE 1 BASKET IN 5 MIN",police,green,100,218)
        texte("NORMAL MODE: SCORE 2 BASKETS IN 5 MIN",police,blue,100,236)
        texte("SPICY MODE: SCORE 3 BASKETS IN 5 MIN",police,orange,100,254)
        texte("HARD MODE: SCORE 4 BASKETS IN 5 MIN",police,pink,100,272)
        texte("DEAD MODE: SCORE 5 BASKETS IN 5 MIN",police,red,100,290)
        for event in p.event.get():
            if event.type == p.QUIT:
                Open = False
    if state=="play":
        texte("CHOOSE YOUR GENDER",police,black,200,400)
        if men_button.placer(screen):
            state="balls"
            gender="men"
        if women_button.placer(screen):
            state="balls"
            gender="women"
        for event in p.event.get():
            if event.type == p.QUIT:
                Open = False
    if state=="balls":
        texte("CHOOSE THE COLOR OF YOUR BALL",police,black,200,200)
        if red_button.placer(screen):
            state="background"
            ballcolor="red"
        if yellow_button.placer(screen):
            state="background"
            ballcolor="yellow"
        if orange_button.placer(screen):
            state="bakcground"
            ballcolor="orange"
        if purple_button.placer(screen):
            state="background"
            ballcolor="purple"
        if green_button.placer(screen):
            state="background"
            ballcolor="green"
        if blue_button.placer(screen):
            state="background"
            ballcolor="blue"
    if state=="difficulty":


    for event in p.event.get():
        if event.type == p.QUIT:
          Open = False


    p.display.update()

p.init()
p.quit()
quit()
