#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    names_filtered = []

    for name in names:
        if not name.startswith('__'):
            names_filtered.append(name)

    names_filtered.sort()

    for name in names_filtered:
        print(name)
