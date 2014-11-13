
##### Sudoku solver ##### 

import copy
import time


# S = "538016079000380541241500000060900000000035090090004002600200930129040050054690008"; # easy
# S = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"; # easy
# S = "300200000000107000706030500070009080900020004010800050009040301000702000000008006"; # hard
# S = list(S);
# S = [[int(c) for c in S[9*n:9*(1+n)]] for n in range(9)];

steps = 0;
solution = [];

def is_filled(S):
    return all((all(s) for s in S));

def solved(S):
    if is_filled(S):
        return check_solution(S);
    else:
        return False;
    

def is_solved(P):
    for i in range(9):
        for j in range(9):
            if len(P[i][j])!=1:
                return False;
    return True;

def check_solution(S):
    
    def check_9(l):
        tmp = [x for x in l if x != 0];
        s = set(tmp);
        if len(s) == len(tmp):
            return True;
        else:
            return False;
    
    for i in range(9):
        if not check_9(S[i]):
            return False;
        if not check_9([s[i] for s in S]):
            return False;
    for i in range(3):
        for j in range(3):
            if not check_9([x for s in S[3*i:3*(i+1)] for x in s[3*j:3*(j+1)]]):
                return False;
    return True;

def pretty_print(S):
    print('Current State after %d steps: ' % steps)
    for i in range(9):
        print(S[i]);


def possibilities(S):
    P = [[list(range(1,10)) for _ in range(9)] for _ in range(9)];
    for i in range(9):
        for j in range(9):
            if S[i][j]:
                P[i][j] = [S[i][j]];
                update_possibles(P,i,j,S[i][j]);
    return P;

def update_possibles(P,i,j,n):
    #line
    for k in range(9):
        if k != j and n in P[i][k]:
            P[i][k].remove(n);
            if len(P[i][k]) == 1:
                update_possibles(P,i,k,P[i][k][0]);
    #column
    for k in range(9):
        if k != i and n in P[k][j]:
            P[k][j].remove(n);
            if len(P[k][j]) == 1:
                update_possibles(P,k,j,P[k][j][0]);
    #square
    for r in range(3*(i//3),3*((i//3)+1)):
        for c in range(3*(j//3),3*((j//3)+1)):
            if r != i and c != j and n in P[r][c]:
                P[r][c].remove(n);
                if len(P[r][c]) == 1:
                    update_possibles(P,r,c,P[r][c][0]);
        

def still_possible(P):
    return(all(all(s) for s in P));
    

def guesses(P):
    best = (0,0);
    l = 10;
    for i in range(9):
        for j in range(9):
            if len(P[i][j]) < l and len(P[i][j]) >= 2:
                best = (i,j);
                l = len(P[i][j]);
    for i in P[best[0]][best[1]]:
        tmp = copy.deepcopy(P);
        tmp[best[0]][best[1]] = [i];
        update_possibles(tmp,best[0],best[1],i);
        if still_possible(tmp):
            yield copy.deepcopy(tmp);
        
def step(P):    
    global steps
    global solution
    steps += 1;
    #pretty_print(P);
    if is_solved(P):
        solution = copy.deepcopy(P);
    else:
        for tmp in guesses(P):
            step(tmp);
                
def solve(S):
    P = possibilities(S);
    #pretty_print(P);
    step(P);
    S = [[0 for _ in range(9)] for _ in range(9)];
    for i in range(9):
        for j in range(9):
            S[i][j] = solution[i][j][0];
    return S;
                

start = time.time();
f = open('C:\\Users\\Gesteb-Keller\\Downloads\\p096_sudoku.txt');
grids = f.read();
f.close();
grids = grids.replace('\n','').split('Grid ');
grids = grids[1:]
grids = [(g[0:2],g[2:]) for g in grids];
res = 0;
for (n,grid) in grids:
    steps = 0;
    S = list(grid);
    S = [[int(c) for c in S[9*n:9*(1+n)]] for n in range(9)];
    print('Grid %s' % (n));
    pretty_print(S);    
    S = solve(S);     
    print('Solved: %r; After %d steps' % (solved(S), steps));            
    pretty_print(S);   
    r = ''.join(str(s) for s in S[0][0:3]);
    res += int(r);
    
print('Solution for PE96: %d' % res)
print('Time: %f seconds' % (time.time()-start))
