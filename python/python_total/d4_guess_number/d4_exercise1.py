#!/usr/bin/env python3

def return_distinct(int1, int2, int3):
    total = int1 + int2 + int3
    
    if total > 15:
        return max(int1, int2, int3)
    elif total < 10:
        return min(int1, int2, int3)
    else:
        # The middle number = total - min - max
        return total - min(int1, int2, int3) - max(int1, int2, int3)

print(return_distinct(1, 3, 4))

