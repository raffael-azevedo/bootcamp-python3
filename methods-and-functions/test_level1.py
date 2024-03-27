'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
'''

def old_macdonald(name):
    splitted_name = [*name]
    splitted_name[0] = splitted_name[0].upper()
    splitted_name[3] = splitted_name[3].upper()
    return ''.join(splitted_name)



'''
MASTER YODA: Given a sentence, return a sentence with the words reversed
'''

def master_yoda(sentence):
    splitted_sentence = sentence.split(' ')
    yoda_sentence = ' '.join(splitted_sentence[::-1])
    return yoda_sentence


'''
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
'''

def almost_there(n):
    for i in range(0,10):
        if n+i == 100 or n+i == 200:
            return True
        elif n-i == 100 or n-i == 200:
            return True
    return False

# tests
def test_old_macdonald():
    assert old_macdonald('macdonald') == 'MacDonald'
    assert old_macdonald('macdo nald') == 'MacDo nald'

def test_master_yoda():
    assert master_yoda('I am home') == 'home am I'
    assert master_yoda('We are ready') == 'ready are We'

def test_almost_there():
    assert almost_there(104) is True
    assert almost_there(150) is False
    assert almost_there(1) is False
    assert almost_there(203) is True