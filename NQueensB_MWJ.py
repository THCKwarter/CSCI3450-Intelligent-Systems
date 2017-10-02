#NQueensB_MWJ.py
#Max puzzle size: 10 -- [0, 4, 9, 5, 8, 1, 3, 6, 2, 7]
#Iterations taken: 9791 iterations.
import random

#Variables
n = int(input("Enter a range for n: "))
nq = list(range(n))
iterations = 0

#Define function
def conflicts(array):
    confCount = 0
    for x in range((len(array)-1)):
        for y in range(x+1, len(array)):
            #Horizontal conflicts
            if array[x] == array[y]:
                confCount += 1
            #Diagonal conflicts
            if (abs(array[x]-array[y]) == abs(x-y)):
                confCount += 1
    return confCount

#Loop until solution is found
while(conflicts(nq) > 0):
    iterations += 1
    random.shuffle(nq)
    print("Randomizing puzzle, attempt: " + str(iterations) + ".")

#Print conflicts and iteration count
print(nq)
print("Problem solved in: " + str(iterations) + " iterations.")

