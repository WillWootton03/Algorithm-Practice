def minOpertations(self, logs):
    res = 0

    for log in logs:
        # remain in current folder
        if log == './':
            continue
        elif log == '../':
            # If res is already 0 it stays 0 else go back a folder
            res = max(0, res - 1)
        else:
            res += 1
    return res

