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

def sockMerchant(ar):
    socks = create_dict(ar)
    pair_count = int(look_for_pairs(socks))
    print(pair_count)
    
def create_dict(ar):
    socks = {}
    for sock in ar: 
        if sock not in socks:
            socks[sock] = 1
        else:
            socks[sock] += 1
    return socks

def look_for_pairs(socks):
    pair_count = 0
    for key, val in socks.items():
        pairs = val/2
        count = pairs//1
        pair_count += count 
    return pair_count 

# sockMerchant([1,2,1,1,2,3])

def findMedian(arr):
    arr.sort()
    mid = (len(arr)/2)//1
    for count, val in enumerate(arr):
        if count == mid:
            print(val)

# findMedian([3,4,2,5,1])

def lonelyinteger(a):
    nums = {}
    for num in a:
        if num not in nums:
            nums[num] = 1
        else:
            nums[num] += 1
    for key, val in nums.items():
        if val < 2:
            print(key)
    
# lonelyinteger([4,4,3,2,2,5,5])

def diagonalDifference(arr):
    ltr = 0
    rtl = 0
    last = len(arr)-1
    for count, val in enumerate(arr):
        for num, value in enumerate(val): 
            if count == num:
                ltr += value
        position = last-count 
        rtl += val[position]
    diff = abs(ltr-rtl)
    print(diff)

# diagonalDifference([[2,4,5],[1,3,6],[8,7,9]])

def getMoneySpent(keyboards, drives, b):
    most_expensive = 0 
    
    for keyboard in keyboards:
        for drive in drives:
            cost = keyboard + drive
            if cost <= b:
                if cost > most_expensive:
                    most_expensive = cost 
    if most_expensive == 0:
        print(-1)
    else:
        print(most_expensive)

# getMoneySpent([40,10,25], [5,20,30], 50)

def angryProfessor(k, a):
    on_time = 0
    for student in a:
        if student <= 0:
            on_time += 1
    if on_time >= k:
        print("NO")
    else:
        print("YES")

# angryProfessor(3, [-5,-3,0,1,2])

def string_to_array(string):
    numbers = []
    array = string.split(" ")
    for i in array:
        numbers.append(int(i))
    return numbers

def countingSort(arr):
    frequency_array = []
    for i in range(100):
        frequency_array.append(0)
    for j in range(len(frequency_array)):
        for num in arr:
            if num == j:
                frequency_array[j] += 1 
    print(frequency_array)

test = "63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33"
numbers = string_to_array(test)
# countingSort(numbers)

def flippingMatrix(matrix):
    # say we have a four-by-four matrix 
    n = len(matrix)
    sum = 0
    # n//2 gives us the number of numbers in the upper left hand quadrant (we only loop through the numbers in the upper left hand quadtrant bc we'll be looking at their mirror values)
    for i in range(n//2):
        for j in range(n//2):
            # first i iteration
            # when i=0 and j=0, get the number in the [0,0] position, the [0,3] position, the [3,0] position, and the [3,3] position 
            # when i=0 and j=1, get the number in the [0,1] position, the [0,2] position, the [3,1] position, and the [3,2] position 
            
            # second i iteration
            # when i=1 and j=0, get the number in the [1,0] position, the [1,3] position, the [2,0] position, and the [2,3] position 
            # when i=1 and j=1, get the number in the [1,1] position, the [1,2] position, the [2,1] position, and the [2,2] position
            
            sum += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
            
            # first i iteration
            # when i=0 and j=0, max(112, 119, 62, 108) will add 119 to the sum 
            # when i=0 and j=1, max(42, 83, 98, 114) will add 114 to the sum

            # second i iteration
            # when i=1 and j=0, max(56, 49, 15, 43) will add 56 to the sum 
            # when i=1 and j=1, max(125, 56, 78, 101) will add 125 to the sum 

            # the total sum is 414

    return sum 

def towerBreakers(n, m): 
    if m == 1:
        print(2)
    if n%2 == 1:
        print(1)
    else:
        print(2)

# towerBreakers(2, 6)

def caesarCipher(s, k):
    encrypted = ""
    for i in s:
        if ord(i.lower()) >= 97 and ord(i.lower()) <= 122:
            if k <= 26:
                new_ascii = ord(i.lower()) + k
            else:
                times_around = k//26
                move = k - (26 * times_around)
                new_ascii = ord(i.lower()) + move
            if new_ascii <= 122:
                new_letter = chr(new_ascii)
                if i.isupper():
                    new_letter = new_letter.upper()
                encrypted += new_letter
            elif new_ascii > 122:
                diff = new_ascii - (122 + 1) 
                new_ascii = 97 + diff
                new_letter = chr(new_ascii)
                if i.isupper():
                    new_letter = new_letter.upper()
                encrypted += new_letter
        else:
            encrypted += i

    print(encrypted)

# caesarCipher("middle-Outz", 80)

def palindromeIndex(s):
    last = len(s)-1

    # loop through front and back of string 
    for i, f in enumerate(s):
        for j in range(last, -1, -1):
            # if "first" and "last" letters are the same, keep moving in and comparing letters
            if f == s[j]:
                last -= 1
                break
            # if "first" and "last" letters aren't the same...
            else:
                # look at string without the "first" letter and then without the "last" letter and see if either are palindromes 
                index = checkForPalindrome(s, i, j)
                print(index)
                return index
    print(-1)
    return -1

def checkForPalindrome(string, index_i, index_j):
    first_string = ""
    second_string = ""
    last_num = len(string)-2
    last = len(string)-2

    # create new strings without the "first" and "last" letter
    for letter in range(len(string)):
        if letter == index_i:
            pass
        else: 
            first_string += string[letter]
    
    for l in range(len(string)):
        if l == index_j:
            pass
        else:
            second_string += string[l]

    # loop through front and back of string
    for i, f in enumerate(first_string):
        for j in range(last_num, -1, -1):
            # if "first" and "last" letters are the same...
            if f == first_string[j]:
                # if i and j are at the same position or have crossed paths (if all of the "first" and "last" letters have been the same), return index_1 (position of the letter that needs to be removed to create a palindrome)
                if i == j or i > j:
                    return index_i 
                # else keep moving in and comparing letters
                else:
                    last_num -= 1
                    break
            # if the "first" and "last" letters of string 1 are not the same...
            else:
                # check for palindrome in the second string (same process as above) 
                for g, first in enumerate(second_string):
                    for h in range(last, -1, -1):
                        if first == second_string[h]:
                            if g == h or g > h:
                                return index_j 
                            else:
                                last -= 1
                                break
                        # if nothing has been returned, there's no palindromes; return -1
                        else:
                            return -1

# palindromeIndex('baa')

def str_to_arr(string):
    values = string.split("\n")
    return values

def gridChallenge(grid):
    new_grid = []
    for string in grid:
        ascii = []
        letters = []
        for letter in string:
            ascii.append(ord(letter))
        ascii.sort()
        for l in ascii:
            letters.append(chr(l))
        new_grid.append(''.join(letters))

    for index in range(len(new_grid[0])):
        columns = []
        for str in new_grid:
            for i in range(len(str)):
                if i == index:
                    columns.append(ord(str[i]))
                    break
        
        compare = 0
        for num in columns:
            if num >= compare:
                compare = num
                continue
            else:
                print("NO")
                return "NO"
            
    print("YES")
    return "YES"

test2 = """iv
sm"""

array = str_to_arr(test2)
# gridChallenge(array)

def superDigit(n, k):
    # the super digit of a number is closely related to its remainder when divided by 9

    # each digit in the number string is summed up and then multipled by how many times the number string repeats 

    # the -1 subtracts 1 from the sum of digits; if the super digit is 9, the remainder will be 0 since 9/9 leaves no remainder; in order to ensure we get a super digit of 9 (and not 0), we have to subtract 1 to get 8; then we do 8/9 which leaves us with a remainder of 8, and the +1 ensures our final answer is 9 

    # the +1 adds 1 to the remainder; if we have a super digit of 1, then doing -1 will give us 0; then we do 0/9 which leaves us with a remainder of 0, and the +1 ensures our final answer is 1 
    
    return 1 + (k * sum(int(num) for num in n) - 1) % 9

# superDigit('1111111111', 10)

def minimumBribes(q):
    bribes = 0 

    for position, person in enumerate(q):
        og_position = person-1
        if og_position - position > 2:
            print("Too chaotic")
            return
        
        # create a sublist of q using the numbers from the position before the og position (to capture larger numbers that bribed their way forward?) up until, but not including, the current position (the max function ensures that the index is at least 0, so if the og position is 0, we don't get an index of -1)

        # if the values in the sublist are greater than the current person, a bribe was made 

        for p in q[max(og_position - 1, 0):position]:
            if p > person:
                bribes += 1

    print(bribes)

# minimumBribes([1,2,5,3,7,8,6,4])

def truckTour(petrolpumps):
    remaining_gas = None
    start = None

    for count, station in enumerate(petrolpumps):
        if start:
            print(start)
            return start
        if station[1] <= station[0]:
            remaining_gas = station[0] - station[1]
            i = count + 1
            while i != count:
                if i <= len(petrolpumps)-1:
                    remaining_gas += petrolpumps[i][0]
                    remaining_gas -= petrolpumps[i][1]
                    if i == len(petrolpumps)-1:
                        i = -1
                    i += 1 
                    if remaining_gas < 0:
                        if count == start:
                            start = None
                        break
                    else:
                        start = count
                else:
                    i = 0

# truckTour([[1,5], [4,3], [1,4], [10,3], [8, 7]])

def mergeLists(head1, head2):
    # if one of the heads is empty, return the other one because there's no need to merge the heads
    if head1 == None:
        return head2
    if head2 == None:
        return head1 
    
    # the head that has the smaller number ("data") is made the head of the merged node, then we move on to the next "head" 
    if head1.data <= head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next

    # start at the head of the merged list
    current = head

    # while there's a value for either head1 or head2...
    while head1 != None or head2 != None:

        # if head1 is None, the next value becomes head2 (and each value in head2 has a next value that it points to, so essentially, the rest of the list is what's left in head2) and then the merged list is finished
        if head1 == None:
            current.next = head2
            break 
        if head2 == None:
            current.next = head1 
            break 
        
        # make the merged list's next whichever head's data is smaller and move to the next "head"
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next 

        # move to the next position in the merged list
        current = current.next

    return head

