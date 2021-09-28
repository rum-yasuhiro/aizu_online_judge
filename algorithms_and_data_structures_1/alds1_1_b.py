def gcd(a, b):
    print("a: ", a, "b: ", b)
    if b > 0:
        gcd(b, a % b)
    else:
        print("ans", a)
        return a


if __name__ == "__main__":
    a, b = map(int, input().split())
    ans = gcd(a, b)
    print(ans)
