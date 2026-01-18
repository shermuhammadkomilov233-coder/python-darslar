import random
import os

def start_game():
    mat = [['0'] * 4 for _ in range(4)]
    add_new_2(mat)
    add_new_2(mat)
    return mat

def add_new_2(mat):
    r, c = random.randint(0, 3), random.randint(0, 3)
    while mat[r][c] != '0':
        r, c = random.randint(0, 3), random.randint(0, 3)
    mat[r][c] = random.choice(['2', '4'])

def compress(mat):
    new_mat = [['0'] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != '0':
                new_mat[i][pos] = mat[i][j]
                pos += 1
    return new_mat

def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != '0':
                mat[i][j] = str(int(mat[i][j]) * 2)
                mat[i][j+1] = '0'
    return mat

def reverse(mat):
    return [row[::-1] for row in mat]

def transpose(mat):
    return [list(row) for row in zip(*mat)]

def move_left(grid):
    grid = compress(grid)
    grid = merge(grid)
    grid = compress(grid)
    return grid

def move_right(grid):
    grid = reverse(grid)
    grid = move_left(grid)
    grid = reverse(grid)
    return grid

def move_up(grid):
    grid = transpose(grid)
    grid = move_left(grid)
    grid = transpose(grid)
    return grid

def move_down(grid):
    grid = transpose(grid)
    grid = move_right(grid)
    grid = transpose(grid)
    return grid

def print_grid(grid):
    print("-" * 21)
    for row in grid:
        print("|", end="")
        for val in row:
            print(f"{val if val != '0' else '.':^4}|", end="")
        print("\n" + "-" * 21)

# O'yinning asosiy qismi
grid = start_game()
print("--- 2048 O'YINI ---")
print("Boshqarish: W (tepa), S (past), A (chap), D (o'ng)")

while True:
    print_grid(grid)
    move = input("Harakatni kiriting: ").lower()
    
    old_grid = [row[:] for row in grid]
    
    if move == 'w': grid = move_up(grid)
    elif move == 's': grid = move_down(grid)
    elif move == 'a': grid = move_left(grid)
    elif move == 'd': grid = move_right(grid)
    elif move == 'exit': break
    else:
        print("Xato buyruq! W, A, S, D dan foydalaning.")
        continue

    if grid != old_grid:
        add_new_2(grid)
    
    # Yutqazganini tekshirish (sodda ko'rinishda)
    empty = any('0' in row for row in grid)
    if not empty:
        print("O'yin tugadi!")
        break
