def knapSack(C, wt, val, n):
	if n == 0 or C == 0:
		return 0;

	if wt[n-1] > C:
		return knapSack(C, wt, val, n-1)
	else:
		return max(val[n-1] + knapSack(C-wt[n-1], wt, val, n-1), knapSack(C, wt, val, n-1))

# The above solution solves same problem again and again (OVERLAPPING SUBPROBLEM). Therefor in below solution
# we will store the value of already solved problem in a matrix

def knapsack(C, wt, val, n):
	k = [[0 for x in range(C+1)] for x in range(n+1)]
	# i is for number of elements and w is for weight
	for i in range(n+1):
		for w in range(C+1):
			if i == 0 or w == 0:
				k[i][w] = 0		# base condition when number of elements or capacity is zero
			elif wt[i-1] <= w:	# when weight is less than capacity, either include n-1 or skip n-1
				k[i][w] = max(val[i-1] + k[i-1][w-wt[i-1]], k[i-1][w])
			else:
				k[i][w] = k[i-1][w]	# else no option, had to skip n-1 element as it's weight is greater than capacity

	return k[n][W]

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val, n)) 