
def heapify(arr,i):

	l = 2*i + 1
	r = 2*i + 2

	max_ = i

	print(i, l, r)
	

	if l<len(arr) and arr[l]>=arr[max_]:
		max_ = l
	
	if r<len(arr) and arr[r]>=arr[max_]:
		max_ = r
	print(max_)
	print(arr, "\n")
	if max_ != i :
		temp = arr[i]
		arr[i] = arr[max_]
		arr[max_] = temp
		
		heapify(arr,max_)


def heapSort(arr):

	n = len(arr)

	i = n//2 -1

	
        #Max heap
	while i >= 0 :
		heapify(arr,i)
		i-=1

	j=n-1
	while j <= 0 :
		temp = arr[0]
		arr[0] = arr[j]
		arr[j] = temp
		n = n-1
		heapify(arr, 0)
	print(arr)

arr = [int(x) for x in input().split()]

sorted_arry = heapSort(arr)
