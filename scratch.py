def area(width: float, height: float) -> float:
    if width >= 0 and height >= 0:
        return float(width * height)
    return float(0)

# tests
test1 = area(1,1)
test2 = area(2.0,2.0)
test3 = area(-1, 1)
test4 = area(1, -1)

# print tests
print(test1)
print(test2)
print(test3)
print(test4)
