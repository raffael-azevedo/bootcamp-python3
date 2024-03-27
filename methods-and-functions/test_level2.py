'''
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
'''

def has_33(mylist):
    for num in range(0, len(mylist)-1):
        if mylist[num] == 3 and mylist[num+1] == 3:
            return True
    return False


'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
'''

def paper_doll(word):
    triplet = []
    for letter in word:
        triplet.append(letter * 3)
    return ''.join(triplet)


'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
'''

def blackjack(a,b,c):
    if sum([a,b,c]) < 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c])-10
    else:
        return 'BUST'



'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9
 (every 6 will be followed by at least one 9). Return 0 for no numbers.
'''

def summer_69(mylist):
    final_sum = 0
    add = True
    for num in mylist:
        while add:
            if num != 6:
                final_sum += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return final_sum

## tests
def test_has_33():
    assert has_33([1, 3, 3]) is True
    assert has_33([1, 3, 1, 3]) is False
    assert has_33([3, 1, 1, 3, 3]) is True
    assert has_33([3, 1, 3]) is False

def test_paper_doll():
    assert paper_doll('Hello') == 'HHHeeellllllooo'
    assert paper_doll('Mississippi') == 'MMMiiissssssiiissssssiiippppppiii'

def test_blackjack():
    assert blackjack(5,6,7) == 18
    assert blackjack(9,9,9) == 'BUST'
    assert blackjack(5,11,11) == 17

def test_summer_69():
    assert summer_69([1, 3, 5]) == 9
    assert summer_69([4, 5, 6, 7, 8, 9]) == 9
    assert summer_69([2, 1, 6, 9, 11]) == 14