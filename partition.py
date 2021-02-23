def parttion(n, r, mn = 0, mx = None):
    """
    Implementation of mathematical partition of n into r parts where each part belongs to [mn, mx];
    mn and mx are optional. The default value of mn is 0 and the default value of mx is n;
    The output of this function is a list containing all the possible partitions in provided condition;
    """

    if mx == None: mx = n
    parts = []
    
    arr = [0 for i in range(r)]
    index = 0
    def part(n, r, mn, mx):
        nonlocal parts, arr, index

        if r==1:
            if n > mx:
                index = 0
                return
            arr[index] = n
            parts.append(arr[:])
        else:
            i = mn
            while r * i <= n:
                arr[index] = i
                index += 1
                part(n-i, r-1, i, mx)
                i += 1
        index -= 1

    part(n, r, mn, mx)
    return parts


if __name__ == '__main__':
    p = parttion(100, 2)
    for arr in p: print(arr)
    print(len(p))

