#Find, the, maximum, total, from, top, to, bottom, of, the, triangle, below:
#Similar to problem 18
from urllib import urlopen 

list = []
file = urlopen("http://projecteuler.net/project/triangle.txt")
for line in file:
    list.append([int(s) for s in line.split()] )

dynamic_list = [];
temp_row = [];
#Naive: do a greedy search from bottom to top
#Naive approach: do a greedy search from top to bottom

#Solution:
#You want to find the maximum path in the DAG.
#This is the same as finding the minumum path over the negative edge weights
#http://en.wikipedia.org/wiki/Longest_path_problem
#http://en.wikipedia.org/wiki/Bellman-Ford_algorithm
# OR Just use dynamic programming from the bottom up!

dynamic_list.insert(0, list[len(list)-1]);
for i in range(len(list)-2,-1, -1):
    for j in range(0,len(list[i])):
        sum = list[i][j] + max(dynamic_list[0][j],dynamic_list[0][j+1])
        temp_row.append(sum);
    print temp_row
    dynamic_list.insert(0, temp_row);
    temp_row = []

print dynamic_list[0][0]
