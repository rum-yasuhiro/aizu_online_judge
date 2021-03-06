def insertion_sort():
    # load input
    # loop while elements in list are checked from second to last that if each of them are bigger than all forward elements
    # if so, swap the order

    len = int(input())
    num_list = list(map(int, input().split()))

    output = num_list
    print(" ".join(map(str, output)))
    for i in range(1, len):
        key = output[i]

        j = i - 1
        while j >= 0 and output[j] > key:
            output[j + 1] = output[j]
            j -= 1
        output[j + 1] = key
        print(" ".join(map(str, output)))


if __name__ == "__main__":

    insertion_sort()
