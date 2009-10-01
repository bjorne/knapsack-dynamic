#!/usr/bin/env python

import sys, re

# the Conf class reads input files via read_file
# and creates a tuple for each item
class Conf(object):

  def __init__(self):
    self.objects = []
    self.capacity = 0

  def read_file(self, filename):
    f = open(filename, 'r')

    # loop through all lines
    for line in f.readlines():
      result = re.match("^capacity=(\d+)$", line)
      if result:
        # the line is the capacity, store it
        self.capacity = int(result.group(1))
      else:
        # the line is an object e.g. (A,B)
        result = re.match("^\((\d+)\s*,\s*(\d+)\)$", line)
        if result:
          item = (int(result.group(1)), int(result.group(2)))
          self.objects.append(item)
        else:
          raise Exception("Config error: invalid item")

    return (self.objects, self.capacity)

# Main class for the program
class KnapsackSolver(object):

  def __init__(self):
    pass

  # Call this method to solve the problem given in filename
  def solve(self, filename):
    conf = Conf().read_file(filename)
    items, capacity = conf
    M, optimal_value = self.generate_optimal_solutions(items, len(items), capacity)
    # print optimal_value
    # 
    # for i in range(0,len(items)):
    #   print items[i]
    # for i in range(0,len(M)):
    #   print M[i]
    
    optimal_set = []
    # raise the recursion limit so that we can handle a large number of items
    sys.setrecursionlimit(len(items)+10)
    optimal_weight = self.get_optimal_set(items, len(items), M, len(items)-1, capacity, optimal_set, 0)
    
    return optimal_set, optimal_weight, optimal_value

  def generate_optimal_solutions(self, items, n, capacity):
    M = [[]]
    for w in range(0,capacity+1):
      M[0].append(0) # = 0
    
    for i in range(0,n):
      M.append([])
      for w in range(0,capacity+1):
        if (items[i][0] > w):
          M[i+1].append(M[i-1+1][w])
        else:
          M[i+1].append( max(M[i-1+1][w], items[i][1] + M[i-1+1][w - items[i][0]]) )
          
    return M, M[n][capacity]
    
  def get_optimal_set(self, items, n, M, j, w, optimal_set, optimal_weight):
    if (j < 0):
      pass
    elif (w >= items[j][0] and items[j][1] + M[j-1+1][w - items[j][0]] > M[j-1+1][w]):
      optimal_set.append(items[j])
      optimal_weight += items[j][0]
      optimal_weight = self.get_optimal_set(items, n, M, j-1, w - items[j][0], optimal_set, optimal_weight)
    else:
      optimal_weight = self.get_optimal_set(items, n, M, j-1, w, optimal_set, optimal_weight)
      
    return optimal_weight
      