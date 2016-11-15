###############################################################################
####
####       George Whiteside
####       Assignment #7

def floydWarshall(d,pi):
	n = len(d)
	for k in range(0,n):
		for i in range(0,n):
			for j in range(0,n):
				if d[i][j] > d[i][k] + d[k][j]:
					d[i][j] = d[i][k] + d[k][j]
					pi[i][j] = pi[k][j]
	return [d, pi]

def printAPSP(pi,i,j):
	if i == j:
		print i
	elif pi[i-1][j-1] == INF:
		print "No path from %i to %i exists" % (i,j)
	else:
		printAPSP(pi,i,pi[i-1][j-1])
		print j


###############################################################################
####       Test Definitions

INF = float("inf")

dTest = [[0,3,8,INF,-4],
[INF,0,INF,1,7],
[INF,4,0,INF,INF],
[2,INF,-5,0,INF],
[INF,INF,INF,6,0]]

piTest = [[INF,1,1,INF,1],
[INF,INF,INF,2,2],
[INF,3,INF,INF,INF],
[4,INF,4,INF,INF],
[INF,INF,INF,5,INF]]


###############################################################################
####       Print Results

print "Inputs are:"
print "D:", dTest
print "Pi:", piTest

outputTest = floydWarshall(dTest,piTest)

print "\nOutputs are:"
print "D:", outputTest[0]
print "Pi:", outputTest[1]

print "\nTests of printAPSP:\n"
print "Shortest path form 2 to 1:"
printAPSP(outputTest[1],2,1)
print "Shortest path form 3 to 5:" 
printAPSP(outputTest[1],3,5)
print "Shortest path form 1 to 5:"
printAPSP(outputTest[1],1,5)
print "Shortest path form 2 to 2:"
printAPSP(outputTest[1],2,2)


print "\nTest if there is no path:"
piTest2 = [[INF,INF],[INF,INF]]
printAPSP(piTest2,0,1)