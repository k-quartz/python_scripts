import re


def printMaze():
    for r in range(0,rows):
        for c in range(0,cols):
            print(maze[r][c],end=" ")

        print("")

   
def getway1(rw, cl):
    if re.search(r'\d',maze[rw][cl]):
        portal=int(maze[rw][cl])
        
        if cl+portal+1<cols:
            getway1(rw,cl+portal+1)

    if maze[rw][cl] == "X":
        return False
    elif maze[rw][cl] == ".":
        return False


    if rw==rows-1 and cl==cols-1:
        return
    else:
        maze[rw][cl] = "."
    

    
    if rw < rows-1 and getway1(rw+1, cl):
        return True
    elif cl > 0 and getway1(rw, cl-1):
        return True
    elif cl < cols-1 and getway1(rw, cl+1):
        return True
    
    return False
    
rows=4#int(input("Enter the number of rows : "))
cols=5#int(input("Enter the number of columns : "))
maze=[['O','X','X','X','2'],['O','1','X','1','O'],['X','X','X','X','1'],['2','X','X','O','O']]


# rows=int(input("Enter the number of rows : "))
# cols=int(input("Enter the number of columns : "))
# maze=[]

# for r in range(0,rows):
#     row=[]
#     for c in range(0,cols):
#         row.append(input("Enter the value : "))
    
#     maze.append(row)

print()
print("=================")
print("Input maze :")
printMaze()
getway1(0, 0)
print("=================")
print("Output Maze  : ")
printMaze()

