def s(n):

    sum = 0 
    for i in range(1, n+1):
        sum += i
        print(sum)
    return sum


if __name__ == "__main__":
    print(s(3))