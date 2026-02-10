def smallest(n:float, m:float) -> float:
    if n < m:
        return n                # Call on line 8
    else:
        return m                # Call on line 7

first = smallest(3, 2)     # returns m; 2.0
second = smallest(2, 2)    # returns n; 2.0
print()

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b            # When int a is greater that
                                # int b and a is greater than c.
    elif b > c:
        return b + c            # When int b is greater than int c.
    else:
        return 2 * c            # If int a is not greater than int b
                                # and a is not greater than int c and
                                # b is not greater than c.


answer1 = function2(3, 2, 1)     # int 1
answer2 = function2(2, 3, 1)     # int 4
answer3 = function2(2, 1, 3)     # int 2 * 3 = 6
print()