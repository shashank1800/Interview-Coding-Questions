#print max repetation element
#2 2 3 3 3 4 5 1
#3
arr = [int(x) for x in input().split()]
    
di = dict()
for ele in arr:
    count = di.get(ele,0)+1
    di[ele] = count

max_ = 0
ele_ = -1
for key in di:
    if di[key]>max_:
        max_ = di[key]
        ele_ = key

print(ele_)
