def recursiveSum(n : int) -> int:
    if n == 0:
        return 0

    else:
        return n + recursiveSum(n-1)


if __name__ == '__main__':
    print(recursiveSum(1))
    print(recursiveSum(3))
    print(recursiveSum(5))
