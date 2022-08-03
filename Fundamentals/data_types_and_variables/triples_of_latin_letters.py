n = int(input())

for i in range(n):
    for u in range(n):
        for e in range(n):
            print(f"{chr(97 + i)}{chr(97 + u)}{chr(97 + e)}")
