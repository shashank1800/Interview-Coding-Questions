def second(tupple):
    return tupple[0]
def sort_fun(a):
    list_ = sorted(a,key = second)
    return list_

a = [(20,5),(30,4),(10,6)]
result = sort_fun(a)
print(result)
