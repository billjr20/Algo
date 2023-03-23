def good_bit_strings(n):
    
    # there exists no possible bit strings
    if n < 1:
        return 0
    
    # base case 1
    elif n == 1:
        return 2
    
    # base case 2
    elif n == 2:
        return 4
    
    # base case 3
    elif n == 3:
        return 7
    
    # allocate and seed constant size tribonacci array
    trib_arr = [0] * (3)
    # base cases / seed values supplied by problem description
    trib_arr[0], trib_arr[1], trib_arr[2] = 2, 4, 7

    # do O(n) tribonacci compuations and store them in the trib_arr
    for i in range(3, n):
        # computation of f(i) = f(i-1) + f(i-2) + f(i-3)
        temp = trib_arr[2] + trib_arr[1] + trib_arr[0]
        trib_arr[0] = trib_arr[1]
        trib_arr[1] = trib_arr[2]
        trib_arr[2] = temp
    
    # return the last value in the tribonacci arracy
    return trib_arr[-1]

for i in range(1, 20):
    print(f'Bit length {i}, good strings = {good_bit_strings(i)}')
