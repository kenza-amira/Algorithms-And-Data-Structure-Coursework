import math
import numpy as np
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
        self.perm = []
        if n == -1: #Intializing where flag is -1
            self.n = 0
            for line in open(filename).readlines(  ): #number of node is equivalent to number of lines
                self.n += 1 #Increments number of nodes with every iteration
            with open (filename) as fp: #This creates a list of tuples from the given file
                result = []
                for i in fp.readlines():
                    tmp = i.encode().split() #encode() is used to get set of bytes for the split, splits at the middle space
                    result.append((int(tmp[0]),int(tmp[1]))) #creates the tuple from the 2 parts of the split
            print(result) #Used for debugging
            self.dists = [[0 for x in range (int(self.n))] for y in range (int(self.n))]
            for i in range(int(self.n)):
                for j in range(int(self.n)): #using the list of tuples to fill self.dists
                    self.dists[i][j] = self.dists[j][i] = euclid(result[i],result[j])
            for y in range (n):
                self.perm.append(y)
        else: #For case where n is given
            self.n = n 
            with open (filename) as fp:
                result = []
                for i in fp.readlines(): #Creates list of tuples (with 3 elements) from the given file
                    tmp = i.encode().split() #same as above
                    result.append((int(tmp[0]),int(tmp[1]),int(tmp[2]))) #creates the tuples from the 3 parts of the split
            print(result)
            self.dists = [[0 for x in range (self.n)] for y in range (self.n)]
            for i in result: #using list of tuples to fill self.dists
                self.dists[i[0]][i[1]] = i[2]
            print(self.dists)
            for y in range (n):
                self.perm.append(y)
    
    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        print(self.perm)
        totalCost = 0
        for x in range (1,int(self.n)):
            totalCost = totalCost + self.dists[self.perm[x]][self.perm[x-1]]
        totalCost = totalCost + self.dists[self.perm((self.n)-1)][0]
        return totalCost