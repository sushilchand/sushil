'''

Problem: Binary search on sorted rotated array

'''
'''def find_pivot(arr, l, h):
	if l>h:
		return -1
	if l == h:
		return l
	mid = int((l+h)/2)
	if arr[mid-1] > arr[mid]: # found pivot element
		return mid
	if arr[mid] > arr[mid-1] and arr[l] > arr[mid]: # lowest element is greated than mid means pivot is at left side
		return find_pivot(arr, l, mid-1)
	return find_pivot(arr, mid+1, h)  # else pivot is at right side



def binarysearch(arr, l, h, key):
	if h<l:
		return -1
	mid = int((l+h)/2)
	if arr[mid] == key:
		return mid
	if key < arr[mid]:
		return binarysearch(arr, l, mid-1, key)
	return binarysearch(arr, mid+1, h, key)

def pivotsearch(arr, l, h, key):
	_piv = find_pivot(arr, l, h)
	if _piv == -1: # array is not rotated
		binarysearch(arr, 0, len(arr), key)
	if arr[_piv] == key:
		return _piv
	if arr[_piv] > arr[l]: # pivot is present at left side
		return binarysearch(arr, l, _piv-1, key)
	else: # pivot is present at right side
		return binarysearch(arr, _piv+1, h, key)
'''
def search(arr, l, h, key):
	if h<l:
		return -1
	mid = int((l+h)/2)
	if arr[mid] == key:
		return mid
	if(arr[l] <= arr[mid]): # left subarray is sorted
		if key <= arr[mid] and key >= arr[l]: # search for left part
			return search(arr, l, mid-1, key)
		return search(arr, mid+1, h, key) # search for right part
	# else right subarray is sorted
	if key >= arr[mid] and key <= arr[h]: # search for right part
		return search(arr, mid+1, h, key)
	return search(arr, l, mid-1, key) # search for left part


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3
# ans = pivotsearch(arr, 0, len(arr), key)
ans = search(arr, 0, len(arr)-1, key)
print (ans)