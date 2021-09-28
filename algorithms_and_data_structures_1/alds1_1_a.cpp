#include <stdio.h>
#include <iostream>

int main()
{
    // input
    int l;
    std::cin >> l;

    int arr[l];
    for (int i = 0; i < l; ++i)
    {
        std::cin >> arr[i];
    }

    // insertion sort
    for (int i = 0; i < l; ++i)
    {
        // swap
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
        // show the list status
        for (int i = 0; i < l - 1; i++)
        {
            std::cout << arr[i] << ' ';
        }
        std::cout << arr[l - 1] << '\n';
    }
}