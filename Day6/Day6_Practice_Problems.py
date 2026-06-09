# Day 6: Big O Notation Reference Code & Practice
# Analyze the Time and Space Complexity for each snippet.

#----------------------------------------
# CATEGORY 1: O(1) CONSTANT TIME
#----------------------------------------

def snippet_1(arr):
    # Expected Time: O(1) | Expected Space: O(1)
    if len(arr) > 1:
        return arr[0]
    return None

def snippet_2(arr):
    # Expected Time: O(1) | Expected Space: O(1)
    if len(arr) > 2:
        return arr[1]
    return None

def snippet_3(arr):
    # Expected Time: O(1) | Expected Space: O(1)
    if len(arr) > 3:
        return arr[2]
    return None

def snippet_4(arr):
    # Expected Time: O(1) | Expected Space: O(1)
    if len(arr) > 4:
        return arr[3]
    return None

def snippet_5(arr):
    # Expected Time: O(1) | Expected Space: O(1)
    if len(arr) > 5:
        return arr[4]
    return None

def snippet_6(arr):
    # Expected Time: O(1) | Expected Space: O(1)
    if len(arr) > 6:
        return arr[5]
    return None

def snippet_7(arr):
    # Expected Time: O(1) | Expected Space: O(1)
    if len(arr) > 7:
        return arr[6]
    return None

def snippet_8(arr):
    # Expected Time: O(1) | Expected Space: O(1)
    if len(arr) > 8:
        return arr[7]
    return None

def snippet_9(arr):
    # Expected Time: O(1) | Expected Space: O(1)
    if len(arr) > 9:
        return arr[8]
    return None

def snippet_10(arr):
    # Expected Time: O(1) | Expected Space: O(1)
    if len(arr) > 10:
        return arr[9]
    return None

#----------------------------------------
# CATEGORY 2: O(log N) LOGARITHMIC TIME
#----------------------------------------

def snippet_11(n):
    # Expected Time: O(log N) | Expected Space: O(1)
    steps = 0
    while n > 1:
        n = n // 2
        steps += 1
    return steps

def snippet_12(n):
    # Expected Time: O(log N) | Expected Space: O(1)
    steps = 0
    while n > 2:
        n = n // 2
        steps += 1
    return steps

def snippet_13(n):
    # Expected Time: O(log N) | Expected Space: O(1)
    steps = 0
    while n > 3:
        n = n // 2
        steps += 1
    return steps

def snippet_14(n):
    # Expected Time: O(log N) | Expected Space: O(1)
    steps = 0
    while n > 4:
        n = n // 2
        steps += 1
    return steps

def snippet_15(n):
    # Expected Time: O(log N) | Expected Space: O(1)
    steps = 0
    while n > 5:
        n = n // 2
        steps += 1
    return steps

def snippet_16(n):
    # Expected Time: O(log N) | Expected Space: O(1)
    steps = 0
    while n > 6:
        n = n // 2
        steps += 1
    return steps

def snippet_17(n):
    # Expected Time: O(log N) | Expected Space: O(1)
    steps = 0
    while n > 7:
        n = n // 2
        steps += 1
    return steps

def snippet_18(n):
    # Expected Time: O(log N) | Expected Space: O(1)
    steps = 0
    while n > 8:
        n = n // 2
        steps += 1
    return steps

def snippet_19(n):
    # Expected Time: O(log N) | Expected Space: O(1)
    steps = 0
    while n > 9:
        n = n // 2
        steps += 1
    return steps

def snippet_20(n):
    # Expected Time: O(log N) | Expected Space: O(1)
    steps = 0
    while n > 10:
        n = n // 2
        steps += 1
    return steps

#----------------------------------------
# CATEGORY 3: O(N) LINEAR TIME
#----------------------------------------

def snippet_21(arr):
    # Expected Time: O(N) | Expected Space: O(1)
    total = 0
    for x in arr:
        total += x + 1
    return total

def snippet_22(arr):
    # Expected Time: O(N) | Expected Space: O(1)
    total = 0
    for x in arr:
        total += x + 2
    return total

def snippet_23(arr):
    # Expected Time: O(N) | Expected Space: O(1)
    total = 0
    for x in arr:
        total += x + 3
    return total

def snippet_24(arr):
    # Expected Time: O(N) | Expected Space: O(1)
    total = 0
    for x in arr:
        total += x + 4
    return total

def snippet_25(arr):
    # Expected Time: O(N) | Expected Space: O(1)
    total = 0
    for x in arr:
        total += x + 5
    return total

def snippet_26(arr):
    # Expected Time: O(N) | Expected Space: O(1)
    total = 0
    for x in arr:
        total += x + 6
    return total

def snippet_27(arr):
    # Expected Time: O(N) | Expected Space: O(1)
    total = 0
    for x in arr:
        total += x + 7
    return total

def snippet_28(arr):
    # Expected Time: O(N) | Expected Space: O(1)
    total = 0
    for x in arr:
        total += x + 8
    return total

def snippet_29(arr):
    # Expected Time: O(N) | Expected Space: O(1)
    total = 0
    for x in arr:
        total += x + 9
    return total

def snippet_30(arr):
    # Expected Time: O(N) | Expected Space: O(1)
    total = 0
    for x in arr:
        total += x + 10
    return total

#----------------------------------------
# CATEGORY 4: O(N log N) LINEARITHMIC TIME
#----------------------------------------

def snippet_31(n):
    # Expected Time: O(N log N) | Expected Space: O(1)
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j = j // 2
            count += 1
    return count

def snippet_32(n):
    # Expected Time: O(N log N) | Expected Space: O(1)
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j = j // 2
            count += 1
    return count

def snippet_33(n):
    # Expected Time: O(N log N) | Expected Space: O(1)
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j = j // 2
            count += 1
    return count

def snippet_34(n):
    # Expected Time: O(N log N) | Expected Space: O(1)
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j = j // 2
            count += 1
    return count

def snippet_35(n):
    # Expected Time: O(N log N) | Expected Space: O(1)
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j = j // 2
            count += 1
    return count

def snippet_36(n):
    # Expected Time: O(N log N) | Expected Space: O(1)
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j = j // 2
            count += 1
    return count

def snippet_37(n):
    # Expected Time: O(N log N) | Expected Space: O(1)
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j = j // 2
            count += 1
    return count

def snippet_38(n):
    # Expected Time: O(N log N) | Expected Space: O(1)
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j = j // 2
            count += 1
    return count

def snippet_39(n):
    # Expected Time: O(N log N) | Expected Space: O(1)
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j = j // 2
            count += 1
    return count

def snippet_40(n):
    # Expected Time: O(N log N) | Expected Space: O(1)
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j = j // 2
            count += 1
    return count

#----------------------------------------
# CATEGORY 5: O(N^2) QUADRATIC TIME
#----------------------------------------

def snippet_41(arr):
    # Expected Time: O(N^2) | Expected Space: O(1)
    pairs_found = 0
    for x in arr:
        for y in arr:
            if x + y == 10:
                pairs_found += 1
    return pairs_found

def snippet_42(arr):
    # Expected Time: O(N^2) | Expected Space: O(1)
    pairs_found = 0
    for x in arr:
        for y in arr:
            if x + y == 20:
                pairs_found += 1
    return pairs_found

def snippet_43(arr):
    # Expected Time: O(N^2) | Expected Space: O(1)
    pairs_found = 0
    for x in arr:
        for y in arr:
            if x + y == 30:
                pairs_found += 1
    return pairs_found

def snippet_44(arr):
    # Expected Time: O(N^2) | Expected Space: O(1)
    pairs_found = 0
    for x in arr:
        for y in arr:
            if x + y == 40:
                pairs_found += 1
    return pairs_found

def snippet_45(arr):
    # Expected Time: O(N^2) | Expected Space: O(1)
    pairs_found = 0
    for x in arr:
        for y in arr:
            if x + y == 50:
                pairs_found += 1
    return pairs_found

def snippet_46(arr):
    # Expected Time: O(N^2) | Expected Space: O(1)
    pairs_found = 0
    for x in arr:
        for y in arr:
            if x + y == 60:
                pairs_found += 1
    return pairs_found

def snippet_47(arr):
    # Expected Time: O(N^2) | Expected Space: O(1)
    pairs_found = 0
    for x in arr:
        for y in arr:
            if x + y == 70:
                pairs_found += 1
    return pairs_found

def snippet_48(arr):
    # Expected Time: O(N^2) | Expected Space: O(1)
    pairs_found = 0
    for x in arr:
        for y in arr:
            if x + y == 80:
                pairs_found += 1
    return pairs_found

def snippet_49(arr):
    # Expected Time: O(N^2) | Expected Space: O(1)
    pairs_found = 0
    for x in arr:
        for y in arr:
            if x + y == 90:
                pairs_found += 1
    return pairs_found

def snippet_50(arr):
    # Expected Time: O(N^2) | Expected Space: O(1)
    pairs_found = 0
    for x in arr:
        for y in arr:
            if x + y == 100:
                pairs_found += 1
    return pairs_found

#----------------------------------------
# CATEGORY 6: O(N^3) CUBIC TIME
#----------------------------------------

def snippet_51(arr):
    # Expected Time: O(N^3) | Expected Space: O(1)
    triplets = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets += 1
    return triplets

def snippet_52(arr):
    # Expected Time: O(N^3) | Expected Space: O(1)
    triplets = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets += 1
    return triplets

def snippet_53(arr):
    # Expected Time: O(N^3) | Expected Space: O(1)
    triplets = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets += 1
    return triplets

def snippet_54(arr):
    # Expected Time: O(N^3) | Expected Space: O(1)
    triplets = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets += 1
    return triplets

def snippet_55(arr):
    # Expected Time: O(N^3) | Expected Space: O(1)
    triplets = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets += 1
    return triplets

def snippet_56(arr):
    # Expected Time: O(N^3) | Expected Space: O(1)
    triplets = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets += 1
    return triplets

def snippet_57(arr):
    # Expected Time: O(N^3) | Expected Space: O(1)
    triplets = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets += 1
    return triplets

def snippet_58(arr):
    # Expected Time: O(N^3) | Expected Space: O(1)
    triplets = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets += 1
    return triplets

def snippet_59(arr):
    # Expected Time: O(N^3) | Expected Space: O(1)
    triplets = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets += 1
    return triplets

def snippet_60(arr):
    # Expected Time: O(N^3) | Expected Space: O(1)
    triplets = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets += 1
    return triplets

#----------------------------------------
# CATEGORY 7: O(2^N) EXPONENTIAL TIME
#----------------------------------------

def snippet_61(n):
    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack
    if n <= 1:
        return n
    return snippet_61(n - 1) + snippet_61(n - 2)

def snippet_62(n):
    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack
    if n <= 1:
        return n
    return snippet_62(n - 1) + snippet_62(n - 2)

def snippet_63(n):
    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack
    if n <= 1:
        return n
    return snippet_63(n - 1) + snippet_63(n - 2)

def snippet_64(n):
    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack
    if n <= 1:
        return n
    return snippet_64(n - 1) + snippet_64(n - 2)

def snippet_65(n):
    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack
    if n <= 1:
        return n
    return snippet_65(n - 1) + snippet_65(n - 2)

def snippet_66(n):
    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack
    if n <= 1:
        return n
    return snippet_66(n - 1) + snippet_66(n - 2)

def snippet_67(n):
    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack
    if n <= 1:
        return n
    return snippet_67(n - 1) + snippet_67(n - 2)

def snippet_68(n):
    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack
    if n <= 1:
        return n
    return snippet_68(n - 1) + snippet_68(n - 2)

def snippet_69(n):
    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack
    if n <= 1:
        return n
    return snippet_69(n - 1) + snippet_69(n - 2)

def snippet_70(n):
    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack
    if n <= 1:
        return n
    return snippet_70(n - 1) + snippet_70(n - 2)

#----------------------------------------
# CATEGORY 8: O(N) SPACE COMPLEXITY
#----------------------------------------

def snippet_71(arr):
    # Expected Time: O(N) | Expected Space: O(N)
    new_array = []
    for x in arr:
        new_array.append(x * 1)
    return new_array

def snippet_72(arr):
    # Expected Time: O(N) | Expected Space: O(N)
    new_array = []
    for x in arr:
        new_array.append(x * 2)
    return new_array

def snippet_73(arr):
    # Expected Time: O(N) | Expected Space: O(N)
    new_array = []
    for x in arr:
        new_array.append(x * 3)
    return new_array

def snippet_74(arr):
    # Expected Time: O(N) | Expected Space: O(N)
    new_array = []
    for x in arr:
        new_array.append(x * 4)
    return new_array

def snippet_75(arr):
    # Expected Time: O(N) | Expected Space: O(N)
    new_array = []
    for x in arr:
        new_array.append(x * 5)
    return new_array

def snippet_76(arr):
    # Expected Time: O(N) | Expected Space: O(N)
    new_array = []
    for x in arr:
        new_array.append(x * 6)
    return new_array

def snippet_77(arr):
    # Expected Time: O(N) | Expected Space: O(N)
    new_array = []
    for x in arr:
        new_array.append(x * 7)
    return new_array

def snippet_78(arr):
    # Expected Time: O(N) | Expected Space: O(N)
    new_array = []
    for x in arr:
        new_array.append(x * 8)
    return new_array

def snippet_79(arr):
    # Expected Time: O(N) | Expected Space: O(N)
    new_array = []
    for x in arr:
        new_array.append(x * 9)
    return new_array

def snippet_80(arr):
    # Expected Time: O(N) | Expected Space: O(N)
    new_array = []
    for x in arr:
        new_array.append(x * 10)
    return new_array

