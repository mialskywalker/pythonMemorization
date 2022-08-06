text = input().split()

team_a = [i for i in range(1, 12)]
team_b = team_a.copy()
terminated = False

for el in text:

    command = el.split('-')

    team = command[0]
    player = int(command[1])

    if team == 'A':
        if player not in team_a:
            continue
        team_a.remove(player)
    elif team == 'B':
        if player not in team_b:
            continue
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if terminated:
    print("Game was terminated")
