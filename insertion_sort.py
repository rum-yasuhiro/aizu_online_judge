def insertion_sort(len, num_list):
    # load input
    # loop while elements in list are checked from second to last that if each of them are bigger than all forward elements
    # if so, swap the order

    output = num_list.copy()
    for i in range(1, len):
        key = output[i]

        j = i - 1
        while j >= 0 and output[j] > key:
            output[j + 1] = output[j]
            j -= 1
        output[j + 1] = key
        print(output)
    # return output


if __name__ == "__main__":
    len = int(input())
    num_list = map(int, input().split())

    insertion_sort(len, num_list)
