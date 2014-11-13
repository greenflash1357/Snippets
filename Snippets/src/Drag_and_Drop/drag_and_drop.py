import sys
import math
import pygame
from pygame.locals import *
from level import level_dict
from classes import *
from static import *

WIDTH = 640;
HEIGHT = 480;

def time_to_string(time):
    s, ms = divmod(time,1000);
    ms //= 10;
    return '%02d:%02d' % (s,ms);
            

def line_segment_intersect(bx1,by1, bv, wx1,wy1, wx2,wy2):
    w1 = pygame.math.Vector2(wx1,wy1);
    w2 = pygame.math.Vector2(wx2,wy2);
    b1 = pygame.math.Vector2(bx1,by1);
    denom = (w2-w1).cross(bv);
    nom1 = (b1-w1).cross(w2-w1);
    nom2 = (b1-w1).cross(bv)
    if denom:
        r = nom1/denom;
        t = nom2/denom;
        if r > 0 and r <= 1 and t > 0 and t <= 1:
            return r;
    elif not nom1:
        # this is the collinear case 
        # WHOOPS ;-)
        return False;
    else:
        return False;
      
def balls_collision_detection(moved):
    global drag;
    for ball in balls:
        if ball._alive and moved != ball and moved.hits_ball(*ball.position()):
            d = pygame.math.Vector2(tuple(map(lambda a, b: a - b, ball.position(), moved.position())));
            v = d.normalize() * 20 - d;
            if walls_collision_detection(ball, v):
                drag = False;
            else:
                ball.push(math.ceil(v.x), math.ceil(v.y));   
                holes_collision_detection(ball); 
                balls_collision_detection(ball);
    return True; 
    
def holes_collision_detection(moved):
    global score;
    for hole in holes:
        if moved._color == hole._color and moved.hits_hole(*hole.position()):
            if moved._alive:
                chime.play();
                score += 1;
            moved._alive = False;
    return True;

def walls_collision_detection(moved, vec):
    x,y = moved.position();
    if vec.length() == 0:
        return False;
    vec = vec + vec.normalize()*10;
    for wall in walls:
        hit = line_segment_intersect(x,y, vec, *wall.position());
        if hit:
            v = vec*hit;
            v = v-v.normalize()*10;
            moved.push(math.floor(v.x), math.floor(v.y));
            return True;
    return False;


pygame.init();
clock = pygame.time.Clock();

window = pygame.display.set_mode((WIDTH,HEIGHT));

chime = pygame.mixer.Sound('data/sounds/chime.wav');
fanfare = pygame.mixer.Sound('data/sounds/fanfare.wav');

mousex, mousey = 0, 0;
drag = False

# Load
save_file = open('data/save.txt', 'r+');
lvl = int(save_file.readline());
score = int(save_file.readline());
score_file = open('data/score.txt', 'r+');

time_font = pygame.font.Font('freesansbold.ttf', 20);

for level in list(range(lvl,max(level_dict.keys())+1)):

    # Set Level
    pygame.display.set_caption('Level: %d - Score: %d' % (level,score)); 
    balls = level_dict[level]['balls'];
    holes = level_dict[level]['holes'];
    walls = level_dict[level]['walls'];
    time = 0;
    
    while any([ball._alive for ball in balls]):
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit();
                sys.exit();
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos;
                if drag:
                    x,y = drag.position();
                    if walls_collision_detection(drag, pygame.math.Vector2(mousex-x, mousey-y)):
                        drag = False;
                    else:                    
                        drag.drag(*event.pos);
                        holes_collision_detection(drag); 
                        balls_collision_detection(drag);
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for ball in balls:
                        if ball._alive and ball.is_clicked(*event.pos):
                            drag = ball;
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    drag = False;
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT));
                if event.key == K_p:
                    pause_time = pygame.time.get_ticks();
                    pause_surface = pygame.font.Font('freesansbold.ttf', 58).render('PAUSE', False, BLACK);
                    window.blit(pause_surface, ((WIDTH-pause_surface.get_width())//2, (HEIGHT-pause_surface.get_height())//2));
                    pygame.display.update();
                    while True:
                        unpause = pygame.event.wait();
                        if unpause.type == KEYDOWN and unpause.key == K_p:
                            time += pause_time - pygame.time.get_ticks();
                            break;
        
        
        window.fill(pygame.Color(220, 245, 255));    
        pygame.display.set_caption('Level: %d - Score: %d' % (level,score));      
        for obj in holes+balls+walls:
            obj.draw(window);    
        time_surface = time_font.render(time_to_string(time), False, BLACK);
        window.blit(time_surface, (WIDTH-time_surface.get_width(),0));
        pygame.display.update();
        time += clock.tick(30);
        
    #Level Done
    fanfare.play();
    save_file.seek(0);
    save_file.write(str(level+1)+'\n');
    save_file.write(str(score));
    score_file.seek(0);
    data = score_file.readlines();
    #new score
    if len(data) < level:
        data.append('%d %s\n' % (level, time_to_string(time)));
    #better score
    elif data[level-1].split()[1] > time_to_string(time):
        data[level-1] = '%d %s\n' % (level, time_to_string(time));
    score_file.seek(0);
    score_file.writelines(data);
    

#End Game
save_file.close();   
score_file.close();
