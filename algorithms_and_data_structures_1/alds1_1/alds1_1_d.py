def max_profit():
    n = int(input())
    min = 10 ** 9
    l = []
    min_indexes = []
    output = -1

    for i in range(n):
        rt = int(input())
        if rt < min:
            min_indexes.append(i)

        l.append(rt)

    max_profit = 0
    for t in min_indexes:
        profit = max(l[i:]) - l[t]
        if profit > max_profit:
            max_profit = profit
            output = t + 1

    return output


if __name__ == "__main__":
    print(max_profit())
