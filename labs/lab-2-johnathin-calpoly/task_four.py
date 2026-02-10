from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # line 12: False, line 13: True
    if test:                            # If test evaluated to True
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # None
second = checked_access([1, 0, 1], 2)    # return L[2] = 1
print()



def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])      # Line 30 result = 4 + 2 + 3 = 9
    elif len(L) > 1:
        result = len(L[0]) + len(L[1])                  # Line 32 result = 7 + 4 = 11
    elif len(L) > 0:
        result = len(L[0])                              # Line 31 result = 11
    else:
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()



def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # list type : ["this", "is", "confusing", "code."]
         # first = list type : ["this", "is", "confusing", "code.", "AVOID"]
         # second = list type : ["this", "is", "confusing", "code.", "AVOID", "SUCH"]
         # Added the string elements "AVOID" and "SUCH" to the list called "words"
print()