n = int(input())
participants = []

for _ in range(n):
    gender, name, language = input().split('.')
    participants.append((gender, name.capitalize(), language))

participants.sort(key=lambda x: (x[0], x[1]))  # Sort by gender, then by name

for gender_group in ['f', 'm']:
    for participant in participants:
        if participant[0] == gender_group:
            print(f"{participant[0]} {participant[1]} {participant[2]}")