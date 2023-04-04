import numpy as np
import csv

with open("maze_files/smallMaze.txt") as f:
    content = f.read()

content = content.replace("P", " ")
content = content.replace(".", " ")
content = content.split("\n")

i = 0
arr = []

for x in content:
    arr.append(x)

arrx = len(arr)
arry = 0

while i < len(arr):
    arr2 = []
    for x in arr[i]:
        arr2.append(x)
        arry += 1
    arr[i] = arr2
    i += 1

def hasWall(arr, x, y, pos):
    arrx = len(arr)
    arry = len(arr[0])

    if pos == "e":
        if y+1 >= arry:
            return 0
        else:
            if arr[x][y+1] == "%":
                return 1
            else:
                return 0
            
    if pos == "w":
        if y-1 < 0:
            return 0
        else:
            if arr[x][y-1] == "%":
                return 1
            else:
                return 0
    
    if pos == "n":
        if x-1 < 0:
            return 0
        else:
            if arr[x-1][y] == "%":
                return 1
            else:
                return 0
            
    if pos == "s":
        if x+1 >= arrx:
            return 0
        else:
            if arr[x+1][y] == "%":
                return 1
            else:
                return 0

result = []

result.append(["  cell  ", "E", "W", "N", "S"])

j = 0
while j < len(arr[0]):
    i = 0
    while i < len(arr):
        arr3 = []
        arr3.append("({x}, {y})".format(x=i+1, y=j+1))
        arr3.append(hasWall(arr, i, j, "e"))
        arr3.append(hasWall(arr, i, j, "w"))
        arr3.append(hasWall(arr, i, j, "n"))
        arr3.append(hasWall(arr, i, j, "s"))
        result.append(arr3)
        i += 1
    j +=1

with open('maze_files/smallMaze.csv','w', newline="") as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)