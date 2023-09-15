def peaks(x):
    # x: list of floats (or ints)
    # returns: list of indexes of peaks
    ans = []
    for i in range(1 ,len(x)-1):
        if x[i-1] < x[i] > x[i+1]:
            ans.append(i)
    return ans

exec(input()) # DON'T remove this line