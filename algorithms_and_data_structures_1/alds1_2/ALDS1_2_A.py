# Bubble Sort
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_A
# Write a program of the Bubble Sort algorithm which sorts a sequence A in ascending order. The algorithm should be based on the following pseudocode:
"""
BubbleSort(A)
1 for i = 0 to A.length-1
2     for j = A.length-1 downto i+1
3         if A[j] < A[j-1]
4             swap A[j] and A[j-1]
"""
# Note that, indices for array elements are based on 0-origin.
# Your program should also print the number of swap operations defined in line 4 of the pseudocode.


def bubble_sort():
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0  # counter for number of swap operation performed
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                cnt += 1

    print(*arr)  # * is unpack of list
    print(cnt)
    return


if __name__ == "__main__":
    bubble_sort()
