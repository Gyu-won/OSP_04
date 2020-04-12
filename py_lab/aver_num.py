#!/usr/bin/python

sum = 0
N = int(input("input number "))
for i in range(0, N):
	value = int(input())
	sum += value
aver = sum/N
print("average: ", aver)
