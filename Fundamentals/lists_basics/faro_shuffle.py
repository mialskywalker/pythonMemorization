deck = input().split()
shuffle_times = int(input())

first_deck = [deck[i] for i in range(len(deck)//2)]
second_deck = [deck[i] for i in range(len(deck)//2, len(deck))]
result = []

for _ in range(shuffle_times):

    result = []

    for i in range(0, len(deck)//2):

        result.append(first_deck[i])
        result.append(second_deck[i])

    first_deck = [result[i] for i in range(len(result)//2)]
    second_deck = [result[i] for i in range(len(result)//2, len(result))]

print(result)
