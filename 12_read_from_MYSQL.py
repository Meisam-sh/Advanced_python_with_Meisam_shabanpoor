import mysql.connector  
from mysql.connector import Error  

def connect_to_db(db_name):  
    try:  
        mydb = mysql.connector.connect(  
            host="localhost",  
            user="sa",  
            password="14001003Sofia_",  
            database=db_name,  
            auth_plugin='caching_sha2_password'  
        )  

        if mydb.is_connected():  
            #print("You are connected")  
            cursor = mydb.cursor()  
            return cursor, mydb  
        else:  
           # print("You are still not connected")  
            return None, None  
    except Error as e:  
        print(f"Error: {e}")  
        return None, None  

mydb = 'employment'  
cursor, mydb_connection = connect_to_db(mydb)  

if cursor:  
    cursor.execute('SELECT COUNT(*) AS number FROM info')  
    count = cursor.fetchall()  
    cursor.execute('SELECT name,height,weight FROM info order by height desc,weight') 
    selection=cursor.fetchall()
    for item in range(len(selection)):
        print(selection[item][0],' ',selection[item][1],' ',selection[item][2])

    cursor.close()  
else:  
    print('You are not connected')  

if mydb_connection:  
    mydb_connection.close()