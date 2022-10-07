items = {}

shadowmourne = False
valanyr = False
dragonwrath = False


while True:

    line = input().split()

    for i in range(0, len(line), 2):

        number = int(line[i])
        material = line[i+1].lower()

        if material not in items.keys():
            items[material] = number
            if number >= 250:
                if material == 'shards':
                    shadowmourne = True
                    items[material] -= 250
                    break
                elif material == 'fragments':
                    valanyr = True
                    items[material] -= 250
                    break
                elif material == 'motes':
                    dragonwrath = True
                    items[material] -= 250
                    break
        else:
            items[material] += number
            if items[material] >= 250:
                if material == 'shards':
                    shadowmourne = True
                    items[material] -= 250
                    break
                elif material == 'fragments':
                    valanyr = True
                    items[material] -= 250
                    break
                elif material == 'motes':
                    dragonwrath = True
                    items[material] -= 250
                    break

    if shadowmourne or valanyr or dragonwrath:
        break

if shadowmourne:
    print("Shadowmourne obtained!")
elif valanyr:
    print("Valanyr obtained!")
elif dragonwrath:
    print("Dragonwrath obtained!")

if 'shards' in items.keys():
    print(f"shards: {items['shards']}")
    items.pop('shards')
else:
    print(f"shards: 0")
if 'fragments' in items.keys():
    print(f"fragments: {items['fragments']}")
    items.pop('fragments')
else:
    print(f"fragments: 0")
if 'motes' in items.keys():
    print(f"motes: {items['motes']}")
    items.pop('motes')
else:
    print(f"motes: 0")

for k, v in items.items():
    print(f"{k}: {v}")
