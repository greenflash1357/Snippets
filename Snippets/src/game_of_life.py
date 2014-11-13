import pygame
from pygame.locals import *
import random
import sys

X = 100;
Y = 100;


Map = [[0 for i in range(Y)] for i in range(X)]

def nextStep(Map):
    tmp = [[0 for i in range(Y)] for i in range(X)];
    for i in range(Y):
        for j in range(X):
            count = sum([Map[y][x] for x in [(j-1)%X,j,(j+1)%X] for y in [(i-1)%Y,i,(i+1)%Y]]);
            if count == 3 and not Map[i][j]:
                tmp[i][j] = 1;
            elif Map[i][j] and (count == 3 or count == 4):
                tmp[i][j] = 1;
            else:
                tmp[i][j] = 0;
    return tmp;
                    

pygame.init();
clock = pygame.time.Clock();

window = pygame.display.set_mode((X*5,Y*5));        
step = 0;       
pygame.display.set_caption('Game of Life - Step: %d' % (step));
mousex, mousey = 0, 0;

# Init
for x in range(40,55,1):
    for y in range(50,57,2):
        Map[y][x] = 1;
        
Map[18][20] = 1;
Map[18][21] = 1;
Map[19][20] = 1;
Map[19][21] = 1;

Map[10][10] = 1;
Map[10][11] = 1;
Map[10][12] = 1;
Map[9][12] = 1;
Map[8][11] = 1;

# Loop
while True:    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
            sys.exit(); 
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos;
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT));
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                j = (mousex-1)//5;
                i = (mousey-1)//5;
                for x in [(j-2)%X,(j-1)%X,j,(j+1)%X,(j+2)%X]:
                    for y in [(i-2)%Y,(i-1)%Y,i,(i+1)%Y,(i+2)%Y]:
                        if random.random() < 0.5:
                            Map[y][x] = 1;
                        else:
                            Map[y][x] = 0;
    
    # step + drawing
    window.fill(pygame.Color(255, 255, 255));    
    for i in range(Y):
        row = Map[i];
        if any(row):
            for j in range(X):
                if row[j]:
                    pygame.draw.rect(window, (0,0,0), (j*5, i*5, 5, 5), 0);
    
    pygame.display.update();
    Map = nextStep(Map);
    clock.tick(8);
    step += 1;
    pygame.display.set_caption('Game of Life - Step: %d' % (step));
    
    
                