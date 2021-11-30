# Stable Sort

# Let's arrange a deck of cards. There are totally 36 cards of 4 suits(S, H, C, D)
# and 9 values (1, 2, ... 9). For example, 'eight of heart' is represented by H8 and 'one of diamonds' is represented by D1.
# Your task is to write a program which sorts a given set of cards in ascending
# order by their values using the Bubble Sort algorithms and the Selection Sort algorithm respectively.
# These algorithms should be based on the following pseudocode:
"""
BubbleSort(C)
1 for i = 0 to C.length-1
2     for j = C.length-1 downto i+1
3         if C[j].value < C[j-1].value
4             swap C[j] and C[j-1]
"""
"""
SelectionSort(C)
1 for i = 0 to C.length-1
2     mini = i
3     for j = i to C.length-1
4         if C[j].value < C[mini].value
5             mini = j
6     swap C[i] and C[mini]
"""
# For each algorithm, report the stability of the output for the given input (instance).
# Here, 'stability of the output' means that: cards with the same value
# appear in the output in the same order as they do in the input (instance).


def bubble_sort(n, arr):
    stability = "Stable"
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j][1] < arr[j - 1][1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr, stability


def selection_sort(n, arr):
    stability = "Stable"
    for i in range(n):
        mini = i
        for j in range(i, n):
            if arr[j][1] == arr[mini][1]:
                tmp = j
            if arr[j][1] < arr[mini][1]:
                mini = j

        arr[i], arr[mini] = arr[mini], arr[i]
        if mini >= tmp and i != mini:
            stability = "Not stable"
    return arr, stability


def stable_sort():

    n = int(input())
    arr = list(input().split())

    bubble, bubble_stability = bubble_sort(n, arr)
    selection, selection_stability = selection_sort(n, arr)

    print(*bubble)
    print(bubble_stability)
    print(*selection)
    print(selection_stability)
    return


if __name__ == "__main__":
    stable_sort()
    # selection_sort()
    # bubble_sort()
