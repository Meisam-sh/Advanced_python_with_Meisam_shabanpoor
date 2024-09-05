from datetime import datetime

def calculate_age(birth_date):
    try:
        today = datetime.today()
        print(f'today is {today}')
        birth_date = datetime.strptime(birth_date, "%Y/%m/%d")
        print(birth_date)
        if birth_date > today:
            print("WRONG")
            return
        
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(age)

    except ValueError:
        print("WRONG")

# ورودی از کاربر دریافت می‌شود
input_date = input()

# تابع calculate_age را صدا می‌زنیم
calculate_age(input_date)