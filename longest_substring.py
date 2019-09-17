#ABAB
#BABC
#3

def substring(string1,string2):
    count = 0
    for char in string1:
        if count<len(string2) and char == string2[count]:
            count +=1
        else:
            return count
    return count

string1 = input()
string2 = input()

matrix = []
len1 = len(string1)
len2 = len(string2)

for i in range(len1):
    matrix.append([0]*len2)

for i in range(len1):
    for j in range(len2):
        substring_length = substring(string1[i:],string2[j:])
        matrix[i][j] = substring_length
max_=0
for row in matrix:
    if max_<max(row):
        max_ = max(row)

print(max_)
