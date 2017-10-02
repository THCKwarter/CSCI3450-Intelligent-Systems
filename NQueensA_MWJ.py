#NQueensA_MWJ.py
#Define a function to count number of conflicts()
#While number of conflicts in NQ > 0
    #Randomize (or improve) NQ
#Print NQ
#Print number of iterations

#abs value of x-y & y-x to check for diagonal conflict
import random

#Ask user for n value
n = 8
nq = [random.randint(0,n-1) for x in range(n)]
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
print(nq)                
print("Number of conflicts: [" + str(conflicts(nq)) + "]")
                
