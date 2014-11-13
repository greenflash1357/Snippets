from classes import *
from static import *

level_dict = {
    1: {
        'balls': [Ball(200,200,RED)],
        'holes': [Hole(400,400,RED)], 
        'walls': [], },

    2: {    
        'balls': [Ball(40,40,RED)],
        'holes': [Hole(40,400,RED)],
        'walls': [], },
              
    3: {    
        'balls': [Ball(540,340,GREEN), Ball(440,40,GREEN)],
        'holes': [Hole(40,250,GREEN)],
        'walls': [], },
    
    4: {        
        'balls': [Ball(500,100, YELLOW), Ball(100,100, RED), Ball(300,200, GREEN)],
        'holes': [Hole(200,150, BLUE), Hole(50,450, YELLOW), Hole(500,400, RED), Hole(400, 50, YELLOW)],
        'walls': [Wall(420,250, 490, 290), Wall(370,40, 400,70), Wall(430,40, 400,70)], },
}