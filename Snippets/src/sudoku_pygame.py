import pygame
from pygame.locals import *
import sys

WHITE = pygame.Color(255,255,255);
YELLOW = pygame.Color(255,255,0);
BLUE = pygame.Color(0,0,255);
RED = pygame.Color(255,0,0);
GREEN =  pygame.Color(0,255,0);
GREY = pygame.Color(100,100,100);
BLACK = pygame.Color(0,0,0);

pygame.init();
clock = pygame.time.Clock();
 
window = pygame.display.set_mode((450,450));
pygame.display.set_caption('Sudoku'); 
font = pygame.font.Font('freesansbold.ttf', 40);
 
mousex, mousey = 0, 0;
sel = (-1,-1);
 
# S = [[0 for _ in range(9)] for _ in range(9)];
S = "300200000000107000706030500070009080900020004010800050009040301000702000000008006"; # hard
S = list(S);
S = [[int(c) for c in S[9*n:9*(1+n)]] for n in range(9)];
Locked = [[1 if x else 0 for x in r] for r in S];
 
    
def mark_error():
    
    def check_9(l):
        tmp = [x for x in l if x != 0];
        s = set(tmp);
        if len(s) == len(tmp):
            return True;
        else:
            return False;
    
    for i in range(9):
        if not check_9(S[i]):
            pygame.draw.rect(window, RED, Rect(0,50*i,450,50), 0);
        if not check_9([s[i] for s in S]):
            pygame.draw.rect(window, RED, Rect(50*i,0,50,450), 0);
    for i in range(3):
        for j in range(3):
            if not check_9([x for s in S[3*i:3*(i+1)] for x in s[3*j:3*(j+1)]]):
                pygame.draw.rect(window, RED, Rect(150*j,150*i,150,150), 0);
    return True;
     
def draw():  
    # clear        
    window.fill(pygame.Color(255, 255, 255)); 
    # draw grid
    for i in range(10):
        w = 1;
        if i%3 == 0:
            w=3;
        pygame.draw.line(window,BLACK,(50*i,0),(50*i,450),w);
        pygame.draw.line(window,BLACK,(0,50*i),(450,50*i),w);
    # draw error area
    mark_error();
    # draw selection rectangle
    if sel[0] >= 0 and sel[0] < 9 and sel[1] >= 0 and sel[1] < 9:
        pygame.draw.rect(window, YELLOW, Rect(50*sel[1]+1,50*sel[0]+1,49,49), 0);
    # draw numbers
    for r in range(9):
        for c in range(9):      
            if S[r][c]:  
                if Locked[r][c]:
                    tmp_surface = font.render(str(S[r][c]), False, BLUE);
                else:    
                    tmp_surface = font.render(str(S[r][c]), False, BLACK);
                x_pos = 450/9*c + (50-tmp_surface.get_width())/2;
                y_pos = 450/9*r + (50-tmp_surface.get_height())/2;
                window.blit(tmp_surface, (x_pos,y_pos));
    pygame.display.update();
     
         
draw();
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
            sys.exit();
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos;
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:          
                c = mousex//50;
                r = mousey//50;
                if not Locked[r][c]:
                    sel = (r,c);
                    draw();
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                pass
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT));
            if sel[0] >= 0 and sel[0] < 9 and sel[1] >= 0 and sel[1] < 9:
                for i in range(10):
                    if event.key == eval('K_%d' % i) or event.key == eval('K_KP%d' % i):
                        S[sel[0]][sel[1]] = i;
                        draw();
    clock.tick(10);
       
       
