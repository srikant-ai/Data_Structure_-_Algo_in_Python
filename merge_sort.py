# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 01:32:25 2021

@author: Srikanth Sahoo
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_arrays(left, right , arr)
    
def merge_sorted_arrays(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    
    while i < len_a and j < len_b :
        if a[i] <= b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i < len_a:
        arr[k]=a[i]
        i+=1
        k+=1
    while j < len_b:
        arr[k]=b[j]
        j+=1
        k+=1

if __name__  == '__main__':
    #a=[2,4,7,11,93]
    #b=[1,3,5,6,8,9]
    arr = [23,4,6,1,11,2,4,7,2,8,8,1]
    merge_sort(arr)
    print(arr)