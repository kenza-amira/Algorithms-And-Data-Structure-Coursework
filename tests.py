import graph
from tabulate import tabulate
import random as rd

#tests on files, for Euclidian part
g = graph.Graph(-1,"cities50")
g1 = graph.Graph(-1,"cities25")
g2 = graph.Graph(-1,"cities75")
g5 = graph.Graph(-1,"K7euclid")

tourValue50 = g.tourValue()
tourValue25 = g1.tourValue()
tourValue75 = g2.tourValue()
tourValue = g5.tourValue()

g.swapHeuristic()
g1.swapHeuristic()
g2.swapHeuristic()
g5.swapHeuristic()

swapValue50 = g.tourValue()
swapValue25 = g1.tourValue()
swapValue75 = g2.tourValue()
swapValue = g5.tourValue()

g.TwoOptHeuristic()
g1.TwoOptHeuristic()
g2.TwoOptHeuristic()
g5.TwoOptHeuristic()

twoValue50 = g.tourValue()
twoValue25 = g1.tourValue()
twoValue75 = g2.tourValue()
twoValue = g5.tourValue()

g = graph.Graph(-1,"cities50")
g1 = graph.Graph(-1,"cities25")
g2 = graph.Graph(-1,"cities75")
g5 = graph.Graph(-1,"K7euclid")

g.Greedy()
g1.Greedy()
g2.Greedy()
g5.Greedy()

greedyValue50 = g.tourValue()
greedyValue25 = g1.tourValue()
greedyValue75 = g2.tourValue()
greedyValue = g5.tourValue()

g = graph.Graph(-1,"cities50")
g1 = graph.Graph(-1,"cities25")
g2 = graph.Graph(-1,"cities75")
g5 = graph.Graph(-1,"K7euclid")

g.LookAhead()
g1.LookAhead()
g2.LookAhead()
g5.LookAhead()

lookValue50 = g.tourValue()
lookValue25 = g1.tourValue()
lookValue75 = g2.tourValue()
lookValue = g5.tourValue()

rangeX = (0,250)
rangeY = (0,250)
qty = 100 
i = 0
points = []
while i < qty:
        x = rd.randrange(*rangeX)
        y = rd.randrange(*rangeY)
        points.append((x,y))
        i += 1      
f = open("myrandom.txt", "w")
for point in points:
        f.write(str(point[0]) + " " + str(point[1]) + "\n")
f.close()

grd = graph.Graph(-1,"myrandom.txt")
rdTour = grd.tourValue()
grd.swapHeuristic()
rdSwap = grd.tourValue()
grd.TwoOptHeuristic()
rd2opt = grd.tourValue()
grd = graph.Graph(-1,"myrandom.txt")
grd.Greedy()
rdGreedy = grd.tourValue()
grd = graph.Graph(-1,"myrandom.txt")
grd.LookAhead()
rdLook = grd.tourValue()

headers = ["Graph","Normal Tour", "Swap heuristic", "Two Opt and Swap", "Greedy", "Look Ahead"]

data = [("cities50",tourValue50, swapValue50,twoValue50,greedyValue50,lookValue50),
        ("cities25",tourValue25,swapValue25 ,twoValue25,greedyValue25,lookValue25),
        ("cities75",tourValue75,swapValue75,twoValue75,greedyValue75,lookValue75),
        ("K7euclid",tourValue,swapValue,twoValue,greedyValue,lookValue),
        ("Random", rdTour,rdSwap,rd2opt,rdGreedy,rdLook)]

print("comparing values for our graphs (euclidean settings)\n".title().center(90))
print(tabulate(data, headers = headers, showindex="always",numalign="right"))

#tests on files, for Metric part
g3 = graph.Graph(6,"sixnodes")
g4 = graph.Graph(7,"K7metric")
g6 = graph.Graph(4,"greedy_confuse")

tour = g3.tourValue()
tour2 = g4.tourValue()
tour3 = g6.tourValue()
g3.swapHeuristic()
g4.swapHeuristic()
g6.swapHeuristic()
swap = g3.tourValue()
swap2 = g4.tourValue()
swap3 = g6.tourValue()
g3.TwoOptHeuristic()
g4.TwoOptHeuristic()
g6.TwoOptHeuristic()
two = g3.tourValue()
two2 = g4.tourValue()
two3 = g6.tourValue()
g3 = graph.Graph(6,"sixnodes")
g4 = graph.Graph(7,"K7metric")
g6 = graph.Graph(4,"greedy_confuse")
g3.Greedy()
g4.Greedy()
g6.Greedy()
greedy = g3.tourValue()
greedy2 = g4.tourValue()
greedy3 = g6.tourValue()
g3 = graph.Graph(6,"sixnodes")
g4 = graph.Graph(7,"K7metric")
g6 = graph.Graph(4,"greedy_confuse")
g3.LookAhead()
g4.LookAhead()
g6.LookAhead()
look = g3.tourValue()
look2 = g4.tourValue()
look3 = g6.tourValue()

data = [("sixnodes",tour, swap,two,greedy,look),
        ("K7metric",tour2, swap2,two2,greedy2,look2),
        ("greedy_confuse non-metric",tour3, swap3,two3,greedy3,look3)]

print("\n")
print("comparing values for our other graphs\n".title().center(90))
print(tabulate(data, headers = headers, showindex="always",numalign="right"))

