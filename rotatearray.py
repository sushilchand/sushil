'''
Problem
=====================================================
Rotate the array by d elements. In the below code array is rotated by d = 3

Result
===============================================
array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
array('i', [4, 5, 6, 7, 8, 9, 1, 2, 3])
'''
import array

def reverse(arr, left, right):
	while(left < right):
		temp = arr[left]
		arr[left] = arr[right]
		arr[right] = temp
		left += 1
		right -= 1

arr = array.array('i', [1,2,3,4,5,6,7,8,9])
print(arr)
reverse(arr, 0, 2)
reverse(arr, 3, 8)
reverse(arr, 0, 8)
print(arr)


