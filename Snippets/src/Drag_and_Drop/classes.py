import pygame
from static import *

class Ball():
    
    _x = 0;
    _y = 0;
    _color = pygame.Color(0,0,0);
    _alive = True;
    
    def __init__(self, x,y, color=YELLOW):
        self._x = x;
        self._y = y;
        self._color = color;
        self._alive = True;
        
    def is_clicked(self, x,y):
        if ((x-self._x)**2 + (y-self._y)**2) < 100:
            return True;
        return False;
    
    def hits_hole(self, x,y):
        if ((x-self._x)**2 + (y-self._y)**2) < 25:
            return True;
        return False;
    
    def hits_ball(self, x,y):
        if ((x-self._x)**2 + (y-self._y)**2) < 400:
            return True;
        return False;
        
    def position(self):
        return (self._x, self._y);        
        
    def drag(self, x,y):
        self._x = x;
        self._y = y;
        return True;
    
    def push(self, dx,dy):
        self._x += dx;
        self._y += dy;
        return True;
        
    def draw(self, surface):
        if self._alive:
            pygame.draw.circle(surface, self._color, (self._x,self._y), 10, 0);
        return True;
    
class Hole():
    
    _x = 0;
    _y = 0;
    _color = pygame.Color(0,0,0);
    
    def __init__(self, x,y, color=YELLOW):
        self._x = x;
        self._y = y;
        self._color = color;
        
    def position(self):
        return (self._x, self._y);
    
    def draw(self, surface):
        pygame.draw.circle(surface, self._color, (self._x,self._y), 15, 5);
        pygame.draw.circle(surface, GREY, (self._x,self._y), 11, 0);
        return True;
    
class Wall():
    
    _x1 = 0;
    _y1 = 0;
    _x2 = 0;
    _y2 = 0;
    
    def __init__(self, x1,y1, x2,y2):
        self._x1 = x1;
        self._y1 = y1;
        self._x2 = x2;
        self._y2 = y2;
        
    def position(self):
        return (self._x1, self._y1, self._x2, self._y2);
    
    def draw(self, surface):
        pygame.draw.line(surface, GREY, (self._x1,self._y1), (self._x2,self._y2), 3);
        return True;