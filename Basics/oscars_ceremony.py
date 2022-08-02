hall_rent = int(input())

statues = hall_rent - (hall_rent * 0.3)
catering = statues - (statues * 0.15)
sound = catering / 2

total = hall_rent + statues + catering + sound

print(f"{total:.2f}")
