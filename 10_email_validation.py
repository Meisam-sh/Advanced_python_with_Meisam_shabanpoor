import re

def validate_email(email):
    pattern = r'^\w+@[a-zA-Z]+\.[a-zA-Z]+$'

    if re.match(pattern, email):
        return 'OK'
    else:
        return 'WRONG'

# ورودی را دریافت می‌کنیم
user_email = input()

# اعتبارسنجی ایمیل
result = validate_email(user_email)

# نمایش خروجی
print(result)