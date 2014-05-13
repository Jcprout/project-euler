__author__ = 'jprout'

from sys import argv
from os.path import exists
import datetime
import time
import sys


def print_list_of_lists(p_lines):
    """
    Print p_lines, which is a list of lists of numbers
    Used to check that the input file was read correctly
    """
    for line in p_lines:
        for number in line:
            print str(number),
        print


def read_numbers_file(p_in_file_name):
    """
    Read the numbers in the file passed as p_in_file_name
    The procedure requires that the first line in the file contain one number
    and that all subsequent lines contain one more number than that on the previous line
    Numbers are assumed to be separated by a single space character
    """
    line_number = 0
    lines = []
    in_file = open(p_in_file_name)
    while True:
        line = in_file.readline()
        if not line: break
        line_number += 1

        #split the line into a list of number strings and then convert into a list of int
        #map calls the int fn on all elements in the parameter list
        numbers = map(int, line.split(' '))
        if line_number == 1 and len(numbers) != 1:
            print "File must start with a line containing a single number"
            sys.exit(1)

        lines.append(numbers)

        #confirm that each line read contains one more number than the previous line
        if line_number != len(numbers):
            print "Line: %s contains %s numbers" % (line_number, len(numbers))
            sys.exit(1)
    return lines


def max_sum_of_triangle_line(p_triangle_lines, p_parent_line_index, p_child_line):
    """
    Recursive procedure to calculate the sum of a two high triangle, with one head and two children
    Call this procedure recursively on every line in the triangle, starting with the second line from the bottom
    (not the bottom line, because we're looking at the heads of triangles which are 2 high)
    new_child_line holds the results of the calculations for this line and is passed to the next recursion
    This procedure will only work with a triangle with one number at its head and one additional on each subsequent line
    This is enforced by the read_numbers_file function
    Input parameters:
        p_triangle_lines - an List of Lists of numbers - the input triangle
        p_parent_line_index - the index to the line in p_triangle_lines, which is the heads of the 2-high triangles
                              which I'm processing in this recursion
        p_child_line - sums from the previous recursion
    Result
        The maximum path sum for p_triangle_lines
    """
    new_child_line = []
    parent_index = 0
    for number in p_triangle_lines[p_parent_line_index]:
        new_child_line.append(number + max(p_child_line[parent_index], p_child_line[parent_index + 1]))
        parent_index += 1

    return new_child_line[0] if p_parent_line_index == 0 \
        else max_sum_of_triangle_line(p_triangle_lines, p_parent_line_index - 1,new_child_line)


def brute_force_maximum_path_sum(p_triangle_lines):
    """
    Brute force approach to finding the maximum paths sum
    Walk down the triangle, traversing every path and keep track of the sum
    Data structure which tracks the sum is a list;
        First List element is the sum on this route
        Second list element is the index of the last element added (i.e. from the line being processed)
    When I'm processing the next line, value added to the sum from the previous line
    will be index and index + 1, which are two more paths
    """
    previous_sums_line = []
    for triangle_line in p_triangle_lines:
        #If this is the top of the triangle, there's nothing to add
        #all I have to do is initialize previous_sums_line with sum = the head of the triangle, index = 0
        if len(triangle_line) == 1:
            previous_sums_line.append([triangle_line[0],0])
            continue
        sums_line = []
        for sum in previous_sums_line:
            #sum[0] is the sum, sum[1] is the index
            first_sum = sum[0] + triangle_line[sum[1]]
            second_sum = sum[0] + triangle_line[sum[1]+1]
            sums_line.append([first_sum,sum[1]])
            sums_line.append([second_sum,sum[1]+1])
        previous_sums_line = sums_line
    return reduce(max_sum, sums_line)[0]


def max_sum(sum_object1, sum_object2):
    """
    Helper function to return the max value in two of the value, index Lists I use in the brute force method
    Input parameters are the two lists to compare
    """
    return sum_object1 if sum_object1[0] > sum_object2[0] else sum_object2


#Testing the solution
#Expected results are from https://code.google.com/p/projecteuler-solutions/wiki/ProjectEulerSolutions
from_file = "euler_18_triangle.txt"
triangle_lines = read_numbers_file(from_file)
maximum_paths_total = max_sum_of_triangle_line(triangle_lines, len(triangle_lines) - 2, triangle_lines[-1])
maximum_paths_total_brute = brute_force_maximum_path_sum(triangle_lines)
assert maximum_paths_total == maximum_paths_total_brute, \
    "Clever and brute force results don't match for Euler 18 triangle"
assert maximum_paths_total == 1074, "Incorrect result for Euler 18 triangle"

from_file = "euler_67_triangle.txt"
triangle_lines = read_numbers_file(from_file)
maximum_paths_total = max_sum_of_triangle_line(triangle_lines, len(triangle_lines) - 2, triangle_lines[-1])
assert maximum_paths_total == 7273, "Incorrect result for Euler 67 triangle"

#Small test triangle
from_file = "test_triangle.txt"
triangle_lines = read_numbers_file(from_file)
maximum_paths_total = max_sum_of_triangle_line(triangle_lines, len(triangle_lines) - 2, triangle_lines[-1])
maximum_paths_total_brute = brute_force_maximum_path_sum(triangle_lines)
assert maximum_paths_total == maximum_paths_total_brute, "Clever and brute force results don't match for test triangle"
assert maximum_paths_total == 23, "Incorrect result for test triangle"

# This is the solution and execution time for Problem 18
start_time = datetime.datetime.now()
from_file = "euler_18_triangle.txt"
triangle_lines = read_numbers_file(from_file)
maximum_paths_total = max_sum_of_triangle_line(triangle_lines, len(triangle_lines) - 2, triangle_lines[-1])
elapsed = datetime.datetime.now() - start_time

print "Problem 18; maximum path total is: " + str(maximum_paths_total) + \
      ", elapsed time is: " + str((datetime.datetime.now() - start_time).microseconds) + " microseconds"

