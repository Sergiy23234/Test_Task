import random
#input matrix
M = int(input("Enter the count of rows"))
N = int(input("Enter the count of colums"))
matrix = [[random.randint(0, 1) for y in range(M)] for x in range(N)]

expamplematrix1 = [[0, 1, 0],
                   [0, 0, 0],
                   [0, 1, 1]]

expamplematrix2 = [[0, 0, 0, 1],
                   [0, 0, 1, 0],
                   [0, 1, 0, 0]]

expamplematrix3 = [[0, 0, 0, 1],
                   [0, 0, 1, 1],
                   [0, 1, 0, 1]]
#matrix = expamplematrix3
for i in matrix:
    print(i)
islands = []

class island:
    def __init__(self):
        self.coords = []

    def addislandpart(self, x, y):
        self.coords.append([x, y])

    def comparecoordinats(self, x, y):
        check = False
        for i in self.coords:
            #print(i)
            if i[0] == x:
                if i[1] == y+1 or i[1] == y-1:
                    check = True
                    break
            elif i[1] == y:
                if i[0] == x+1 or i[0] == x-1:
                    check = True
                    break
        return check

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if matrix[i][j] == 1:
            a = island()
            a.addislandpart(i, j)
            islands.append(a)

def findisland(ind):
    obj = islands[ind]
    for n in islands:
        if n != obj:
            if obj.comparecoordinats(n.coords[0][0], n.coords[0][1]):
                return islands.index(n)
    return False

print(islands)

end = False
ind = 0
while end == False:
    l = len(islands)
    obj = findisland(ind)
    if obj != False:
        for i in islands[obj].coords:
            islands[ind].coords.append(i)
        islands.pop(obj)
        ind = 0
    elif ind == len(islands)-1:
        end = True
    elif obj == False:
        ind += 1
print("К-сть островів: ")
print(len(islands))



