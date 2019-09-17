#input:{1,3,4,5} d = 8
#output:{1,3,4},{3,5}
#1 2 4 5
#8
#[[1,3,4],[3,5]]


array = [int(x) for x in input().split()]
d = int(input())

result_array = []

def subset(array,d):

    if len(array)==0:
        return

    if sum(array)==d and array not in result_array:
            result_array.append(array)
    
    for i in range(0,len(array)):
        subset(array[0:i]+array[i+1:],d)
        
subset(array,d)
print(result_array)
