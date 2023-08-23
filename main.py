import sys
import numpy as np
import timeit
from collections import deque
import itertools
from abc import ABC, abstractmethod
import heapq
import psutil
import os
import tracemalloc
from BoardGame import Board
from MyAlgo import BFS, DFS, IDDFS, AStar
from Solver import Solver
from Node import Node
from UCS import uniform_cost




def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

flag = 0
print('enter the input using , in between')
zz = list(map(int, input().split(',')))
p = Board(np.array(zz))
alg = input("enter the algorithm: ")
if alg == 'bfs':
    s = BFS(p)
elif alg == 'ids':
    s = IDDFS(p)
elif alg == 'dfs':
    s = DFS(p)
elif alg == 'ast':
    s = AStar(p)
elif alg == 'ucs':

    tracemalloc.start()
    start = timeit.default_timer() 
    result = uniform_cost(zz, [1,2,3,4,5,6,7,8,0])
    stop = timeit.default_timer()
    
    print(result)
    print(len(result), " moves")
    print('time ', stop-start)
    print('ram ' , tracemalloc.get_traced_memory())
    tracemalloc.stop()
    flag = 1
else:
    print("Invalid input, continuing through A*")
    s = AStar(p)

if flag == 0:
    tracemalloc.start()
    start = timeit.default_timer()   
    s.solve()
    stop = timeit.default_timer()


    print('path_to_goal: ' + str(s.path) + '\n')

    print('time: ', format(stop-start, '.8f'))
    print('RAM Usage (MiB): ', psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
    print(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

