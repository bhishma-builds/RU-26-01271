maze = [
    ['P', '.', '.', '#', '#'],
    ['#', '#', '.', '#', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', 'E']
]

def print_maze(r, c):
    print()
    for i in range(5):
        s = ""
        for j in range(5):
            if i == r and j == c:
                s = s + "P "
            elif maze[i][j] == 'P':
                s = s + ". "
            else:
                s = s + maze[i][j] + " "
        print(s)
    print()

def bfs():
    q = [[0, 0, 0]]
    vis = [[0, 0]]
    
    while len(q) > 0:
        curr = q.pop(0)
        r = curr[0]
        c = curr[1]
        d = curr[2]
        
        if r == 4 and c == 4:
            return d
            
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for x in dirs:
            nr = r + x[0]
            nc = c + x[1]
            
            if nr >= 0 and nr < 5 and nc >= 0 and nc < 5:
                if maze[nr][nc] != '#' and [nr, nc] not in vis:
                    vis.append([nr, nc])
                    q.append([nr, nc, d + 1])
                    
    return -1

def play():
    r = 0
    c = 0
    moves = 0
    
    print_maze(r, c)
    
    while True:
        inp = input("Move (W/A/S/D): ").upper()
        parts = inp.split(',')
        
        for p in parts:
            k = p.strip()
            if k == "":
                continue
                
            nr = r
            nc = c
            
            if k == 'W':
                nr = r - 1
            elif k == 'S':
                nr = r + 1
            elif k == 'A':
                nc = c - 1
            elif k == 'D':
                nc = c + 1
            else:
                print(f"Invalid key '{k}'. Use W, A, S or D only.")
                print(f"Moves counted: {moves}")
                continue
                
            if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                print(f"Cannot move outside the maze. Player stays at ({r}, {c}) | Moves: {moves}")
                continue
                
            if maze[nr][nc] == '#':
                print(f"Wall ahead. Move blocked. Player stays at ({r}, {c})")
                continue
                
            r = nr
            c = nc
            moves = moves + 1
            
            print_maze(r, c)
            
            if r == 4 and c == 4:
                print(f"You escaped the maze! Total moves: {moves}")
                return
            else:
                print(f"Player moved to (row {r}, col {c}) | Moves: {moves}")

while True:
    print("\n1. Play Maze Game")
    print("2. Shortest path")
    print("3. Exit")
    
    ch = input("Enter choice: ").strip()
    
    if ch == '1':
        play()
    elif ch == '2':
        ans = bfs()
        print(f"Shortest path length: {ans} steps")
    elif ch == '3':
        break
    else:
        print("Invalid choice")