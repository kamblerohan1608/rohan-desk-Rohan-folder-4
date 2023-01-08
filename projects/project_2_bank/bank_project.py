
# Bank Application 

import os,random,re,time

class Main_app:
    def __init__(self):
        pass
        # try:
        #     os.mkdir("bank_data")
        # except:
        #     pass
        # os.chdir("bank_data")
    def check_bal(self,email):
        with open(f"{email}.txt","r") as file:
            data = file.readlines()
        data = data[-1]
        data = data.replace("\n",'')
        ptr = r': [0-9]*'
        findings = re.findall(ptr,data)
        findings_1 = findings[0]
        amount = findings_1[2:]
        amount = int(amount)
        print(f"\nThe Current Balance Of Account Is : {amount}\n")

    def deposite(self,email,depo_amount):
        with open(f"{email}.txt","r") as file:
            data = file.readlines()
        data = data[-1]
        data = data.replace("\n",'')
        ptr = r': [0-9]*'
        findings = re.findall(ptr,data)
        findings_1 = findings[0]
        amount = findings_1[2:]
        amount = int(amount)
        data = amount + depo_amount
        with open(f"{email}.txt","a") as file:
            print((f"\nThe Amount Deposited To Account : {depo_amount}\n"))
            file.write(f"The Amount deposited : {depo_amount}                {time.strftime('%d:%m:%y')}  {time.strftime('%I:%M:%S')}\n")
            file.write(f"Balance : {data}                           {time.strftime('%d:%m:%y')}  {time.strftime('%I:%M:%S')}\n")

    def withdrawal(self,email,withdraw_amount):
        with open(f"{email}.txt","r") as file:
            data = file.readlines()
        data = data[-1]
        data = data.replace("\n",'')
        ptr = r': [0-9]*'
        findings = re.findall(ptr,data)
        findings_1 = findings[0]
        current_amount = findings_1[2:]
        current_amount = int(current_amount)
        if withdraw_amount > current_amount:
            print("\n********* Insuficient Balance for withdrawal *********\n")
        else:
            data = current_amount - withdraw_amount
            with open(f"{email}.txt","a") as file:
                print((f"\nThe Amount Deducted from Account : {withdraw_amount}\n"))
                file.write(f"The Amount Withdraw : {withdraw_amount}                 {time.strftime('%d:%m:%y')}  {time.strftime('%I:%M:%S')}\n")
                file.write(f"Balance : {data}                           {time.strftime('%d:%m:%y')}  {time.strftime('%I:%M:%S')}\n")

    def Emi(self,principal,period):
        print(r"Rate of intrest will be 18% for personal loan.")
        rate = 18/12/100
        emi_amount = (principal*rate) * ((1+rate)**period)/(((1+rate)**period)-1)
        emi_amount = round(emi_amount,3)
        print(f"EMI Amount per Month Will Be {emi_amount}")
    
    def history(self,email):
        with open(f"{email}.txt","r") as file:
            data = file.read()
            ind = data.index("The account for")
            print(data[ind:])
            

class Create_Login_account(Main_app):
    def __init__(self):        
        try:
            os.mkdir("bank_data")
        except:
            pass
        os.chdir("bank_data")
        with open("varification.txt","a") as file:
            pass

        self.open_flag = False
        self.log_in_flag = False
        super().__init__()

    def open_account(self,f_name,l_name,age,contact,email,address,amount,password):

        # for Email existance varification

        all_files = os.listdir()
        #print(all_files)
        all_files_1 = ''.join(all_files)

        # Account number creation and varification of account number and contact number whther exists already 

        account_no = random.randint(10000000000,99999999999)
        with open("varification.txt","r") as file:
            data = file.read()
        if ('*' + contact ) in data:
            print("\n*********** Contact Already Exist....Try Another One ***********\n")
        elif (':'+ str(account_no)) in data :
            print("\n*********** Something Went Wrong ***********\n")
        elif email in all_files_1:
            print("\n*************** Email Already Exist....You Can Try Another One ****************\n")
        else:
            with open("varification.txt","a") as file:
                file.write(f"Customer Name : {f_name} {l_name}\n")
                file.write(f"Contact Number : *{contact}\n")
                file.write(f"Account Number : :{account_no}\n\n")

            with open(f"{email}.txt","a") as file:
                file.write(f"Name of customer is : {f_name} {l_name}\n")
                file.write(f"Age of customer is : {age}\n")
                file.write(f"Contact of customer is :{contact}\n")
                file.write(f"Address of customer is : {address}\n")
                file.write(f"Amount For First Deposite : {amount}\n")
                file.write(f"email of customer is : {email}\n")
                file.write(f"Password is : {password}\n")
                file.write(f"Account Number is : {account_no}\n\n")
                print(f"\nThe account for {f_name}{l_name} has been created with depositing amount of : {amount}")
                file.write(f"The account for {f_name}{l_name} has been created with depositing amount of : {amount}    {time.strftime('%d:%m:%y')}  {time.strftime('%I:%M:%S')}\n")
                self.open_flag = True
        return self.open_flag

    def log_in_account(self,email,password):
        all_files = os.listdir()
        #print(all_files)
        if f'{email}.txt' in all_files:
            with open(f"{email}.txt","r") as file:
                data = file.readlines()
                #print(data)
            data = data[6]
            # print(data)
            new_password = data[14:]
            # print(new_password)
            new_password = new_password.replace("\n",'')
            if new_password == password:
                self.log_in_flag = True
        return self.log_in_flag


if __name__=="__main__":

    app = Create_Login_account()
    def front():
        print("\n*************** Welcome To The OneBank Registration ****************\n")
        print("\nPress 1 : Create Account\nPress 2 : Login Account\nPress 3 : Exit Application\n")
    front()
    while True:        
        f_ch = input("Enter Your Choice : ")
        if f_ch == '1' :
            
            while True:
                f_name = input("Enter Your First Name : ")
                f_name = f_name.strip()
                str_ptr =re.findall( r'[a-zA-Z]' ,f_name)
                f_name_new = ''.join(str_ptr)
                if f_name == f_name_new:
                    f_name = (f_name.lower()).capitalize()
                    break
                else:
                    print("\n******************* Error...First Name should have Alphabets Only ************************\n")
                    print('********************************* Kindly Try Again **********************************\n')

            while True:
                l_name = input("Enter Your Last Name : ")
                l_name = l_name.strip()
                str_ptr =re.findall( r'[a-zA-Z]' ,l_name)
                l_name_new = ''.join(str_ptr)
                if l_name == l_name_new:
                    l_name = (l_name.lower()).capitalize()
                    break
                else:
                    print("\n******************* Error...Last Name should have Alphabets Only ************************\n")
                    print('********************************* Kindly Try Again **********************************\n')
            
            while True:        
                age = input("Enter Your Age : ")
                age = age.strip()
                if age.isdigit() == True:
                    break
                else:
                    print("\n*************************Error... Age Has To Be Number Only ************************\n")
                    print('********************************* Kindly Try Again **********************************\n')

            while True:
                contact = input("Enter Your Contact Number : ")
                contact = contact.strip()
                if len(contact) != 10:
                    print("\n******************* Contact Has To Be Of 10 Digits **********************\n")
                elif contact.isdigit() == True:
                    break
                else:
                    print("\n************************* Error... Contact Has To Be Number Only ************************\n")
                    print('********************************* Kindly Try Again **********************************\n')

            while True:

                address = input("Enter Your Address : ")
                address = address.strip()
                str_ptr =re.findall( r'[a-zA-Z]' ,address)
                address_new = ''.join(str_ptr)
                if address == address_new:
                    address = (address.lower()).capitalize()
                    break
                else:
                    print("\n******************* Error... Address should have Alphabets Only ************************\n")
                    print('********************************* Kindly Try Again **********************************\n')

            while True:

                amount = input("Enter Initial Amount Of Deposite : ")
                amount = amount.strip()
                if amount.isdigit() == True:
                    break
                else:
                    print("\n************************* Error... Amount Has To Be Number Only ************************\n")
                    print('********************************* Kindly Try Again **********************************\n')
            while True:

                email = input("Enter Your Email : ")
                email = email.strip()
                ptr = re.findall(r'\b[a-zA-Z0-9.*_*-*]+@+[a-zA-Z]+\.[a-zA-Z]{2,}',email)
                if email in ptr:
                    break
                else:
                    print("\n************************* Error... Invalid Email Entered ************************\n")
                    print('********************************* Kindly Try Again **********************************\n')

            while True:
                password = input("Enter Your Password : ")
                c_password = input("Confirm Password : ")
                password = password.strip()
                c_password = c_password.strip()
                if len(password) < 6:
                    print("\n******** Password Too Short has to be 6 characters Minimum ********\n")
                elif len(password) > 15 :
                    print("\n******** Password Too long maximum 15 characters allowed ********\n")
                elif password != c_password:
                    print("\n********* Passsword Does not Match**********\n")
                else:
                    break
            
            o_flag = app.open_account(f_name,l_name,age,contact,email,address,amount,password)
            if o_flag == False:
                print("******************** Can Not Create Account Currently *********************\n")
                front()
            else:
                print("\n**************************** You Can Log In Now ***************************\n")
                front()

        elif f_ch == '2' :
            email = input("Enter Your Email id : ")
            password = input("Enter Your Password : ")
            email = email.strip()
            password = password.strip()
            log_f = app.log_in_account(email,password)
            if log_f == False:
                print("\n*********** Incorrect Email Id Or Password...Try Again *************\n")
                front()
            else:
                def main():
                    print("\n******************** Welcome to The OneBank Application ****************\n")
                    print("Press 1 : Check Balance\nPress 2 : Deposite Balance\nPress 3 : Withdraw Amount\nPress 4 : Check Loan EMI\nPress 5 : See Payment History\nPress 6 : Log Out Account")
                main()
                while True:
                    print()
                    m_ch = input("Enter Your choice : ")
                    if m_ch == '1':
                        app.check_bal(email)
                        main()
                    elif m_ch == '2':
                        depo_amount = input("Enter The Amount To Be Deposited : ")
                        if depo_amount.isdigit() != True:
                            print("\n****************** Error... Depositing Amount Must Be Digit Only ******************\n")
                        else:
                            depo_amount = int(depo_amount)
                            app.deposite(email,depo_amount)
                        main()
                    elif m_ch == '3':
                        withdraw_amount = input("Enter The Amount To Withdraw : ")
                        if withdraw_amount.isdigit() == False:
                            print("\n****************** Error... Withdraw Amount Must Be Digit Only ******************\n")    
                        else:
                            withdraw_amount = int(withdraw_amount)
                            app.withdrawal(email,withdraw_amount)
                        main()
                    elif m_ch == '4':
                        principal = input("Enter The Amount of loan : ")
                        if principal.isdigit() == False :
                            print("\n****************** Error...Amount must be digit only ******************\n")
                            main()
                        else:
                            principal = int(principal)
                            period = input("Enter The Number of Months : ")
                            if period.isdigit() == False:
                                print("\n****************** Error...Period must be in digit only ******************\n")
                                main()
                            else:
                                period = int(period)
                                app.Emi(principal,period)
                                main()
                    elif m_ch == '5':
                        print("\n*********** All Transactions From Your Account *************\n")
                        app.history(email)
                        main()
                    elif m_ch == '6':
                        print("\n************************ logged out of account ************************\n")
                        front()
                        break
                    else:
                        print("\n********************** Invalid Choice ************************\n")
                        main()
        elif f_ch == '3':
            print("\n*********** Thank You For Using OneBank Application *****************\n")
            break
        else:
            print("\n************* Invalid Option ****************\n")