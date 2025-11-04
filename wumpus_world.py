import random

class WumpusWorld:
    def __init__(self, n=4, random_state=None):
        random.seed(random_state)
        self.n = n
        self.world = [[[] for _ in range(n)] for _ in range(n)]  # grid to store hazards/perceptions
        self.agent_pos = (0, 0)  # agent starts at bottom-left
        self.agent_dir = 0  # 0=right, 1=up, 2=left, 3=down
        self.gold_pos = None
        self.wumpus_pos = None
        self.alive = True
        self.has_gold = False
        
        # place pits with 0.2 probability (except agent start position)
        for i in range(n):
            for j in range(n):
                if (i, j) != (0, 0) and random.random() < 0.2:
                    self.world[i][j].append('P')
        
        # place wumpus randomly (not at agent start)
        while True:
            x, y = random.randint(0, n-1), random.randint(0, n-1)
            if (x, y) != (0, 0) and 'P' not in self.world[x][y]:
                self.world[x][y].append('W')
                self.wumpus_pos = (x, y)
                break
        
        # place gold randomly (not at agent start, can be with hazards)
        while True:
            x, y = random.randint(0, n-1), random.randint(0, n-1)
            if (x, y) != (0, 0):
                self.world[x][y].append('G')
                self.gold_pos = (x, y)
                break
        
        # add perceptions (breeze near pits, stench near wumpus)
        for i in range(n):
            for j in range(n):
                if 'P' not in self.world[i][j] and 'W' not in self.world[i][j]:  # only if no hazard
                    neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
                    for ni, nj in neighbors:
                        if 0 <= ni < n and 0 <= nj < n:
                            if 'P' in self.world[ni][nj] and 'B' not in self.world[i][j]:
                                self.world[i][j].append('B')
                            if 'W' in self.world[ni][nj] and 'S' not in self.world[i][j]:
                                self.world[i][j].append('S')
    
    def print_world(self):
        dirs = ['>', '^', '<', 'v']
        for i in range(self.n-1, -1, -1):  # print from top to bottom
            row = []
            for j in range(self.n):
                cell = []
                # show agent if at this position
                if (i, j) == self.agent_pos and self.alive:
                    cell.append(dirs[self.agent_dir])
                # show hazards and perceptions
                cell.extend(self.world[i][j])
                row.append(''.join(cell) if cell else '.')
            print(' '.join(f'{c:4s}' for c in row))
        print()
    
    def move(self, action):
        if not self.alive or self.has_gold:
            print("Game over!")
            return
        
        if action == 'left':  # turn left
            self.agent_dir = (self.agent_dir + 1) % 4
        elif action == 'right':  # turn right
            self.agent_dir = (self.agent_dir - 1) % 4
        elif action == 'forward':  # move forward
            x, y = self.agent_pos
            dx, dy = [(0,1), (-1,0), (0,-1), (1,0)][self.agent_dir]  # direction vectors
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < self.n and 0 <= ny < self.n:  # check bounds
                self.agent_pos = (nx, ny)
                
                # check for hazards
                if 'P' in self.world[nx][ny]:
                    print("You fell into a pit! Game over.")
                    self.alive = False
                elif 'W' in self.world[nx][ny]:
                    print("You were eaten by the Wumpus! Game over.")
                    self.alive = False
                elif 'G' in self.world[nx][ny] and not self.has_gold:
                    print("You grabbed the gold! You win!")
                    self.has_gold = True
            else:
                print("Can't move forward - wall!")
        else:
            print("Invalid action! Use: 'left', 'right', 'forward'")

if __name__ == "__main__":
    game = WumpusWorld(n=4, random_state=42)
    print("Wumpus World - Commands: 'left', 'right', 'forward'")
    print("Legend: > < ^ v = agent, P = pit, W = wumpus, G = gold, B = breeze, S = stench\n")
    
    game.print_world()
    
    # example moves
    moves = ['forward', 'forward', 'left', 'forward', 'forward']
    for move in moves:
        print(f"Action: {move}")
        game.move(move)
        game.print_world()
        if not game.alive or game.has_gold:
            break
