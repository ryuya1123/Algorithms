#python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:17:05 2020

@author: ryuya11235
"""

'''
*Formuration
 input: n<a1,a2...an>
 output: a1' <= a2' <= ... <= an

'''

def insertion_sort():
    A = list(map(int, input('please input array: ').split()))
    for i in range(1,len(A)):
        key = A[i]
        
        j = i - 1
        
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            
            j = j - 1
            
        A[j+1] = key
    return A

print(insertion_sort())





