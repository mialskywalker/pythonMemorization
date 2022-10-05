text = input().split(', ')
text = list(map(int, text))

positive = [el for el in text if el >= 0]
negative = [el for el in text if el < 0]
even = [el for el in text if el % 2 == 0]
odd = [el for el in text if el % 2 != 0]

print(f"Positive: {', '.join(list(map(str, positive)))}\n"
      f"Negative: {', '.join(list(map(str, negative)))}\n"
      f"Even: {', '.join(list(map(str, even)))}\n"
      f"Odd: {', '.join(list(map(str, odd)))}\n")
