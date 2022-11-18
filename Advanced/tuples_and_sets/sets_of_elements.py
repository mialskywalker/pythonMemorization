n, m = input().split()
n = int(n)
m = int(m)

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(int(input()))

for _ in range(m):
    m_set.add(int(input()))

unique = n_set & m_set

print('\n'.join(set(map(str, unique))))
