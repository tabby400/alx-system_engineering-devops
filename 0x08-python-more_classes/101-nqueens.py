#!/usr/bin/python3

"""involved in the  solving ofN-queens puzzle.
finds all of the possible solutions to placing N
N has to be an integer greater than or equal to 4."""


import sys


def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        #  is it safe to place a queen at board[row][col]

        for p in range(col):
            if board[row][p] == "Q":
                return False

        p = row
        k = col
        while p >= 0 and k >= 0:
            if board[p][k] == "Q":
                return False

            p = p - 1
            k = k - 1

        p = row
        k = col
        while p < N and k >= 0:
            if board[p][k] == "Q":
                return False

            p = p + 1
            k = k - 1

        return True

    def solve_nqueens(board, col):

        if col >= N:
            print_solution(board)
            return True

        for row in range(N):
            if is_safe(board, row, col):
                board[row][col] = "Q"
                solve_nqueens(board, col + 1)
                board[row][col] = "."

    def print_solution(board):
        for row in board:
            print(" ".join(row))
        print()

    board = [["." for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
