import mysql.connector  
import re  

def is_valid_email(email):  
    # الگوی regex برای بررسی فرمت ایمیل  
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  
    return re.match(regex, email) is not None  

def is_valid_password(password):  
    # بررسی اینکه رمز عبور شامل حداقل یک عدد و یک حرف باشد  
    return any(char.isdigit() for char in password) and any(char.isalpha() for char in password)  

def save_to_database(username, password):  
    # اتصال به پایگاه داده MySQL  
    connection = mysql.connector.connect(  
        host='localhost',  
        user='root',        # نام کاربری MySQL خود را وارد کنید  
        password='14001003Sofia_', # رمز عبور خود را وارد کنید  
        database='mydatabase'  
    )  
    cursor = connection.cursor()  
    
    # ذخیره‌سازی اطلاعات در جدول  
    sql = "INSERT INTO user_info (username, password) VALUES (%s, %s)"  
    cursor.execute(sql, (username, password))  
    connection.commit()  

    cursor.close()  
    connection.close()  

def main():  
    while True:  
        email = input()  
        if is_valid_email(email):  
            break  
        else:  
            print("ایمیل وارد شده نادرست است. لطفاً یک ایمیل صحیح وارد کنید. مثال: example@domain.com")  
    
    while True:  
        password = input()  
        if is_valid_password(password):  
            break  
        else:  
            print("رمز عبور باید شامل حداقل یک عدد و یک حرف باشد. لطفاً دوباره تلاش کنید.")  
    
    save_to_database(email, password)  
    print("اطلاعات با موفقیت ذخیره شد.")  

if __name__ == "__main__":  
    main()