
import mysql.connector as db

class A:
    def __init__(self):
        mydb = db.connect(host = "localhost",user = "root",password = "c0d3r123")
        
        cur = mydb.cursor()
        query1 = '''create database if not exists movie_application'''
        cur.execute(query1)
        cur.execute("commit;")
        mydb.close()

        mydb = db.connect(host = "localhost",user = "root",password = "c0d3r123",database = "movie_application")
        cur = mydb.cursor()
        query2 = '''show tables;'''
        cur.execute(query2)
        # cur.execute("commit;")
        data = cur.fetchall()
        # print(data)
        if (not data) or ("staff_info" not in data[0]): 
            cur = mydb.cursor()
            query2 = '''create table staff_info(emp_id int unique,emp_f_name varchar(30),emp_l_name varchar(30),emp_age tinyint,emp_contact bigint,emp_email varchar(50),emp_password varchar(30));'''
            cur.execute(query2)
            cur.execute("commit;")
            query3 = '''insert into staff_info(emp_id,emp_f_name,emp_l_name,emp_age,emp_contact,emp_email,emp_password)values(Null,null,null,null,null,"rohan@gmail.com","123456")'''
            cur.execute(query3)
            cur.execute("commit;")
            print("Created")
        else:
            print("Already exist")
        query4 = '''select * from staff_info;'''
        cur.execute(query4)
        # cur.execute("commit;")
        data = cur.fetchall()
        # print(data)
        if data :
            pass
        else:
            query5 = '''insert into staff_info(emp_id,emp_f_name,emp_l_name,emp_age,emp_contact,emp_email,emp_password)values(Null,null,null,null,null,"rohan@gmail.com","123456")'''
            cur.execute(query5)
            cur.execute("commit;")
            print("File Was Created But Admin wasn't....Added Now")

        mydb.close()
        
obj = A()
