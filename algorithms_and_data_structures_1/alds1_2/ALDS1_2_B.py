# Selection Sort
# Write a program of the Selection Sort algorithm which sorts
# a sequence A in ascending order.
# The algorithm should be based on the following pseudocode:
"""
SelectionSort(A)
1 for i = 0 to A.length-1
2     mini = i
3     for j = i to A.length-1
4         if A[j] < A[mini]
5             mini = j
6     swap A[i] and A[mini]
"""
# Note that, indices for array elements are based on 0-origin.
# Your program should also print the number of swap operations
# defined in line 6 of the pseudocode in the case where i ≠ mini.


def selection_sort():
    n = int(input())
    arr = list(input().split())

    cnt = 0
    for i in range(n):
        mini = i
        for j in range(i, n):
            if arr[j] < arr[mini]:
                mini = j

        arr[i], arr[mini] = arr[mini], arr[i]
        if i != mini:
            cnt += 1

    print(*arr)
    print(cnt)
    return


if __name__ == "__main__":
    selection_sort()
