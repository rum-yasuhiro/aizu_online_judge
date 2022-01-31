"""
Doubly Linked List
Your task is to implement a double linked list.

Write a program which performs the following operations:

insert x: insert an element with key x into the front of the list.
delete x: delete the first element which has the key of x from the list. If there is not such element, you need not do anything.
deleteFirst: delete the first element from the list.
deleteLast: delete the last element from the list.
"""

from collections import deque


def doubly_linked_list():
    n = int(input())
    l = deque()
    for _ in range(n):
        command = input()

        if command == "deleteFirst":
            l.popleft()
        elif command == "deleteLast":
            l.pop()
        else:
            command, num = command.split()
            if command == "delete" and num in l:
                # try:
                #     l.remove(num)
                # except:
                #     pass
                l.remove(num)
            elif command == "insert":
                l.appendleft(num)
    print(*l)
    return


if __name__ == "__main__":
    doubly_linked_list()
