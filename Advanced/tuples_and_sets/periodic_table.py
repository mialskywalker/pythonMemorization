n = int(input())

chemical_compounds = set()

for _ in range(n):

    data = input().split()

    for el in data:
        chemical_compounds.add(el)

print('\n'.join(chemical_compounds))
