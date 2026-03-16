import time
import os

N = 4
board = [["." for _ in range(N)] for _ in range(N)]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    clear()
    for row in board:
        print(" ".join(row))
    print("\n")
    time.sleep(0.3)

def is_safe(row, col):
    # cek kolom
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # diagonal kiri atas
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # diagonal kanan atas
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solve(row):
    if row == N:
        print("SOLUSI DITEMUKAN!")
        print_board()
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = "Q"
            print_board()

            if solve(row + 1):
                return True

            # backtracking
            board[row][col] = "."
            print_board()

    return False

solve(0)
