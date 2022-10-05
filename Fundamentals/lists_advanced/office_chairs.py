rooms = int(input())
free = 0
result = 0
game_on = True

for room in range(1, rooms + 1):

    chairs, people = input().split()
    result = len(chairs) - int(people)
    if result < 0:
        print(f"{abs(result)} more chairs needed in room {room}")
        game_on = False
    else:
        free += result

if game_on:
    print(f"Game On, {free} free chairs left")
