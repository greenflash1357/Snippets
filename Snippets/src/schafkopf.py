import random


suits = ['Eichel', 'Gras', 'Herz', 'Schellen'];
values = ['Ass', '10', 'Koenig', 'Ober', 'Unter', '9', '8', '7'];
pips_dict = {'Ass': 11, '10': 10, 'Koenig': 4, 'Ober': 3, 'Unter': 2, '7': 0, '8': 0, '9': 0};


def pips_of_cardlist(cards=None):
    if cards == None:
        cards = [];
    res = 0;
    for card in cards:
        res += card.pips;
    return res;


class Player():
            
    def __str__(self):
        return str(self.__dict__)
    
    hand = [];
    tricks = [];
    pips = 0;
    
    
class Card():
    
    def __init__(self, suit, value):
        self.suit = suit;
        self.value = value;
        self.pips = pips_dict[value];
        
    def __str__(self):
        return self.suit + ' ' + self.value;
    
    suit = '';
    value = '';
    pips = 0;


class Game():
    
    def __init__(self):
        self.deck = [Card(s, v) for s in suits for v in values];
        random.shuffle(self.deck);
        self.players = [Player() for n in range(4)];
           
    def generate_order(self, mode='Sauspiel', trump='Herz'):
        ober = [('Eichel','Ober'), ('Gras','Ober'), ('Herz', 'Ober'),('Schellen','Ober')];
        unter = [('Eichel','Unter'), ('Gras','Unter'), ('Herz','Unter'),('Schellen','Unter')];
        value_order = ['Ass', '10', 'Koenig', 'Ober', 'Unter', '9', '8', '7'];
        if mode in ['Solo', 'Sauspiel']:
            value_order.remove('Ober');
            value_order.remove('Unter');
            trump_order = ober + unter;
        if mode == 'Geier':
            value_order.remove('Ober');
            trump_order = ober;
        if mode in ['Wenz', 'Farbwenz']:
            value_order.remove('Unter');
            trump_order = unter;
        if mode not in ['Geier', 'Wenz']:
            trumps = [(trump, v) for v in value_order];
            trump_order += trumps;
            
        self.trump_order = trump_order;
        self.value_order = value_order;
        return True;
    
    def winner_of_trick(self, trick, suit_to_follow):
        trumps = [card for card in trick if (card.suit, card.value) in self.trump_order];
        if trumps:
            winner = min(trumps, key=lambda x: self.trump_order.index((x.suit, x.value)));
        else:
            suited = [card for card in trick if card.suit == suit_to_follow];
            winner = min(suited, key=lambda x: self.value_order.index(x.value));
        return trick.index(winner);
    
    mode = '';
    trump = '';
    deck = [];
    players = [];
    trump_order = [];
    value_order = [];
    teams = [];
    last_trick = [];
    
    


game = Game();
    
# 10 tricks..
for n in range(1):
    # first 4 cards
    for n in range(4):
        game.players[n].hand = game.deck[n*4:(1+n)*4];
        
    #TODO: klopfen?
    
    # next 4 cards
    for n in range(4):
        game.players[n].hand += game.deck[(4+n)*4:(5+n)*4];
        
    #TODO: mode?
    game.mode = 'Sauspiel';
    game.trump = 'Herz';
    game.teams = [[0,3], [1,2]];
    game.generate_order(game.mode, game.trump);
    
    #TODO: select card; first player; follow suit
    trick = [p.hand.pop(random.randint(0,9-n)) for p in game.players];
    if (trick[0].suit, trick[0].value) in game.trump_order:
        first_suit = 'Trump';
    else:
        first_suit = trick[0].suit;
    print(first_suit);
    for card in trick:
        print(card); 

    # determine winner of trick
    winner_idx = game.winner_of_trick(trick, first_suit);
    print('Player %d won!' % winner_idx)
    
    game.last_trick = trick;
    game.players[winner_idx].tricks.append(trick)    
    game.players[winner_idx].pips += pips_of_cardlist(trick);
    
    #TODO: set new starting player
    
    
    