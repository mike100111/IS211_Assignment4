import time
import timeit
import random

def insertion_sort(a_list):
    
    start_time = timeit.default_timer()
    for index in range(1, len(a_list)):
        
        current_value = a_list[index]
        position = index
        
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            
        a_list[position] = current_value
        
    return timeit.default_timer() - start_time    

def shell_sort(a_list):
    start_time = timeit.default_timer()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)        
        
        sublist_count = sublist_count // 2

    return timeit.default_timer() - start_time

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

def  python_sort(a_list):
    start_time = timeit.default_timer()
    a_list.sort()
    return timeit.default_timer() - start_time

def generate_list(size):

    return random.sample(range(1, 50000), size)       

def main():

    sizes = [500, 1000, 10000]        
    insertion_timelapsed = 0
    shell_timelapsed = 0
    python_timelapsed = 0    

    for size in sizes:        
        for x in range(0, 99):
            
            insertion_timelapsed += insertion_sort(generate_list(size))
            shell_timelapsed += shell_sort(generate_list(size))
            python_timelapsed += python_sort(generate_list(size))
            
        print 'For ' + str(size) + ', Insertion Sort took%10.7f to run on average' % (insertion_timelapsed/100)     
        print 'For ' + str(size) + ', Shell Sort took%10.7f to run on average' % (shell_timelapsed/100)
        print 'For ' + str(size) + ', Python Sort took%10.7f to run on average' % (python_timelapsed/100)
    
main()
    
