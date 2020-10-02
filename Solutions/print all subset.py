a = [1, 2, 3, 4]


def subset(a, n):
    if n == 1:
        return n
    else:
        return (subset(a[n - 1]), subset(a[n - 2]))


print(subset(a, n=4))
