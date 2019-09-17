str_ = input()

lenby2 = len(str_)//2

index = lenby2

stack = []
for i in range(index):
    stack.append(str_[i])
if len(str_)%2 != 0:
    index+=1

for i in range(index,len(str_)):
    top = stack.pop()
    if str_[i] != top:
        print("NO")
        break

else:
    print("YES")
