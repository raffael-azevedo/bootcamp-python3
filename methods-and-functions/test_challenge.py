'''
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
'''

def spy_game(arr):
    codename = [0,0,7,'x']
    for num in arr:
        if num == codename[0]:
            codename.pop(0)
    return len(codename) == 1



'''
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
'''

def count_primes(num):
    primes = [2]
    x = 3
    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return len(primes)

'''
PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
'''


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    letters = {"a": [1,2,4,3,3], "b": [5,3,5,3,5], "c": [4,9,9,9,4], "d": [5,3,3,3,5], "e": [4,9,4,9,4]}

    for pattern in letters[letter]:
        print(patterns[pattern])    

print_big('a')
print_big('b')
print_big('c')
print_big('d')
print_big('e')

# tests

def test_spy_game():
    assert spy_game([1,2,4,0,0,7,5]) is True
    assert spy_game([1,0,2,4,0,5,7]) is True
    assert spy_game([1,7,2,0,4,5,0]) is False

def test_count_primes():
    assert count_primes(100) == 25