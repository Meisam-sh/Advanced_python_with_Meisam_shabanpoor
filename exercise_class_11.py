import random

class Human:
    def __init__(self, name):
        self.name = name

class Footballer(Human):
    def __init__(self, name):
        super().__init__(name)
    
# ایجاد یک لیست از نام‌های بازیکنان
players = ["حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار", "میلاد",
           "مصطفی", "امین", "سعید", "پویا", "پوریا", "رضا", "علی", "بهزاد", "سهیل",
           "بهروز", "شهروز", "سامان", "محسن"]

# ایجاد ۲۲ شی فوتبالیست و اختصاص دادن نام به هر شی
footballers = [Footballer(name) for name in players]

# تقسیم بازیکنان بین دو تیم به صورت رندم
team_A = random.sample(footballers, 11)
team_B = [player for player in footballers if player not in team_A]

# چاپ کردن نام هر بازیکن با نام تیم مربوطه‌شان
for player_A in team_A:
    print(f"{player_A.name} - Team A")

for player_B in team_B:
    print(f"{player_B.name} - Team B")