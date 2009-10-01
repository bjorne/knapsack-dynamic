#!/usr/bin/env python

# Main file

import sys
sys.path.append('lib')
from dynprog import KnapsackSolver

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: knapsack input/knapsack.txt'
        sys.exit(1)
    filename = sys.argv.pop()
    
    # call Exhaust class for a solution (along with its weight and value)
    solution, w, v = KnapsackSolver().solve(filename)
    if solution != []:
        print "solution of weight %d, value %d found:" % (w,v)
        print ", ".join(map(lambda t: str(t), solution))
    else:
        # this should never happen (and hasen't as far as we're concerned)
        print 'no solution found(!).'
