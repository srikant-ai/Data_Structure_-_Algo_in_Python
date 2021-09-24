# -*- coding: utf-8 -*-
"""
Bubble Sort Program implementation in Python
"""

def bubble_sort(elements):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j+1]
                elements[j+1]=elements[j]
                elements[j]=temp
                swapped = True
        if not swapped:
            break
            
if __name__ == '__main__':
    
    # elements =[1,2,4]
    elements = [5,9,2,1,67,34,88,34]
    bubble_sort(elements)
    print(elements)
    
    