# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:35:03 2021

@author: Srikanth Sahoo
"""

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j=i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1]=elements[j]
            j=j-1
        elements[j+1]=anchor

if __name__ == '__main__':
    elements = [78,3,4,55,2,11,0]
    insertion_sort(elements)
    print(elements)
    