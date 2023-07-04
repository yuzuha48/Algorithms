def breakingRecords(scores):
    max_score = scores[0]
    max_count = 0
    min_score = scores[0]
    min_count = 0 
    
    for count, value in enumerate(scores):
        if count == 0:
            continue
        elif value > max_score:
            max_score = value
            max_count += 1
        elif value < min_score:
            min_score = value
            min_count += 1 
            
    print(max_count, min_count)

# breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])

def birthday(s, d, m):
    day = 0
    count = 0

    for i, val2 in enumerate(s):
        for j, val in enumerate(s):
            j = j+1
            if j <= i:
                continue
            elif j > i:
                if day < d: 
                    day += val 
                    if day == d: 
                        if j-i == m:
                            count += 1
                            day = 0
                            break
                        else:
                            day = 0
                            break
                    elif day > d:
                        day = 0
                        break
    print(count)

# birthday([1,2,1,3,2], 3, 2)

def divisibleSumPairs(n, k, ar):
    count = 0 
    positions = []
    for i, val_i in enumerate(ar):
        for j, val_j in enumerate(ar):
            if i != j:
                if (val_i+val_j)%k == 0:
                    if [j,i] in positions:
                        continue
                    else:
                        count += 1
                        positions.append([i,j])
            else:
                continue
    print(count)

# divisibleSumPairs(6, 5, [1,2,3,4,5,6])

def bonAppetit(bill, k, b):
    total = 0
    for count, val in enumerate(bill):
        if count != k:
            total += val
    anna = int(total/2)
    if b == anna:
        print("Bon Appetit")
    else:
        difference = b-anna 
        print(difference)

    
# bonAppetit([2,4,6], 2, 6)

def plusMinus(arr):
    pos = 0
    zero = 0
    neg = 0
    arr_len = len(arr)
    for i in arr:
        if i > 0: 
            pos += 1 
        if i == 0:
            zero += 1
        if i < 0:
            neg += 1 
    print("{:.6f}".format(pos/arr_len))
    print("{:.6f}".format(neg/arr_len))
    print("{:.6f}".format(zero/arr_len))

# plusMinus([-4, 3, -9, 0, 4, 1])

def miniMaxSum(arr):
    arr.sort()
    min_sum = 0
    max_sum = 0 
    for count, val in enumerate(arr):
        if count < len(arr)-1:
            min_sum += val 
    
    for count2, val2 in reversed(list(enumerate(arr))):
        if count2 > 0:
            max_sum += val2

    print(min_sum, max_sum)

# miniMaxSum([1, 2, 3, 4, 5])