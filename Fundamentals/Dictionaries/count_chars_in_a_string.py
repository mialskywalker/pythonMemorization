text = input().split()

counter = {}

for el in text:

    for i in el:

        if i not in counter.keys():
            counter[i] = 1
        else:
            counter[i] += 1

for key, value in counter.items():
    print(f"{key} -> {value}")

