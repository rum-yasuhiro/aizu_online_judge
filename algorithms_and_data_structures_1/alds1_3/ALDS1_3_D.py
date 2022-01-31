from logging.handlers import WatchedFileHandler
import pstats
import sys
from collections import deque
import re
import copy


def main():
    lands = input()

    ends_up = False
    while not ends_up:
        if lands[-1] == "/":
            ends_up = True
        else:
            print(lands)
            lands = lands.rstrip("_")
            lands = lands.rstrip("\\")

    print(lands)

    depth = 0
    sub_area = 0
    sub_areas = deque()
    for l in lands:
        if l == "_":
            section = depth
            sub_area += section
        elif l == "/":
            if depth > 0:
                section = depth - 0.5
                sub_area += section
                depth -= 1
                if depth == 0 and sub_area:
                    print("########", sub_area, "########")
                    sub_areas.append(str(int(copy.copy(sub_area))))
                    sub_area = 0
                    depth = 0
        else:
            depth += 1
            section = depth - 0.5
            sub_area += section
        print(sub_area, depth)

    print(len(sub_areas), " ".join(sub_areas))

    return


if __name__ == "__main__":
    main()
