import pygame as p
import pygame.font

p.init()

p.display.set_caption("BASKETBALL_GAME")

hauteur = 480  #taille de la hauteur de l'ecran
longueur =640  #taille longueur de la fenetre

screen = p.display.set_mode((longueur, hauteur))  # Taille Ecran

gris = (127, 127, 127)
yellow = (255,255,0)
red = (255,0,0)
black=(0,0,0)

police = p.font.SysFont("arialblack", 20) #on defini la police de caractere avec le type de police et la taille des caracteres

def texte(text,police,couleur_text,x,y):
    img= police.render(text,True,couleur_text)
    screen.blit(img,(x,y))

playnewgame=False
Open=True
while Open:
    screen.fill(yellow)
    if playnewgame==True:
        pass
    else:
        texte("Play new game",police,black,100,200)
    for event in p.event.get():
        if event.type==p.KEYDOWN:
            if event.key==pygame.K_SPACE:
                playnewgame=True
        if event.type == p.QUIT:
            Open=False  # La page se ferme
    p.display.update()



p.init()
p.quit()
quit()