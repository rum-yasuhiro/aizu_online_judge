"""
Reverse Polish notation is a notation where every operator follows all of its operands. 
For example, an expression (1+2)*(5+4) in the conventional Polish notation can be represented as 1 2 + 5 4 + * in the Reverse Polish notation. 
One of advantages of the Reverse Polish notation is that it is parenthesis-free.

Write a program which reads an expression in the Reverse Polish notation and prints the computational result.

An expression in the Reverse Polish notation is calculated using a stack. 
To evaluate the expression, the program should read symbols in order. 
If the symbol is an operand, the corresponding value should be pushed into the stack. 
On the other hand, if the symbols is an operator, the program should pop two elements from the stack, perform the corresponding operations, then push the result in to the stack. 
The program should repeat this operations.
"""


def solve():
    l = input().split()

    stack = []
    for op in l:
        if op in ["+", "-", "*"]:
            b = int(stack.pop())
            a = int(stack.pop())
            if op == "+":
                c = a + b
            elif op == "-":
                c = a - b
            else:
                c = a * b
            stack.append(c)
        else:
            stack.append(op)
    ans = stack[-1]
    print(ans)
    return


if __name__ == "__main__":
    solve()
