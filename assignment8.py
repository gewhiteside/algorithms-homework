###############################################################################
####
####       George Whiteside
####       Assignment #8

####       Part I - Matrix-Chain-Multiplication and Print-Optimal-Parens

def matrixChainOrder(p):
	n = len(p) - 1
	## initialize m
	m = []
	for row in range(0,n):
		m.append([])
	for row in m:
		for column in range(0,n):
			row.append(0)
	## initialize s
	s = []
	for row in range(0,n):
		s.append([])
	for row in s:
		for column in range(0,n):
			row.append(0)
	## begin function
	for i in range(0,n):
		m[i][i] = 0
	for l in range(1,n):
		for i in range(0,n-l):
			j = i+l
			m[i][j] = float("inf")
			for k in range(i,j):
				q = m[i][k] + m[k+1][j] + (p[i] * p[k+1] * p[j+1])
				if q < m[i][j]:
					m[i][j] = q
					s[i][j] = k
	toReturn = [m,s]
	return toReturn

def printOptimalParens(s,i,j):
	if i==j:
		print "A%i" % i,
	else:
		print "(",
		printOptimalParens(s,i,s[i][j]),
		printOptimalParens(s,s[i][j]+1,j),
		print ")",

###############################################################################
####       Test Definitions

pTest = [30,35,15,5,10,20,25]

###############################################################################
####       Print Results

print "Test of Matrix-Chain-Order:"
print matrixChainOrder(pTest)[0]
print matrixChainOrder(pTest)[1]

print "\nTest of Print-Optimal-Parens:"
print "Should be ((A0(A1A2))((A3A4)A5)):"
print "Is:",
printOptimalParens(matrixChainOrder(pTest)[1],0,len(pTest)-2)


###############################################################################
####       Part II - Longest-Common-Subsequence

def LCS(x,y):
	m = len(x)
	n = len(y)
	## intialize b
	b = []
	for row in range(0,m+1):
		b.append([])
	for row in b:
		for column in range(0,n+1):
			row.append(None)
	## intialize c
	c = []
	for row in range(0,m+1):
		c.append([])
	for row in c:
		for column in range(0,n+1):
			row.append(None)
	## begin function
	for i in range(1,m+1):
		c[i][0]=0
	for j in range(0,n+1):
		c[0][j]=0
	for i in range(1,m+1):
		for j in range(1,n+1):
			if x[i-1]==y[j-1]:
				c[i][j]=c[i-1][j-1]+1
				b[i][j]="up-left"
			elif c[i-1][j]>=c[i][j-1]:
				c[i][j]=c[i-1][j]
				b[i][j]="up"
			else:
				c[i][j]=c[i][j-1]
				b[i][j]="left"
	return [c,b]

def printLCS(b,X,i,j):
	if i==0 or j==0:
		return
	if b[i][j]=="up-left":
		printLCS(b,X,i-1,j-1)
		print X[i-1],
	elif b[i][j]=="up":
		printLCS(b,X,i-1,j)
	else:
		printLCS(b,X,i,j-1)

###############################################################################
####       Test Definitions

XTest1 = "abcbdab"
YTest1 = "bdcaba"

XTest2 = "abba"
YTest2 = "bab"

XTest3 = "mzjawxu"
YTest3 = "xmjyauz"

###############################################################################
####       Print Results

TestOutput1 = LCS(XTest1,YTest1)
TestOutput2 = LCS(XTest2,YTest2)
TestOutput3 = LCS(XTest3,YTest3)

print "\n\nTests of LCS and printLCS:"
print "\nTest 1:\nInputs:", XTest1, YTest1
print "Should be BCBA or BDAB:"
print "Is:"
printLCS(TestOutput1[1],XTest1,len(XTest1),len(YTest1))
print "\n\nTest 2:\nInputs:", XTest2, YTest2
print "Should be AB or BA:"
print "Is:"
printLCS(TestOutput2[1],XTest2,len(XTest2),len(YTest2))
print "\n\nTest 1:\nInputs:", XTest1, YTest1
print "Should be MJAU:"
print "Is:"
printLCS(TestOutput3[1],XTest3,len(XTest3),len(YTest3))