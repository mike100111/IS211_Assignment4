import time
import timeit
import random

def sequential_search(a_list, item):
    pos = 0
    found = False
    start_time = timeit.default_timer()
    
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    elapsed = timeit.default_timer() - start_time   
    
    return (found, elapsed)

def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    start_time = timeit.default_timer()
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    elapsed = timeit.default_timer() - start_time   
    return found, elapsed

def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    start_time = timeit.default_timer()
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
                
    elapsed = timeit.default_timer() - start_time   
    return found, elapsed

def binary_search_recursive(a_list, item, timeelapsed):
    start_time = timeit.default_timer()
    if len(a_list) == 0:
        elapsed = timeit.default_timer() - start_time   
        return False, elapsed + timeelapsed
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        elapsed = timeit.default_timer() - start_time   
        return True, elapsed + timeelapsed
    else:
        if item < a_list[midpoint]:
            elapsed = timeit.default_timer() - start_time   
            return binary_search_recursive(a_list[:midpoint], item, elapsed)
        else:
            elapsed = timeit.default_timer() - start_time   
            return binary_search_recursive(a_list[midpoint + 1:], item, elapsed)

def generate_list(size):

    return random.sample(range(1, 50000), size)       

def main():

    sizes = [500, 1000, 10000]        
    sequential_timelapsed = 0
    orderedsequential_timelapsed = 0
    binarySearchIterative_timelapsed = 0
    binarySearchRecursive_timelapsed = 0
    
    # sequential search
    for size in sizes:        
        for x in range(0, 99):
            
            sequential_timelapsed += sequential_search(generate_list(size), -1)[1]
            orderedsequential_timelapsed += ordered_sequential_search(sorted(generate_list(size)), -1)[1]
            binarySearchIterative_timelapsed += binary_search_iterative(sorted(generate_list(size)), -1)[1]
            binarySearchRecursive_timelapsed += binary_search_recursive(sorted(generate_list(size)), -1, 0)[1]
            
        print 'For ' + str(size) + ', Sequential Search took%10.7f to run on average' % (sequential_timelapsed/100)     
        print 'For ' + str(size) + ', Ordered Sequential Search took%10.7f to run on average' % (orderedsequential_timelapsed/100)
        print 'For ' + str(size) + ', Binary Search Iterative took%10.7f to run on average' % (binarySearchIterative_timelapsed/100)
        print 'For ' + str(size) + ', Binary Search Recursive took%10.7f to run on average' % (binarySearchRecursive_timelapsed/100)
    
main()
