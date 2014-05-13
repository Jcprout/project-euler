__author__ = 'jprout'

import datetime


def factorial(p_value):
    """
    Recursive implementation of the Factorial operation
    """
    return p_value if p_value <= 2 else factorial(p_value-1) * p_value


def lattice_paths(p_grid_size):
    """
    Calculate the number of paths through a square lattice
    The formula is (2*grid-size)!/(grid-size!)**2
    See http://copingwithcomputers.com/2013/07/06/lattice-paths for an explanation
    """
    return factorial(2*p_grid_size)/(factorial(p_grid_size)**2)


grid_size = 20

start_time = datetime.datetime.now()
paths = lattice_paths(grid_size)
elapsed = datetime.datetime.now() - start_time

#Expected result is from https://code.google.com/p/projecteuler-solutions/wiki/ProjectEulerSolutions
assert paths == 137846528820, "Incorrect number of paths"

print "Problem 15; Number of lattice paths for a square grid of size: " + str(grid_size) + " is " + str(paths) + \
      " Execution time: " + str((datetime.datetime.now() - start_time).microseconds)
