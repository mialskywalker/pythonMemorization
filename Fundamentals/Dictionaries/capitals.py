country = input().split(', ')
capital = input().split(', ')

d = zip(country, capital)

d = dict(d)

for key, value in d.items():
    print(f"{key} -> {value}")
