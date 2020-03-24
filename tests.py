import graph
from tabulate import tabulate

#tests on given files, for Euclidian part
g = graph.Graph(-1,"cities50")
g1 = graph.Graph(-1,"cities25")
g2 = graph.Graph(-1,"cities75")

tourValue50 = g.tourValue()
tourValue25 = g1.tourValue()
tourValue75 = g2.tourValue()

g.swapHeuristic()
g1.swapHeuristic()
g2.swapHeuristic()

swapValue50 = g.tourValue()
swapValue25 = g1.tourValue()
swapValue75 = g2.tourValue()

g.TwoOptHeuristic()
g1.TwoOptHeuristic()
g2.TwoOptHeuristic()

twoValue50 = g.tourValue()
twoValue25 = g1.tourValue()
twoValue75 = g2.tourValue()

g = graph.Graph(-1,"cities50")
g1 = graph.Graph(-1,"cities25")
g2 = graph.Graph(-1,"cities75")

g.Greedy()
g1.Greedy()
g2.Greedy()

greedyValue50 = g.tourValue()
greedyValue25 = g1.tourValue()
greedyValue75 = g2.tourValue()

g = graph.Graph(-1,"cities50")
g1 = graph.Graph(-1,"cities25")
g2 = graph.Graph(-1,"cities75")

g.LookAhead()
g1.LookAhead()
g2.LookAhead()

lookValue50 = g.tourValue()
lookValue25 = g1.tourValue()
lookValue75 = g2.tourValue()

headers = ["Graph","Normal Tour", "Swap heuristic", "Two Opt and Swap", "Greedy", "Look Ahead"]

data = [("cities50",tourValue50, swapValue50,twoValue50,greedyValue50,lookValue50),
        ("cities25",tourValue25,swapValue25 ,twoValue25,greedyValue25,lookValue25),
        ("cities75",tourValue75,swapValue75,twoValue75,greedyValue75,lookValue75)]

print("comparing values for our given graphs (euclidean settings)\n".title().center(90))
print(tabulate(data, headers = headers, showindex="always",numalign="right"))

#tests on given files, for Metric part
g3 = graph.Graph(6,"sixnodes")

tour = g3.tourValue()
g3.swapHeuristic()
swap = g3.tourValue()
g3.TwoOptHeuristic
two = g3.tourValue()
g3 = graph.Graph(6,"sixnodes")
g3.Greedy()
greedy = g3.tourValue()
g3 = graph.Graph(6,"sixnodes")
g3.LookAhead()
look = g3.tourValue()

data = [("sixnodes",tour, swap,two,greedy,look)]

print("\n")
print("comparing values for our given graph (metric settings)\n".title().center(90))
print(tabulate(data, headers = headers, showindex="always",numalign="right"))