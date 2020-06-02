#! /usr/bin/env python3
from sys import exit

grid = [[7, 0, 6, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 4, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 0, 0, 4],
        [0, 0, 5, 0, 0, 6, 0, 0, 0],
        [6, 2, 0, 0, 0, 0, 0, 8, 3],
        [0, 0, 0, 9, 0, 0, 1, 0, 0],
        [8, 0, 0, 0, 7, 0, 0, 9, 0],
        [5, 0, 0, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 7, 0, 2]]

# grid = []


def init():

    for y in range(9):
        a = []
        for x in range(9):
            print("Input Number At Row " + str(y) +
                  ", Column " + str(x), end=": ", flush=True)
            try:
                info = int(input())
                if info < 0 or info > 9:
                    info = invalid(y, x)
            except ValueError:
                info = invalid(y, x)
            except KeyboardInterrupt:
                print("[-] Closing Program...")
                exit()
            a.append(info)
        grid.append(a)


def invalid(y, x):
    not_valid = True
    while not_valid:
        print("Invalid Entry. Please Re-Enter number at Row " +
              str(y) + ", Column " + str(x), end=": ", flush=True)
        try:
            info = int(input())
            if info < 0 or info > 9:
                continue
            else:
                return info
        except ValueError:
            continue
        except KeyboardInterrupt:
            print("\n[-] Closing Program...")
            exit()


def print_grid():
    print()
    for y in range(9):
        if y == 3 or y == 6:
            print("- - - - - - - - - - -")
        for x in range(9):
            if x == 3 or x == 6:
                print("| ", end="")
            print(str(grid[y][x]), end=" ")
        print()
    print()


def possible(y, x, n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x//3) * 3
    y0 = (y//3) * 3

    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print_grid()
    input("Find Next Solution? [Enter] ")
    print()


def main():
    ans = input(
        "Type 'Test' to to see a test puzzle, type anything else to input puzzle: ")
    if ans.lower() != "test":
        init()
    print("\nPuzzle to be solved: \n")
    print_grid()
    print("\n")
    solve()
    print("Couldn't find any more solutions")


if __name__ == "__main__":
    main()
