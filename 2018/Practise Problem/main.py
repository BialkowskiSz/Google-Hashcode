def outputToFile(slices, points):
    with open("output/example.out", "w") as file:
        file.write(str(slices) + '\n')
        for i in points:
            for j in i:
                file.write(str(j) + ' ')

pizza           = []
rows            = 0
columns         = 0
minIngredients  = 0
maxSlice        = 0

tomato      = 'T'
mushroom    = 'M'


with open("input/example.in", "r") as file:
    rows, columns, minIngredients, maxSlice = [ int(i) for i in file.readline().split(' ') ]
    for i in range(rows):
        pizza.append([ i for i in file.readline().replace('\n', '') ])

mushroomCount   = 0
tomatoCount     = 0


for i in range(rows):
    for j in range(columns):
        if pizza[i][j] == 'T':
            tomatoCount += 1
        else:
            mushroomCount += 1

rarerIngredient = mushroom if mushroomCount < tomatoCount else tomato

mushroomCount   = 0
tomatoCount     = 0

rarer = False


i = 0
j = 0
startingX = 0
startingY = 0
totalSlices = 0
ingredient = ''
points = []



while j < columns and j < maxSlice:
    ingredient = pizza[i][j]
    if ingredient == rarerIngredient and rarer:
        totalSlices += 1
        break
    if ingredient == rarerIngredient:
        rarer = True
    j += 1

points.append([startingX, startingY, i, j])


outputToFile(totalSlices, points)






