
# log_in and sign_in feature :

import os,random

class Admin:
    def __init__(self):
        self.update_info_flag = False
        self.del_flag = False
        self.del_vol_flag = False
    def del_info(self,ad_del):
        with open(r"User_data\survey_data.txt","r") as file:
            data = file.readlines()
            for user in data:
                if ad_del in user :
                    ind = data.index(user)
        name = data[ind+1]
        name_1 = name[10:]
        name_1 = name_1.capitalize()
        for position in range(0,8):
            data.pop(ind)
        data = ''.join(data)
        print(f"\n  Deleting The Information Of {name_1}\n")
        with open(r"User_data\survey_data.txt","w") as file:
            file.write(data)
            self.del_flag = True
        return self.del_flag

    def update_info(self,ad_update,name,age,gender,location,contact_no,family_mem):
        with open(r"User_data\survey_data.txt","r") as file:
            data = file.readlines()
            for user in data:
                if ad_update in user :
                    ind = data.index(user)
        # print(data)
        l_1 = data[ind]
        for position in range(0,8):
            data.pop(ind)
        data = ''.join(data)
        with open(r"User_data\survey_data.txt","w") as file:
            file.write(data)
            file.write(l_1)
            file.write(f"Name is : {name}\n")
            file.write(f"age is : {age}\n")
            file.write(f"Gender is : {gender}\n")
            file.write(f"Location is : {location}\n")
            file.write(f"Contact Number is : {contact_no}\n")
            file.write(f"Family members : {family_mem}\n\n")
            self.update_info_flag = True
        return self.update_info_flag
    
    def del_volunteer(self,del_vol):
        with open(r"User_data\user_data.txt","r") as file:
            data = file.read()
        if del_vol not in data :
            print("\n************ Email Not Present As Volunteer *************\n")
        else:
            with open (r"User_data\user_data.txt","r") as file:
                data_new = file.readlines()
            for volunteer in data_new:
                if del_vol in volunteer:
                    ind = data_new.index(volunteer)
                    name = data_new[ind].split(',')
                    #print(name)
            print(f"\n************ Deteting the user {name[0]} {name[1]} From The Database *************\n")
            data_new.pop(ind)
            data_new_1 = ''.join(data_new)
            #print(data_new_1)
            with open (r"User_data\user_data.txt","w") as file:
                file.write(data_new_1)
                self.del_vol_flag = True
        return self.del_vol_flag

    def view_volunteer_info(self):
        with open(r"User_data\user_data.txt","r") as file:
            data = file.readlines()
        #print(data)
        new_data = [access.replace('\n','') for access in data]
        #print(new_data)
        new_data1 = [i.split(',') for i in new_data]
        #print(new_data1)
        print("\n**************** All Volunteer Information *****************")
        for i in new_data1:
            print(f"\nVolunteer Name : {i[0]} {i[1]}")
            print(f"Volunteer Age : {i[2]}")
            print(f"Volunteer Email id : {i[3]}\n")
            
class main_app:
    def __init__(self):
        self.add_flag = False

    def uni_code(self):
        otp_1 = random.randint(10000,99999)
        return otp_1

    def read_surve_data(self):
        with open(r"User_data\survey_data.txt","r") as file:
            data = file.read()
        return(data)

    def add_user_info(self,name,age,gender,location,contact_no,family_mem):
        name = name.strip()
        age = age.strip()
        gender = gender.strip()
        location = location.strip()
        contact_no = contact_no.strip()
        family_mem = family_mem.strip()
        
        unique_code = self.uni_code()
        unique_code = str(unique_code)
        unique_code = "00" + unique_code + "00"
        survey_data = self.read_surve_data()

        if (unique_code not in survey_data) and (contact_no not in survey_data):

            with open(r"User_data\survey_data.txt","a") as file :
                print(f"\nUser {name} added to the survey and the unique code is {unique_code}\n")
                file.write(f"User {name} added to the survey and the unique code is {unique_code}\n")
                file.write(f"Name is : {name}\n")
                file.write(f"age is : {age}\n")
                file.write(f"Gender is : {gender}\n")
                file.write(f"Location is : {location}\n")
                file.write(f"Contact Number is : {contact_no}\n")
                file.write(f"Family members : {family_mem}\n\n")
            self.add_flag = True
            return self.add_flag
        else:
            print("\nContact already existx/n")

    def search_user(self,unique_id):
        with open(r"User_data\survey_data.txt","r") as file:
            all_data = file.readlines()
            for check in all_data:
                if unique_id in check:
                    idx = all_data.index(check)
        search_data = all_data[idx:(idx + 6 )]
        search_data = ''.join(search_data)
        print("\n" + search_data)
                    
                    
class Registration_log_in(Admin,main_app):
    def __init__(self):
        try:
            os.mkdir("User_data")
        except FileExistsError:
            pass
        with open(r"User_data\user_data.txt","a") as file:
            pass
        self.registration_flag = False
        self.log_in_flag = False
        super().__init__()
        main_app.__init__(self)
    
    def registration(self,f_name,l_name,age,id,password):
        f_name = f_name.strip()
        l_name = l_name.strip()
        age = age.strip()
        id = id.strip()
        password = password.strip()
        with open(r"User_data\user_data.txt","r") as file:
            data = file.read()
        if id in data:
            return self.registration_flag
        else:
            with open(r"User_data\user_data.txt","a") as file:
                file.write(f"{f_name},{l_name},{age},{id},{password},\n")
                self.registration_flag = True
            return self.registration_flag 
        
    def log_in(self,id,password):
        id = id.strip()
        password = password.strip()
        with open(r"User_data\user_data.txt","r") as file:
            all_data = file.readlines()
        for user in all_data:
            user1 = user.split(',')
            if id == user1[3] and password == user1[4]:
                self.log_in_flag = True
        return self.log_in_flag

if __name__=="__main__":

    app = Registration_log_in()
    def front():
        print('''
        *****************************************************************************
        *                      Welcome to the Application 3                         *
        *****************************************************************************

         ----------------------------------------
        |   Volunteer Sign up   :    Press 1     |
         ----------------------------------------
         ----------------------------------------
        |    Volunteer log in   :    Press 2     |
         ----------------------------------------
         ----------------------------------------
        |        Admin log in   :    Press 3     |
         ----------------------------------------
         ----------------------------------------
        |            exit       :    Press 4     |
         ----------------------------------------
        ''')
    front()
    while True:
        
        ch = input("Enter the option : ")
        if ch == '1':
            f_name = input("Enter your first name : ")
            l_name = input("Enter your last name : ")
            age = input("Enter your age : ")
            id = input("Enter your email id : ")
            while True:
                password = input("Enter you password : ")
                c_password = input("Confirm you password : ")
                password = password.strip()
                c_password = c_password.strip()
                if len(password) < 6 :
                    print("\nPassword Too Short...should have atleast 6 characters\n")
                elif len(password) > 15:
                    print("\nPassword Too Large...Maximum 15 characters allowed\n")
                elif password != c_password:
                    print("\nPassword Does Not Match\n")
                else:
                    break


            if f_name == "":
                print("\nFirst Name is Empty\n")
            elif l_name == "":
                print("\nLast Name is Empty\n")
            elif age == "" :
                print("\nAge is Empty\n")
            elif id == "":
                print("\nEmail is Empty\n")
            elif password == "":
                print("\nPassword is Empty\n")
            else :
                r_flag = app.registration(f_name,l_name,age,id,password)
                if r_flag == False:
                    print("\n********** Email Already Exists *********\n")
                    front()
                else :
                    print("\n********* Registration Successful..!!! *********\n")
                    front()
        elif ch =='2':
            id = input("Enter the email : ")
            password = input("Enter the password : ")
            d = l_flag = app.log_in(id,password)
            if d == False:
                print("\n***** Information Did not match check email and password ******\n")
            else:
                def survey_fn():
                    print("\n************** Welcome To the Survey Application ***************\n")
                    print("\nPress 1 - Adding Information \nPress 2 - View Information \nPress 3 - Exit Survey Application\n")
                survey_fn()
                while True:
                    survey_ch = input("Enter your choice : ")
                    if survey_ch == '1':
                        name = input("Enter the Name : ")
                        age = input("Enter the age : ")
                        gender = input("Enter the gender : ")
                        location = input("Enter the Location : ")
                        contact_no = input("Enter the number : ")
                        family_mem = input("Enter the family mambers : ")
                        
                        add_flag = app.add_user_info(name,age,gender,location,contact_no,family_mem)
                        if add_flag == False:
                            print("\n********** Something Went Wrong *************\n")
                            survey_fn()
                        else :
                            print("\n************* Information Added Succesfully **************\n")
                            survey_fn()
                    elif survey_ch == '2':
                        while True:
                            check_ch = input("\nEnter your unique code : ")
                            check_ch = check_ch.strip()
                            if len(check_ch) < 9:
                                print("************* Unique code incorrect must be of 9 digits !!! *************")
                            elif len(check_ch) > 9:
                                print("************* Unique code incorrect must be of 9 digits !!! *************")
                            else:
                                app.search_user(check_ch)
                                survey_fn()
                                break
                    elif survey_ch == '3':
                        print("\n********** Thank You For Using Survey Application *************\n")
                        front()
                        break
                    else:
                        print("\n************ invalid choice **************\n")
                        front()
        elif ch== '3':
            admin_id = input("Enter the Admin Id : ")
            admin_pass = input("Enter the Admin password : ")
            if admin_id != "rohan@gmail.com" :
                print("\n**************** Wrong Admin Email Id or Password Entered ******************\n")
                front()
            elif admin_pass != "123456":
                print("\n**************** Wrong Admin Email Id or Password Entered ******************\n")
                front()
            elif admin_id == "rohan@gmail.com" and admin_pass == "123456":
                def admin():
                    print("\n************** Welcome Admin **************")
                    print("\nPress 1 - View Survey Information By Unique Code\nPress 2 - View All Survey Information \nPress 3 - Add Survey Information\nPress 4 - Update Survey Information\nPress 5 - Delete Survey Information\nPress 6 - View All Volunteer \nPress 7 - Delete Volunteer account\nPress 8 - Logout Admin Account\n")
                admin()
                while True :
                    ad_ch = input("Enter Your Choice : ")
                    if ad_ch == '1':
                        check_ch = input("\nEnter your unique code : ")
                        check_ch = check_ch.strip()
                        if len(check_ch) < 9:
                            print("************* Unique code incorrect must be of 9 digits !!! *************")
                        elif len(check_ch) > 9:
                            print("************* Unique code incorrect must be of 9 digits !!! *************")
                        else:
                            app.search_user(check_ch)
                            admin()
                                
                    elif ad_ch == '2':
                        print('\n'+ app.read_surve_data())
                        admin()
                    elif ad_ch == '3': # add survey info
                        name = input("Enter the Name : ")
                        age = input("Enter the age : ")
                        gender = input("Enter the gender : ")
                        location = input("Enter the Location : ")
                        contact_no = input("Enter the number : ")
                        family_mem = input("Enter the family mambers : ")
                        
                        add_flag = app.add_user_info(name,age,gender,location,contact_no,family_mem)
                        if add_flag == False:
                            print("\n********** Something Went Wrong *************\n")
                            admin()
                        else :
                            print("\n************* Information Added Succesfully **************\n")
                            admin()
                    elif ad_ch == '4':
                        while True:
                            ad_update = input("Enter The Unique Code To Update Information : ")
                            ad_update = ad_update.strip()
                            if len(ad_update) < 9:
                                print("************* Unique code incorrect must be of 9 digits !!! *************")
                            elif len(ad_update) > 9:
                                print("************* Unique code incorrect must be of 9 digits !!! *************")
                            else:
                                print("\n************** Updating User info ******************\n")
                                name = input("Enter the Name : ")
                                age = input("Enter the age : ")
                                gender = input("Enter the gender : ")
                                location = input("Enter the Location : ")
                                contact_no = input("Enter the number : ")
                                family_mem = input("Enter the family mambers : ")
                                update_flag = app.update_info(ad_update,name,age,gender,location,contact_no,family_mem)
                                if update_flag == False:
                                    print("\n******************Something Went Wrong**********************\n")
                                    admin()
                                    break
                                else:
                                    print("\n******************* Information Updated Succesfully *********************\n")
                                    admin()
                                    break
                    elif ad_ch == '5':
                        ad_del = input("Enter The Unique Code To Delete Information : ")
                        ad_del = ad_del.strip()
                        if len(ad_del) < 9:
                            print("************* Unique code incorrect must be of 9 digits !!! *************")
                        elif len(ad_del) > 9:
                            print("************* Unique code incorrect must be of 9 digits !!! *************")
                        else:
                            print("\n************** Deleting User info ******************\n")
                            delete_flag = app.del_info(ad_del)
                            if delete_flag == False:
                                print("\n****************** Something Went Wrong *******************\n")
                                admin()
                            else:
                                print("******************* Information Deleted Successfully ********************\n ")
                                admin()
                    elif ad_ch == '6': # view all volunteers
                        app.view_volunteer_info()
                        admin()
                    elif ad_ch == '7':
                        del_vol = input("Enter The Email Of The Volunteer : ")
                        del_vol = del_vol.strip()
                        delete_volunteer = app.del_volunteer(del_vol)
                        if delete_volunteer == False:
                            print("\n****************** Something Went Wrong *******************\n")
                            admin()
                        else:
                            print("\n************** Volunteer Deleted successfully*****************\n")
                            admin()
                    elif ad_ch == '8':
                        print("\n************* Logged Out Of Admin Account ***************\n")
                        front()
                        break
        elif ch == '4':
            print("\n********** Thank You For Using My Application **********\n")
            break
        else:
            print("\n**************Invalid input*************\n")
            front()





