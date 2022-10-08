n = int(input())
academy = {}


for _ in range(n):

    name = input()
    grade = float(input())

    if name not in academy.keys():
        academy[name] = [grade]
    else:
        academy[name].append(grade)

for k, v in academy.items():
    avg = sum(v) / len(v)
    if avg >= 4.50:
        print(f"{k} -> {avg:.2f}")
