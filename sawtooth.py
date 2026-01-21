def convert(s, numRows):
    if numRows == 1:
        return s

    # current row index
    i = 0

    # direcetion of movement, down = 1 up = -1
    d = 1

    # sets all rows to list of lists
    rows = [[] for _ in range(numRows)]

    for c in s:
        rows[i].append(c)
        if i == 0:
            d = 1
        elif i == numRows - 1:
            d = -1
        i += d
    
    # res string on diag 
    res = ''
    
    for i in range(numRows):
        res += ''.join(rows[i])
    
    return res
    

