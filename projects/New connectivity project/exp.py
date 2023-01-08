
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
        query5 = '''alter table staff_info modify emp_id int auto_increment;'''
        cur.execute(query5)
        cur.execute("commit;")
        mydb.close()
        print("Auto increment added...")

    def register(self,f_name,l_name,age,contact,email_id,password):

        mydb = db.connect(host = "localhost",user = "root",password = "c0d3r123",database = "movie_application")
        cur = mydb.cursor()
        query = '''select * from staff_info;'''
        cur.execute(query)
        data = cur.fetchall()
        # print(data)
        e_mail_collection = []
        mobile_no_collection = []
        for i in range (len(data)):
            e_mail_collection.append(data[i][-2])
            mobile_no_collection.append(data[i][-3])
        # print(e_mail_collection)
        # print(mobile_no_collection)
        # print(len(data))
        if len(data) == 1:
            id = 101
            query = f'''insert into staff_info(emp_id,emp_f_name,emp_l_name,emp_age,emp_contact,emp_email,emp_password)values({id},"{f_name}","{l_name}",{age},{contact},"{email_id}","{password}")'''
            cur.execute(query)
            cur.execute("commit;")
        elif email_id in e_mail_collection:
            print("\n************************** Email Already Exist... Try Other One ************************\n")
        elif int(contact) in mobile_no_collection:
            print("\n************************* Contact Number Already Exist... Try Other One ************************\n")
        elif len(data) > 1 and (email_id not in e_mail_collection and contact not in mobile_no_collection):
            query = f'''insert into staff_info(emp_f_name,emp_l_name,emp_age,emp_contact,emp_email,emp_password)values("{f_name}","{l_name}",{age},{contact},"{email_id}","{password}")'''
            cur.execute(query)
            cur.execute("commit;")
            print("New staff added")
        else:
            print("Email Already Exists")
        mydb.close()
        
    def view_staff(self):
        mydb = db.connect(host = 'localhost',user = "root", password = "c0d3r123", database = "movie_application")
        cur = mydb.cursor()
        query = '''select * from staff_info where emp_id > 100 '''
        cur.execute(query)
        data = cur.fetchall()
        mydb.close()
        print(data)
        if data : 
            for ind in range (len(data)):
                print(f"\nEmployee Id : {data[ind][0]}")
                print(f"Employee Name : {data[ind][1]} {data[ind][2]}")
                print(f"Employee Age : {data[ind][3]}")
                print(f"Employee Contact Number : {data[ind][4]}")
                print(f"Employee Email ID : {data[ind][5]}\n")
        else:
            print("***************************** No Staff Member Assigned Yet ************************")

    def remove_staff(self,e_id):
        mydb = db.connect(host = 'localhost',user = "root", password = "c0d3r123", database = "movie_application")
        cur = mydb.cursor()
        query = '''select * from staff_info where emp_id > 100 '''
        cur.execute(query)
        data = cur.fetchall()
        print(data)
        ids = []
        for ind in range(len(data)):
            ids.append(data[ind][0])
        print(ids)
        if e_id in ids :
            query1 = f'''delete from staff_info where emp_id = {e_id};'''
            cur.execute(query1)
            cur.execute("commit;")
        else:
            print("\n*************************** Employee Id Does Not Exist ***************************\n")
        mydb.close()

    
    def log_in(self,email_id,password):
        mydb = db.connect(host = 'localhost',user = "root", password = "c0d3r123", database = "movie_application")
        cur = mydb.cursor()
        query = f'''select * from staff_info where emp_email = "{email_id}" and emp_password = "{password}" '''
        cur.execute(query)
        data = cur.fetchall()
        print(data)
        if data:
            self.log_in_flag = True
        return self.log_in_flag


obj = A()
# obj.register("lila","kedar","35","1548796532","lila@gmail.com","123456")
# obj.view_staff()
# obj.remove_staff(100)
obj.log_in("kedar@gmail.com","123456")