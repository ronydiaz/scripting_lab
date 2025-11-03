#!/usr/bin/env python3

# Given a array: [[1,3],[2,5],[6,10]]
# Detect the overlap with the numbers and replacethem like: [[1,5][6,10]]


#original_array=[[1,3],[2,5],[6,10]]
original_array=[[1,4],[5,7],[6,10],[9,16]]

def find_overlap(array):
    
    i=0
    flag=True
    while(flag):

        print(i)
        if array[i][1] >= array[i+1][0]:
         
            array.insert(i+2,[array[i][0], array[i+1][1]])

            array.pop(i)
            array.pop(i)
            
            i = 0
        else:
            i += 1

        if i==(len(array)-1):
            flag=False

    print(array)


original_array=[[1,3],[2,5],[6,10]]
find_overlap(original_array)

original_array=[[1,4],[5,7],[6,10],[9,16]]
find_overlap(original_array)

original_array=[[3,5],[5,7],[8,10],[9,16],[15,18]]
find_overlap(original_array)



