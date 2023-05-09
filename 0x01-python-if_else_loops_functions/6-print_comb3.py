#!/usr/bin/python3
for num_1 in range(0, 10):
    for num_2 in range(num_1 + 1, 10):
        if num_1 == 8 and num_2 == 9:
            print(f"{num_1}{num_2}")
        else:
            print(f"{num_1}{num_2}", end=", ")
