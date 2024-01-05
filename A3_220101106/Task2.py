import random

# Input the size of the square matrix
n = int(input("Enter the Number of rows/columns for the square matrix: "))
visited = {}  # Initialize a dictionary to track visited cells
maze = []     # Initialize an empty maze

# Taking the matrix as input
print("Give the maze as input")
matrix = []
for i in range(n):
    # taking input for the row from the user
    single_row = list(map(int, input().split()))
    # appending the 'single_row' to the 'matrix'
    matrix.append(single_row)

# Reverse the matrix to create the maze
maze = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        maze[i][j] = matrix[n-i-1][j]

# Display the maze
print("The Provided Maze is: ")
for i in range(n):
    for j in range(n):
        print(maze[n - i - 1][j], end=" ")
    print()

# Input source and destination coordinates
sourcesy = int(input("Enter source's ROW coordinate: "))
sourcesx = int(input("Enter source's COLUMN coordinate: "))

# Validate that source coordinates are within bounds
if sourcesx < 1 or sourcesx > n or sourcesy < 1 or sourcesy > n:
    print("Error: Source coordinates are out of bounds.")
else:
    sourcesy = sourcesy - 1
    sourcesx = sourcesx - 1
    ssy = sourcesy
    ssx = sourcesx

destinationx = int(input("Enter destination's ROW coordinate : "))
destinationy = int(input("Enter destination's COLUMN coordinate : "))

# Validate that destination coordinates are within bounds
if destinationx < 1 or destinationx > n or destinationy < 1 or destinationy > n:
    print("Error: Destination coordinates are out of bounds.")
else:
    destinationx = destinationx - 1
    destinationy = destinationy - 1

# Initialize the visited dictionary to track distances
visited = {str([sourcesy, sourcesx]): 0}
curr = [[sourcesy, sourcesx]]

paths = []
ans = []

step = 0

# Explore the maze to find the path
while (len(curr) != 0):
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):

            if ((str([max(sourcesy+i, 0), max(sourcesx+j, 0)]) not in visited) and (sourcesy+i < n and sourcesx+j < n)):
                if (maze[max(sourcesy+i, 0)][max(sourcesx+j, 0)] != 1):
                    visited[str([max(sourcesy+i, 0), max(sourcesx+j, 0)])
                            ] = visited[str([sourcesy, sourcesx])]+1
                    curr.append([max(sourcesy+i, 0), max(sourcesx+j, 0)])
            if ((str([min(sourcesy+i, n-1), min(sourcesx+j, n-1)]) not in visited) and (sourcesy+i >= 0 and sourcesx+j >= 0)):
                if (maze[min(sourcesy+i, n-1)][min(sourcesx+j, n-1)] != 1):

                    visited[str([min(sourcesy+i, n-1), min(sourcesx+j, n-1)])
                            ] = visited[str([sourcesy, sourcesx])]+1
                    curr.append([min(sourcesy+i, n-1), min(sourcesx+j, n-1)])
    curr.pop(0)
    if (len(curr)):

        sourcesy = curr[0][0]
        sourcesx = curr[0][1]
paths.append([ssy, ssx])

# Function to make the path


def makepath(ssy, ssx, visited):
    global ans
    global paths
    global distance
    global destinationx
    global destinationy
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if (str([ssy + i, ssx + j]) in visited):
                if (visited[str([ssy + i, ssx + j])] == visited[str([ssy, ssx])] + 1):
                    paths.append([ssy + i, ssx + j])
                    if len(paths) == distance + 1:
                        if (paths[-1] == [destinationx, destinationy]):
                            for element in paths:
                                print(
                                    "{", element[0] + 1, ",", element[1] + 1, "}", end=" ")
                            print()
                    makepath(ssy + i, ssx + j, visited)
                    paths.pop()
    return ans


# Check if the destination is unreachable or find the path
if (maze[ssy][ssx] == 1 or maze[destinationx][destinationy] == 1 or (str([destinationx, destinationy]) not in visited)):
    print("The destination is unreachable from source")
else:
    print("Shortest path length is")
    print(visited[str([destinationx, destinationy])])
    distance = visited[str([destinationx, destinationy])]
    print("The possible paths are")
    makepath(ssy, ssx, visited)
