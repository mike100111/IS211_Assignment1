class ListDivideException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

def listDivide( numbers, divide = 2):
    count = 0
    for x in numbers:
        if x % divide is 0:
            count += 1
    return count


def testListDivide():
    listDivide('hi')
    listDivide([2,4,6,8,10])
    listDivide([30, 54, 63,98, 100], divide=10)
    listDivide([])
    listDivide([1,2,3,4,5], 1)

try:
    testListDivide()
except:
    raise ListDivideException('Error')
