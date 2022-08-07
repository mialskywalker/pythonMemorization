initial_energy = 100
initial_coins = 100

text = input().split('|')

current_energy = initial_energy
current_coins = initial_coins
opened = True

for el in text:

    command, value = el.split('-')
    value = int(value)

    if command == 'rest':

        if current_energy + value >= 100:
            print(f"You gained {100 - current_energy} energy.")
            current_energy = 100
        else:
            current_energy += value
            print(f"You gained {value} energy.")
        print(f"Current energy: {current_energy}.")

    elif command == 'order':

        if current_energy < 30:
            current_energy += 50
            print("You had to rest!")
        else:
            current_energy -= 30
            current_coins += value
            print(f"You earned {value} coins.")
    else:
        if current_coins < value:
            print(f"Closed! Cannot afford {command}.")
            opened = False
            break
        else:
            current_coins -= value
            print(f"You bought {command}.")

if opened:
    print(f"Day completed!\n"
          f"Coins: {current_coins}\n"
          f"Energy: {current_energy}")
