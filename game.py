import random

BOMB = '\U0001f4a3'
FLAG = '🚩'
UNOPENED = '~'

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def print_color(text, color_code="0"):
    print(f"\033[{color_code}m{text}\033[0m")

def displayMap(Map):
    print("\n   " + " ".join([f"{i:2}" for i in range(len(Map))]))
    for i, row in enumerate(Map):
        print(f"{i:2} | " + " ".join(f"{str(cell):2}" for cell in row))
    print()

def mindSweeper(n, k):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    bomb_set = set()

    while len(bomb_set) < k:
        x, y = random.randint(0, n - 1), random.randint(0, n - 1)
        if (x, y) not in bomb_set:
            bomb_set.add((x, y))
            grid[x][y] = BOMB

    for x, y in bomb_set:
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != BOMB:
                grid[nx][ny] += 1
    return grid

