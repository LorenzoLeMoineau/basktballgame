import pygame
import time
import math

marge=20 #marge du terrain sur l'écran
c_g=9.81 #constante gravitationnel
c_xs=640 #taile en pixel de la longueur
c_ys=480 #taille en pixel de la hauteur
c_hr=8 #hauteur du plafond en metre
c_hterrainp=c_ys-(marge*2) #hauteur du terrain
c_lterrain=(c_hr*(c_xs-marge*2))/c_hterrainp #environ 11.63 m longueur terrain
coeffpix2m=c_hr/c_hterrainp #coefficient de conversion de pixel à mètre
coeffm2pix=c_hterrainp/c_hr #coefficient de conversion de mètre à pixel
c_amortissement=0.5 #coefficient d'amortissement
c_seuilv=0.9 #seuil de vitesse auquel la balle s'arrête
c_rayonball=0.15 #rayon de la balle

pygame.init()
pygame.display.set_caption("game")
screen = pygame.display.set_mode((c_xs,c_ys))

#convertie les coordonnées dans le repère physique classique dans le repère inversé de Pygame
def chgtrepere(xp,yp):
    xs=xp+marge
    ys=(c_ys-yp)-marge
    return xs,ys

#dessine la ball à partir des coordonnés physiques du moteur
def ball(xp,yp):
    global coeffm2pix
    xp = xp * coeffm2pix
    yp = yp * coeffm2pix
    xs, ys = chgtrepere(xp, yp)
    rayon=c_rayonball*coeffm2pix
    pygame.draw.circle(screen, (153, 204, 255),(xs, ys), rayon)
    pygame.display.flip()

# dessine l'axe physique du jeu
def drawaxe():
    white = (255, 255, 255)
    pygame.draw.line(screen, white, (0, c_ys-marge), (c_xs, c_ys-marge), 1)
    pygame.draw.line(screen, white, (marge, c_ys), (marge, 0), 1)
    pygame.draw.line(screen, white, (c_xs - marge,c_ys), (c_xs-marge,0), 1)
    pygame.draw.line(screen, white, (0,marge),(c_xs,marge), 1)

#calcule la vitesse d'un vecteur en fonction de son angle, de sa composante en x et y et du temps t
def vitesse(angle,vi,t):
    global c_g
    vx=vi*math.cos(angle)
    vy=-c_g*t+vi*math.sin(angle)
    return vx,vy

#calcule la norme d'un vecteur
def norme(x,y):
    norm=math.sqrt(x**2+y**2)
    return norm

#calcule le produit scalaire
def scalaire(x1,y1,x2,y2):
    return x1*x2+y1*y2

#calcule l'angle entre deux vecteurs
def angle(x1,y1,x2,y2):
    dot = x1 * x2 + y1 * y2  # dot product between [x1, y1] and [x2, y2]
    det = x1 * y2 - y1 * x2  # determinant
    angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
    return angle

#effectue une rotation de vecteur selon un certain angle donné
def rotationvecteur(x,y,angle):
    xf=x*math.cos(angle)-y*math.sin(angle)
    yf=x*math.sin(angle)+y*math.cos(angle)
    return round(xf,4),round(yf,4)

#calcule l'angle de réflexion après une collision
def anglereflexion(nx,ny,vx,vy):
    nrx,nry=rotationvecteur(nx,ny,-math.pi/2)
    angler=angle(vx,vy,nrx,nry)
    anglecorrection=angle(1,0,nrx,nry)
    return angler+anglecorrection

#calcule la norme de la surface après une collision
def collision(x,y):
    nx=0
    ny=0
    if(y<=c_rayonball): #sol
        nx=0
        ny=1
        y=c_rayonball
    if (x>=c_lterrain-c_rayonball): #mur droit
        nx=-1
        ny=0
        x=c_lterrain-c_rayonball
    if (x<=c_rayonball): #mur gauche
        nx=1
        ny=0
        x=c_rayonball
    if (y>=c_hr-c_rayonball): #plafond
        nx=0
        ny=-1
        y=c_hr-c_rayonball
    return nx,ny,x,y

#calcule la trajectoire d'un projectile
def projectile(xi,yi,angle,vi,t):
    x=vi*math.cos(angle)*t+xi
    y=-c_g*(t**2/2)+vi*math.sin(angle)*t+yi
    return x,y

#effectue un shoot tant que la balle ne se cogne pas contre une surface
def shoot(v0,angle,x0,y0):
    t=0
    choc=0
    while choc==0: #tant qu'il n'y a pas de collision, la balle tombe
        time.sleep(0.01)
        t = t + 0.01
        xp,yp=projectile(x0,y0,angle,v0,t)
        vx,vy=vitesse(angle, v0, t)
        screen.fill((0, 0, 0))
        drawaxe()
        ball(xp, yp)
        nx,ny,xp,yp=collision(xp,yp) #determine s'il y a une collision
        choc=norme(nx,ny)

    return vx,vy,xp,yp,nx,ny

t=0
drawaxe()
v0=100 #parametre qu'on peut varier
x0=3   #parametre qu'on peut varier
y0=3   #parametre qu'on peut varier
#nx=0
#ny=0
ang=0.75 #parametre qu'on peut varier
while (v0>c_seuilv): 
    vx,vy,xp,yp,nx,ny=shoot(v0,ang,x0,y0)
    t = 0
    vc = norme(vx, vy)
    v0 = vc * c_amortissement
    anglereflex = anglereflexion(nx,ny,vx,vy)
    x0 = xp
    y0 = yp
    ang=anglereflex

#affiche la fenêtre de jeu
run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            print("Fermeture du jeu")




