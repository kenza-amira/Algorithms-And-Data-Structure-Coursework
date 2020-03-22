import math

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)
                
class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        if n == -1: #Intializing where flag is -1
            self.perm = []
            self.n = 0
            for line in open(filename).readlines(  ): #number of node is equivalent to number of lines
                self.n += 1 #Increments number of nodes with every iteration
            with open (filename) as fp: #This creates a list of tuples from the given file
                result = []
                for i in fp.readlines():
                    tmp = i.encode().split() #encode() is used to get set of bytes instead of str for the split, splits at the middle space
                    result.append((int(tmp[0]),int(tmp[1]))) #creates the tuple from the 2 parts of the split
            print(result) #Used for debugging
            self.dists = [[0 for x in range (self.n)] for y in range (self.n)]
            for i in range(int(self.n)):
                for j in range(int(self.n)): #using the list of tuples to fill self.dists
                    self.dists[i][j] = self.dists[j][i] = euclid(result[i],result[j])
            for y in range (int(self.n)):
                self.perm.append(y)
        else: #For case where n is given
            self.perm = []
            self.n = n 
            with open (filename) as fp:
                result = []
                for i in fp.readlines(): #Creates list of tuples (with 3 elements) from the given file
                    tmp = i.encode().split() #same as above
                    result.append((int(tmp[0]),int(tmp[1]),int(tmp[2]))) #creates the tuples from the 3 parts of the split
            print(result)
            self.dists = [[0 for x in range (self.n)] for y in range (self.n)]
            for i in result: #using list of tuples to fill self.dists
                self.dists[i[0]][i[1]] = self.dists[i[1]][i[0]] = i[2]
            print(self.dists)
            for y in range (int(self.n)):
                self.perm.append(y)
    
    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        print(self.perm)
        totalCost = 0
        for x in range (int(self.n)):
            totalCost += self.dists[self.perm[x]][self.perm[(x+1)%self.n]]
        return totalCost
    
    
    # Below are given functions   
    def swapHeuristic(self):
        better = True
        while better:
            better = False
            for i in range(self.n):
                if self.trySwap(i):
                    better = True
                    

    def TwoOptHeuristic(self):
        better = True
        while better:
            better = False
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True
    # End of given functions
    
    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self,i):
        
        normalCost = self.dists[self.perm[i]][self.perm[(i-1)%self.n]] #calculating cost of original permutation 
        normalCost += self.dists[self.perm[(i+2)%self.n]][self.perm[(i+1)%self.n]]
        #calculating cost of swap only at the swap location to avoid expensive algorithm (by calling tourValue each time)
        changedCost = self.dists[self.perm[i]][self.perm[(i+2)%self.n]]
        changedCost += self.dists[self.perm[(i+1)%self.n]][self.perm[(i-1)%self.n]]
                
        if (changedCost < normalCost): #performing swap if cost is less
            #saving current values
            a = self.perm[i]
            b = self.perm[(i+1)%self.n]
            #performing the swap
            self.perm[i] = b
            self.perm[(i+1)%self.n] = a
            return True
        else:
            return False


    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.              
    # 
    def tryReverse(self,i,j):
        normalCost = self.dists[self.perm[i]][self.perm[(i-1)%self.n]] #calculating cost of original permutation 
        normalCost += self.dists[self.perm[j]][self.perm[(j+1)%self.n]]
        #calculating cost of swap only at the swap location to avoid expensive algorithm (by calling tourValue each time)
        changedCost = self.dists[self.perm[j]][self.perm[(i-1)%self.n]]  
        changedCost += self.dists[self.perm[i]][self.perm[(j+1)%self.n]]
        
        if (changedCost<normalCost): 
            self.perm[i:j+1] = reversed(self.perm[i:j+1]) #reversing only the slice we care about
            print(self.perm) #For debugging
            return True;
        else:
            return False;
        
    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
        visited = []
        for i in self.perm:
            visited.append(i)
            print("the loop is" , i)
            next = self.dists[i].copy()
            for x in visited:
                next[x] = 0
            print("next array is", next)
            value = min([x for x in next if x!= 0]) #gets the smallest non zero distance (since self.dists[i][i]) is in the array
            print("smallest value is" , value)
            index = self.dists[i].index(value) #finds node of first occurence of the value within our array

            a = self.perm[(i+1)%self.n] #saving current value at i+1
            self.perm[index] = a #swapping original value of i+1 with index
            self.perm[(i+1)%self.n] = index #changing it to our index(next node to visit)
            print("calculated index is", index)
            print("next index is",self.perm[(i+1)%self.n])
            

                
                
                
                
 
 