# -*- coding: utf-8 -*-
"""
Bubble Sort Assignment Program implementation in Python
"""

def bubble_sort(elements, key=None):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j][key] > elements[j+1][key]:
                temp = elements[j+1][key]
                elements[j+1][key]=elements[j][key]
                elements[j][key]=temp
                swapped = True
        if not swapped:
            break
            
if __name__ == '__main__':
    
    elements = [
            { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
            { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
            { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
            { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]
    bubble_sort(elements,key='transaction_amount')
    print(elements)
    
    