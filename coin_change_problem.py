sum_ = 10
arr_ = [2, 5, 3, 6]

def count():
    combination = [0]*(sum_+1)
    combination[0]=1

    print(combination)

    for coin in arr_:
        for amount in range(0,sum_+1):
            if amount >= coin:
                combination[amount] += combination[amount-coin]
                print(combination)
            
    return combination[sum_]

result = count()
print(result)
