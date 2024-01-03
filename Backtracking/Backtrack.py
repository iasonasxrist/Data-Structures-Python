# Backtracking Tutorial

# 1. Simple Maze
# 2. Pad Maze
# 3. Make with Obstacles 

def count(r, c, p):

    li = []
    if r==1 and c==1:
        li.append(p)
        return li
    
    if (r > 1):
        li.append(count(r-1, c, p + "U"))
    
    if (c > 1):
        li.append( count(r, c-1, p + "L"))
    
    return li
# print(count(3, 3, ""))

# Variation with Obstacle
def mazeWithObstacle(r, c, path):
            
              # base case
            if r == 1 or c == 1:
                print(path)
                return
            
            # obstacle
            if (r == 1 and c == 2):
                return
            
            # left
            if r > 1 :
                mazeWithObstacle(r - 1, c, path + "U")

            # right
            if c >1 :
                mazeWithObstacle(r, c - 1, path + "L")

            # diagonal
            if c > 1 and r > 1:
                mazeWithObstacle(r - 1, c - 1, path + "D")


# print(mazeWithObstacle(3, 3, ""))

maze= [ [True, True, True],
        [True, True, True],
        [True, True, True],
        [True, True, True]
    ]
                
def allPath(p, maze, r, c, path, step):
     
    if r ==len(maze) -1  and c == len(maze[0]) -1 :
        
        for i in path:
            print(i)
            # print("\n")
        print("maze", maze)
        return 

    if ( not maze[r][c]):
        return
    

    maze[r][c] = False
    path[r][c] = step

    if (r < len(maze) -1 ):
        allPath(p +"D", maze, r+1, c, path,  step+1)

    if (c < len(maze[0]) -1 ):
        allPath(p +"R", maze, r, c+1,path , step+1)
    
    if (c > 0):
        allPath(p +"L", maze, r, c-1,path , step+1)
    
    if (r > 0):
        allPath(p +"U", maze, r-1, c,path,  step+1)

    maze[r][c] = True
    path[r][c] = 0
    return path

arr = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    
print(allPath("", maze, 0, 0, arr, 1))


class Solution(object):
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

# Testing the code
solution = Solution()
obstacleGrid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
result = solution.uniquePathsWithObstacles(obstacleGrid)
print("Total unique paths to Bottom-Right Corner:", result)
class Solution(object):
    def uniquePaths(self, m, n):
        memo = {}

        def myPath(m, n):
            if m == 0 and n == 0:
                return 1
            if m == 1 and n == 1:
                return 1

            # Check if result is already memoized
            if (m, n) in memo:
                return memo[(m, n)]

            # Explore right and down paths
            right = myPath(m - 1, n)
            down = myPath(m, n - 1)

            # Memoize the result
            memo[(m, n)] = right + down

            return right + down

        paths = myPath(m, n)
        return paths

# Testing the code
solution = Solution()
m_value = 3
n_value = 3
result = solution.uniquePaths(m_value, n_value)
print("Total unique paths:", result)
