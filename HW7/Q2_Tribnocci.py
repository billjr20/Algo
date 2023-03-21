def good_bit_strings(n):
    if n < 1:
        raise ValueError
    if n == 1:
        return 2
    elif n == 2:
        return 4
    elif n == 3:
        return 7
    trib_arr = [0] * (n)
    trib_arr[0], trib_arr[1], trib_arr[2] = 2, 4, 7

    
    for i in range(3, n):
        trib_arr[i] = trib_arr[i-1] + trib_arr[i-2] + trib_arr[i-3]
    print(trib_arr)
    return trib_arr[-1]

print(good_bit_strings(0))