#include <iostream>
#include <cmath>

bool isPrimeNaive(int n)
{
    if (n <= 1)
    {
        return false;
    }

    //check from 2 to square root of n
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int l;
    std::cin >> l;

    int arr[l];

    int counter = 0;
    for (int i = 0; i < l; ++i)
    {
        std::cin >> arr[i];
        if (isPrimeNaive(arr[i]))
        {
            counter += 1;
        }
    }
    std::cout << counter << std::endl;
}
