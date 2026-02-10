
more = [x + 1 for x in [1,2,3,4]]     # 2, 3, 4, 5
print()                               # [2, 3, 4, 5]

###########################################################

def square(n:int) -> int:
    return n * n                           # n:return ; 1:1, 2:return 4, n=3:return 9, n=4:return 16

squares = [square(x) for x in [1,2,3,4]]   # The value of squares is a list [1,4,9,16] each value in the list is squared
print()

###########################################################

def check1(n:int) -> bool:
    return n > 2                             # n:return : 0:False, 1:False, 2:False, 3:True, 4:True


answer = [x for x in range(5) if check1(x)]   # [False, False, False, True, True]
print() 

###########################################################

def inc(m:int) -> int:
    return m + 1                             # m:return ; 0:1, 1:2, 2:3, 3:4, 4:5


def check2(n:int) -> bool:
    return n > 2                             # n:return ; 0:False, 1:False, 2:False, 3:True, 4:True


answer = [inc(x) for x in range(5) if check2(x)]   # [4,5]
print()

###########################################################
