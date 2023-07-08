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

def timeConversion(s):
    military_time = []
    convert = "no"
    hour = 0
    time = s.split(":")
    
    for count, val in enumerate(time):
        if count == 0:
            hour = val
        if count == 2:
            seconds = list(val)
            if "P" in seconds and hour != "12":
                    convert = "yes"
            if "A" in seconds and hour == "12":
                convert = "yes"
            for i in range(len(seconds)-1, 1, -1):
                seconds.pop()
    seconds = ''.join(seconds)

    for i, m in enumerate(time):
        if i == 0:
            if convert == "yes" and hour != "12":
                hour = int(m) + 12
                military_time.append(str(hour))
            elif convert == "yes" and hour == "12":
                hour = int(m) - 12
                military_time.append("0"+str(hour))
            else:
                military_time.append(m)
        if i == 1:
            military_time.append(m)
        if i == 2:
            military_time.append(seconds)
        
    new_time = ":".join(military_time)
    print(new_time)

# timeConversion("09:01:00AM")

def fizzBuzz(n):
    for i in range(1, n+1):
        if i%3 == 0: 
            if i%5 == 0:
                print("Fizzbuzz")
            else: 
                print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else: 
            print(i)

# fizzBuzz(65)

def breakPalindrome(palindromeStr):
    highest_val = find_highest_val(palindromeStr)
    new_string = create_new(palindromeStr, highest_val)

    if new_string == palindromeStr:
        print("IMPOSSIBLE")
    elif len(new_string)%2 == 0:
        print(new_string)
    elif len(new_string)%2 != 0:
        impossible = look_for_palindrome(new_string)
        if impossible == "yes":
            print("IMPOSSIBLE")
        else: 
            print(new_string)

def find_highest_val(palindromeStr):
    highest_val = palindromeStr[0]
    for i in palindromeStr:
        if i > highest_val:
            highest_val = i
    return highest_val

def create_new(palindromeStr, highest_val):
    new_string = ""
    replaced = 0
    for i in palindromeStr: 
        if replaced == 0 and i == highest_val:
            new_string += "a"
            replaced += 1 
        else: 
            new_string += i
    return new_string

def look_for_palindrome(new_string):
    impossible = "no"
    for count, val in enumerate(new_string):
        count = count + 1
        for i in range(len(new_string)-count, count, -1):
            if val == new_string[i]:
                impossible = "yes"
                break
            else: 
                impossible = "no"
                break
    return impossible

# breakPalindrome("abcaa")

def areAlmostEquivalent(s, t):
    answer = []

    for i in range(len(s)):
        strings = get_one_string(i, s, t)
        difference = compare_lengths(strings)
        if difference != 0:
            answer.append("NO")
        else: 
            count_dict = count_letters(strings)
            boolean = compare_count(count_dict)
            if boolean == "yes":
                answer.append("YES")
            else:
                answer.append("NO")
    print(answer)

def get_one_string(num, s, t):
    for count, val in enumerate(s):
        if count == num:
            s_string = val
    for c, v in enumerate(t):
        if c == num:
            t_string = v
    return [s_string, t_string]

def compare_lengths(strings):
    difference = len(strings[0]) - len(strings[1])
    return difference 

def count_letters(strings):
    letters_s = {}
    letters_t = {}
    for i in strings[0]: 
        if i not in letters_s: 
            letters_s[i] = 1
        else:
            letters_s[i] += 1
    for j in strings[1]:
        if j not in letters_t:
            letters_t[j] = 1
        else: 
            letters_t[j] += 1 
    return [letters_s, letters_t]
    
def compare_count(count_dict):
    diff_arr = []
    answer = "yes"
    for key in count_dict[0]:
        if key not in count_dict[1]:
            count_dict[1][key] = 0
    for k in count_dict[1]:
        if k not in count_dict[0]:
            count_dict[0][k] = 0

    for letter, count in count_dict[0].items():
        difference = abs(count - count_dict[1][letter])
        diff_arr.append(difference)

    for i in diff_arr:
        if i > 3:
            answer = "no"
    return answer

# areAlmostEquivalent(['aab', 'aabbcc', 'aab'], ['bbabbc', 'abbbcc', 'bab'])

def migratoryBirds(arr):
    bird_types = count_type(arr)
    m = max_sighting(bird_types)
    min_type = check_for_dupes(m, bird_types)
    print(min_type)
    
def count_type(arr):
    bird_types = {}
    for num in arr:
        if num not in bird_types:
            bird_types[num] = 1
        else:
            bird_types[num] += 1 
    return bird_types 
    
def max_sighting(bird_types):
    m = None
    
    for key, val in bird_types.items():
        if m == None:
            m = val 
        elif val > m:
            m = val
    return m
    
def check_for_dupes(m, bird_types):
    duplicates = []
    min_type = None
    
    for key, val in bird_types.items():
        if val == m:
            duplicates.append(key)
    if len(duplicates) > 0:
        for i in duplicates:
            if min_type == None:
                min_type = i
            elif i < min_type:
                min_type = i
    else:
        min_type = duplicates[0]      
    return min_type

# migratoryBirds([1,1,2,2,3])

def catAndMouse(x, y, z):
    catADiff = abs(z-x)
    catBDiff = abs(z-y)
    
    if catADiff > catBDiff:
        print("Cat B")
    elif catADiff < catBDiff:
        print("Cat A")
    else:
        print("Mouse C")

# catAndMouse(1,5,4)

def hurdleRace(k, height):
    highest = height[0]
    
    for i in height:
        if i > highest:
            highest = i
    
    if highest > k:
        doses = highest-k
        print(doses)
    else:
        print(0)

# hurdleRace(4, [1,2,3,5,6])
