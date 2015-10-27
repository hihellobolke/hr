def bitFlip(arr):
    r = get_redux(arr)
    return reduxion(r)


def get_redux(arr):
    redux = [0]
    for i in arr:
        if i == 1:
            if redux[-1] >= 0:
                redux[-1] += 1
            else:
                redux.append(1)
        elif i == 0:
            if redux[-1] <= 0:
                redux[-1] -= 1
            else:
                redux.append(-1)
    return redux


def reduxion(redux):
    sum_prev = sum(redux)
    sum_max_so_far = sum_prev
    sum_so_far = 0
    reduxed = []
    max_reduxed = []
    for i, r in enumerate(redux):
        if r > 0:
            continue
        else:
            reduxed = redux[:i]
            reduxed.append(-r)
            sum_so_far = sum(redux) + (2 * -r)
            t = 0
            skip = 0
            for j, s in enumerate(redux[i+1:], i+1):
                if j <= skip:
                    continue
                try:
                    s2 = redux[j+1]
                except:
                    s2 = 0
                if - (s + s2) >= 0:
                    reduxed += [-s, -s2]
                    sum_so_far += (-1 * (s + s2))
                    skip = j + 1
                else:
                    break
            if sum_so_far > sum_max_so_far:
                max_reduxed = reduxed + redux[len(reduxed):]
                reduxed = []
                sum_max_so_far = sum_so_far
    max_ones = 0
    for i in max_reduxed:
        if i > 0:
            max_ones += i
    return max_ones

print("\n\n")
print("Flip bit in slice of array to maximise overall 1's in the array. "
      "Then count the max 1's possible?\n")
arr = [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
print("Input: {}\nOutput: {}\n".format(arr, bitFlip(arr)))

arr = [1, 0, 0, 1, 0, 0, 1, 0]
print("Input: {}\nOutput: {}\n".format(arr, bitFlip(arr)))

arr = [1, 1, 1]
print("Input: {}\nOutput: {}\n".format(arr, bitFlip(arr)))

