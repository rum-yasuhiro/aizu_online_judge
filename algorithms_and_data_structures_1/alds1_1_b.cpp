#include <iostream>

int gcd(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    else
    {
        return gcd(b, (a % b));
    }
}

int main()
{
    //input
    int a, b;
    std::cin >> a >> b;

    int ans;
    ans = gcd(a, b);

    std::cout << ans << '\n';
}