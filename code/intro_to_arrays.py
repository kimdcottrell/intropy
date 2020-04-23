import array

print("What's your favorite 3 foods?")
prompt = '> '

a = []
for i in range(0, 3):
    a.append(input(prompt))

print(f"Here's your favorite foods: {', '.join(a[:])}")
