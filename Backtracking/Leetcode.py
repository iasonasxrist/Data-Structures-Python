# 62. Unique Paths

class Solution():
    def uniquePaths(self, m , n):

        memo = [[ -1 for _ in range(m+1)] for _ in range(n+1)]
        def myPath(m, n):

            if m ==0 or n == 0:
                return 0
            if m == 1 and n == 1:
                return 1
            
            if memo[m][n] !=-1:
                return memo[m][n]

            memo[m][n] = myPath(m-1, n) + myPath(m, n - 1)

            return memo[m][n]
            
        paths = myPath(m, n)
        return paths



n_cols = 3
n_rows = 3
solution = Solution()
print(solution.uniquePaths(n_rows, n_cols))




# 63. Unique Paths II

class Solution2(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # Create a memoization table to store already calculated results
        memo = [[-1] * cols for _ in range(rows)]

        def mazeWithObstacle(r, c):
            # Check if already calculated
            if memo[r][c] != -1:
                return memo[r][c]

            # Base case: Bottom-Right Corner
            if r == rows - 1 and c == cols - 1 and obstacleGrid[r][c] == 0:
                return 1

            # Obstacle at the current cell
            if obstacleGrid[r][c] == 1:
                return 0

            paths = 0

            # Move right
            if c < cols - 1:
                paths += mazeWithObstacle(r, c + 1)

            # Move down
            if r < rows - 1:
                paths += mazeWithObstacle(r + 1, c)

            # Save the result in the memo table
            memo[r][c] = paths

            return paths

        return mazeWithObstacle(0, 0)
    
solution2 = Solution2()

obstacleGrid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
result = solution2.uniquePathsWithObstacles(obstacleGrid)
print("Total unique paths to Bottom-Right Corner:", result)



# ******* Complexity Analysis ************
# 51. N-Queens

# Time Complexity O(N!)
# Bad Complexity Algorithm
# Best Solution is Dynamic Programming

def queens(board, row):

    if (row == len(board)):
        # print(board)
        display(board)
        
        return 1

    count=0

    for col in range(len(board[0])):
        if (isSafe(board,row, col)):
            board[row][col] = True
            count += queens(board, row+1)
            board[row][col] = False
        
    return count


def isSafe(board, row, col):

    # check vertical rows
    for i in range(len(board)):
        if board[i][col]:
            return False
   
    
    # Diagonal Left
    maxLeft = min(row, col)
    for i in range(1,maxLeft+1):
        if board[row-i][col-i]:
            return False
    
    # Diagonal Right
    maxRight= min(row, len(board) - col - 1)
    for i in range(1,maxRight+1):
        if board[row-i][col+i]:
            return False

    return True


def display(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]:
                print("Q", end=" ")
            else:
                print("X", end=" ")
        print("")

    print("")

n = 4
board = [[ False for _ in range(n)] for _ in range(n)]


# print(queens(board,0))

# Knight Tour

def knight(board, row, col, knights):
    if knights == 0 :
        display(board)
        print("")

    if (col == len(board[0])-1):
        knight(board, row+1, 0, knights)
        return
    if (row ==len(board)-1 and col== len(board[0])-1):
        return;

    if isSafe(board, row, col):
        board[row][col] = True
        knight(board, row, col+1, knights - 1)
        board[row][col] =False

    knight(board, row, col+1, knights)


def isSafe(board, row, col):
    if isCheck(board, row-2, col-1):
        if board[row-2][col-1]:
            return False

    if isCheck(board, row-1, col-2):
        if board[row-1][col-2]:
            return False
        
    if isCheck(board,  row-2, col+1):
        if board[row-2][col+1]:
            return False
        
    if isCheck(board, row-1, col+2):
        if board[row-1][col+2]:
            return False
        
    return True

def isCheck(board,col, row):
   return 0 <= row < len(board) and 0 <= col < len(board[0])

n = 4
board = [[ 0 for _ in range(n)] for _ in range(n)]

# print(knight(board, 0, 0, 4))

# Debug later
import random

def sudoku(board):

    n = len(board)
    row =-1
    col =-1

    emptyLeft = True
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                row = i
                col = j
                emptyLeft = False
                break;
    
        if emptyLeft ==  False:
            break;
    
    if emptyLeft == True:
        return True
    

 
    for number in range(1,10):
        if isSafe(board, row, col, number):
            board[row][col] = number
            if sudoku(board):
                displaySudoku(board)
                return True
        else:
            board[row][col] = 0
    
    return False




def isSafe(board, row, col, num):
    # check row
    for i in range(len(board)):
        if board[i][col] == num:
            return False
    
    # check col
    for col in range(len(board[0])):
        if board[row][col] == num:
            return False
   

    # check square 3x3
    sqrt = int(len(board) ** 0.5)

    rowStart = row - row % sqrt
    rowEnd = col - col % sqrt

    for rowStart in range(rowStart + sqrt):
        for rowEnd in range (rowEnd + sqrt):
            if board[row][col] == num:
                return False

    return True


def displaySudoku(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            print( board[row][col], end="")

        print("")

    print("")
# n = 8

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# print(sudoku(board))

# 2596. Check Knight Tour Configuration

# ******* Complexity Analysis ************
# Time Complexity O(8^(N^2))
# Bad Complexity Algorithm
# Best Solution is Dynamic Programming


class Solution(object):

    def checkValidGrid(self, grid):

        def isSafeCheck(row, col, grid):

            if (0<=row<len(grid) and 0<=col<len(grid)):
                return True
            return False
    
        def display(grid):
            for i in range(len(grid)): 
                for j in range(len(grid)): 
                    print(grid[i][j], end=' ') 
            print() 


        move_x = [-2, -2, +2, +2, -1, -1, +1, +1]
        move_y = [-1, +1, -1, +1, -2, +2, -2, +2]

        
        
        def checkTour(grid, row, col, step):

            if step == len(grid)**2:
                display(grid)
                print("There is a solution")
                return True
            
            for index in range(len(move_x)):
                rowNew = row + move_x[index]
                colNew = col + move_y[index]
                print("row",rowNew, colNew)

                if isSafeCheck(rowNew,colNew, grid) and grid[rowNew][colNew] == -1:

                    grid[rowNew][colNew] = step
                    print(grid)
                    
                    if (checkTour(grid, rowNew, colNew, step+1)):
                        return True
                    
                    grid[rowNew][colNew] = -1
            return False

        return checkTour(grid, 0, 0, 0)
        

n=5
grid = [[-1 for _ in range(n)] for _ in range(n)]
grid[0][0] = 0
# sol = Solution()
# print(sol.checkValidGrid(grid))

# result
# [[0, -1, -1, 12, -1],
# [-1, 11, 0, -1, -1], 
# [-1, -1, 7, 4, 1], 
# [10, 5, 2, -1, 8], 
# [-1, -1, 9, 6, 3]]
