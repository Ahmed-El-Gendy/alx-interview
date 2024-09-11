#!/usr/bin/python3
"""
Queens problem
"""

import sys


def valid_board(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


board = []


def rec(board, col, N, solutions):
    """
    Recursive function
    """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for i in range(N):
        if valid_board(board, i, col, N):
            board[i][col] = 1
            rec(board, col + 1, N, solutions)
            board[i][col] = 0


def solve_queens(N):
    """
    Solve the N queens problem
    """
    for i in range(N):
        board.append([0] * N)
    solutions = []
    rec(board, 0, N, solutions)
    return solutions


def main():
    """
    Main Function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = solve_queens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
