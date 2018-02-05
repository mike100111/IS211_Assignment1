class ListDivideException(Exception):
    pass

def listDivide(numbers, divide = 2):
    count = 0
    for x in numbers:
        if x % divide == 0:
            count += 1
    return count

def testListDivide():
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30, 54, 63,98, 100], divide=10)
        listDivide(['hi'])
        listDivide([1,2,3,4,5], 1)
    except:
        raise ListDivideException

testListDivide()

