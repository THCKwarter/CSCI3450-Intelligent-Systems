#NQueensA_MWJ.py
#Max puzzle size: 6
#Iterations taken: 759
import random

#Variables
n = int(input("Enter a range for n: "))
nq = [random.randint(0,n-1) for x in range(n)]
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
    nq = [random.randint(0,n-1) for x in range(n)]
    #print("Number of conflicts: " + str(conflicts(nq)) + ".")
    print("Randomizing puzzle, attempt: " + str(iterations) + ".")

#Print conflicts and iteration count
print("Problem solved in: " + str(iterations) + " iterations.")
