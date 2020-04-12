#!/usr/bin/python

F = []
N = int(input("fibonacci number? "))
for i in range(0,N):
	if (i < 2):
		F.append(1)
	else:
		F.append(F[i-1] + F[i-2])

for j in range(0,N-1):
	print(F[j],end=",")
print(F[N-1])
print("F%d = %d" % (N, F[N-1]))


