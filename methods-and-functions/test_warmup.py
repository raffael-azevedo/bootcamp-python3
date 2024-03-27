'''
LESSER OF TWO EVENS: Write a function that returns the lesser 
of two given numbers if both numbers are even, 
but returns the greater if one or both numbers are odd
'''

def lesser_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b


'''
ANIMAL CRACKERS: Write a function takes a two-word string 
and returns True if both words begin with same letter
'''

def animal_crackers(text):
    word1,word2 = text.split(' ')
    if word1[0].upper() == word2[0].upper():
        return True
    else:
        return False

'''
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
or if one of the integers is 20. If not, return False
'''

def makes_twenty(a,b):
    if sum((a,b)) == 20 or a == 20 or b == 20:
        return True
    else:
        return False




## tests
def test_lesser_of_two():
    assert lesser_two_evens(2,4) == 2
    assert lesser_two_evens(2,5) == 5

def test_animal_crackers():
    assert animal_crackers('Levelheaded Llama') is True
    assert animal_crackers('Crazy Kangaroo') is False

def test_makes_twenty():
    makes_twenty(20,10) is True
    makes_twenty(12,8) is True
    makes_twenty(2,3) is False