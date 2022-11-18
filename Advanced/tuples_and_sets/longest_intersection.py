n = int(input())

length = 0
longest = None
for i in range(n):

    numbers = input().split('-')
    first_two, second_two = numbers
    first, second = first_two.split(',')
    third, fourth = second_two.split(',')

    inter_1 = {el for el in range(int(first), int(second)+1)}
    inter_2 = {el for el in range(int(third), int(fourth)+1)}

    intersection = inter_1 & inter_2
    if len(intersection) > length:
        length = len(intersection)
        longest = intersection

print(f"Longest intersection is {list(longest)} with length {length}")
