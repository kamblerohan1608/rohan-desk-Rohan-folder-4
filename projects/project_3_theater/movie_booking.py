
import os,re,random
from multipledispatch import dispatch

class Admin:
    def __init__(self):
        
        self.register_flag = False
        self.remove_staff_flag = False
        self.update_movie_flag = False
        self.update_time_flag = False
        self.update_price_flag = False
        self.add_new_food_flag = False
        self.delete_food_flag = False


    def view_staff(self):
        with open("staff_info.txt","a+") as file:
            file.seek(52)
            data = file.readlines()
        # print(data)
        if data : 
            for employee in data:
                emp = employee.split(',')
                print(f"\nEmployee Id : {emp[0]}")
                print(f"Employee Name : {emp[1]} {emp[2]}")
                print(f"Employee Age : {emp[3]}")
                print(f"Employee Contact Number : {emp[4]}")
                print(f"Employee Email ID : {emp[5]}\n")
        else:
            print("***************************** No Staff Member Assigned Yet ************************")

    def register(self,f_name,l_name,age,contact,email_id,password):
        with open("staff_info.txt","r")as file:
            data = file.readlines()
        # print(len(data))
        id = 100
        if len(data) == 1 :
            id = id + 1
        else:
            last_emp = data[-1]
            last_emp_id = re.findall(r'\b\d{3,5}\b,',''.join(last_emp))
            # print(last_emp_id)
            last_emp_id = [i.replace(',','') for i in last_emp_id]
            id = int(last_emp_id[0])
            id = id + 1
            # print(id)
        
        with open("staff_info.txt","a")as file:
            data = f"{id},{f_name},{l_name},{age},{contact},{email_id},{password},\n"
            file.write(data)
            self.register_flag = True
        return self.register_flag
    
    def remove_staff(self,emp_id):
        with open("staff_info.txt","r") as file:
            data = file.read()
        emp_list = re.findall(r'\b\d{3,5}\b',''.join(data))
        # print(emp_list)
        if str(emp_id) not in emp_list:
            print("\n************************ Employee ID Does Not Exist **********************\n")
        else:
            ind = emp_list.index(str(emp_id))
            with open("staff_info.txt","r") as file:
                data = file.readlines()
            data.pop(ind+1)
            data = ''.join(data)
            with open("staff_info.txt","w") as file:
                file.write(data)
                self.remove_staff_flag = True
            return self.remove_staff_flag

    
    @dispatch(int,str)
    def movie_update(self,movie_choice,new_movie_name):
        new_movie_name = f" {new_movie_name} "
        with open("theater_schedule.txt","r") as file:
            data = file.read()
            data = data.split(':')
            # print(data)
            # print(data[1],data[9],data[17])
        if movie_choice == 1:
            data.pop(1)
            # print(data)
            data.insert(1,new_movie_name)
            # print(data)
            data = ':'.join(data)
            # print(data)
        elif movie_choice == 2:
            data.pop(9)
            # print(data)
            data.insert(9,new_movie_name)
            # print(data)
            data = ':'.join(data)
            # print(data)
        elif movie_choice == 3:
            data.pop(17)
            # print(data)
            data.insert(17,new_movie_name)
            # print(data)
            data = ':'.join(data)
            # print(data)
        with open("theater_schedule.txt","w") as file:
            file.write(data)
            self.update_movie_flag = True
        return self.update_movie_flag
        
    @dispatch(str,str)
    def movie_update(self,movie_choice_and_slot_choice,new_movie_time):
        with open("theater_schedule.txt","r") as file:
            data1 = file.read()
            time_old = re.findall(r'\d{2}:\d{2} [a-zA-Z]{2}',data1)
            # print(time_old)
        with open("theater_schedule.txt","r") as file:    
            data = file.readlines()
            # print(data)
        merged_data = re.findall(r'\d',movie_choice_and_slot_choice) 
        # print(merged_data)
        movie_choice = merged_data[0]
        slot_choice = merged_data[1]
        # print(movie_choice)
        # print(slot_choice)
        # print(data)
        if movie_choice == '1':
            if slot_choice == '1':
                data_new = data[0]
                data_new1 =data_new.replace(time_old[0],new_movie_time)
                # print(data_new1)
                data.pop(0)
                data.insert(0,data_new1)
                # print(data)
                data = ''.join(data)
            elif slot_choice == '2':
                data_new = data[0]
                data_new1 = data_new.replace(time_old[1],new_movie_time)
                data.pop(0)
                data.insert(0,data_new1)
                # print(data)
                data = ''.join(data)
        elif movie_choice == '2':
            if slot_choice == '1':
                data_new = data[1]
                data_new1 =data_new.replace(time_old[2],new_movie_time)
                data.pop(1)
                data.insert(1,data_new1)
                # print(data)
                data = ''.join(data)
            elif slot_choice == '2':
                data_new = data[1]
                data_new1 = data_new.replace(time_old[3],new_movie_time)
                data.pop(1)
                data.insert(1,data_new1)
                # print(data)
                data = ''.join(data)
        elif movie_choice == '3':
            if slot_choice == '1':
                data_new = data[2]
                data_new1 =data_new.replace(time_old[4],new_movie_time)
                data.pop(2)
                data.insert(2,data_new1)
                # print(data)
                data = ''.join(data)
            elif slot_choice == '2':
                data_new = data[2]
                data_new1 = data_new.replace(time_old[5],new_movie_time)
                # print(data_new1)
                data.pop(2)
                data.insert(2,data_new1)
                # print(data)
                data = ''.join(data)
                # print(data)
        with open("theater_schedule.txt","w") as file:
            file.write(data)
            self.update_time_flag = True
        return self.update_time_flag



    @dispatch(str,int)
    def movie_update(self,movie_choice_and_slot_choice,new_movie_price):

        with open("theater_schedule.txt","r") as file:
            data = file.read()

        prices = re.findall(r'\*\d+',data)
        prices = ','.join(prices)
        prices = prices.replace('*','')
        prices = prices.split(',')
        # print(prices)
        merged_data = re.findall(r'\d',movie_choice_and_slot_choice) 
        # print(merged_data)
        movie_choice = merged_data[0]
        slot_choice = merged_data[1]
        data = data.split('*')
        # print(data)

        if movie_choice == '1':
            if slot_choice == '1':
                data_new = data[1]
                data_new1 =data_new.replace(prices[0],str(new_movie_price))
                data.pop(1)
                data.insert(1,data_new1)
                data = '*'.join(data)
                # print(data)
            elif slot_choice == '2':
                data_new = data[2]
                data_new1 = data_new.replace(prices[1],str(new_movie_price))
                data.pop(2)
                data.insert(2,data_new1)
                data = '*'.join(data)
                # print(data)
        elif movie_choice == '2':
            if slot_choice == '1':
                data_new = data[3]
                data_new1 =data_new.replace(prices[2],str(new_movie_price))
                data.pop(3)
                data.insert(3,data_new1)
                data = '*'.join(data)
                # print(data)
            elif slot_choice == '2':
                data_new = data[4]
                data_new1 = data_new.replace(prices[3],str(new_movie_price))
                # print(data_new1)
                data.pop(4)
                data.insert(4,data_new1)
                data = '*'.join(data)
                # print(data)
        elif movie_choice == '3':
            if slot_choice == '1':
                data_new = data[5]
                data_new1 =data_new.replace(prices[4],str(new_movie_price))
                data.pop(5)
                data.insert(5,data_new1)
                data = '*'.join(data)
                # print(data)
            elif slot_choice == '2':
                data_new = data[6]
                data_new1 = data_new.replace(prices[5],str(new_movie_price))
                # print(data_new1)
                data.pop(6)
                data.insert(6,data_new1)
                data = '*'.join(data)
                # print(data)
        with open("theater_schedule.txt","w") as file:
            file.write(data)
            self.update_price_flag = True
        return self.update_price_flag

    def add_new_food(self,update_food_ch,new_item,Price):
        with open("theater_schedule.txt","r") as file:
            data = file.read()
            data = data.split(':')
            # print(data)
        if update_food_ch == '1':
            data_new = data[-4]
            data_new = data_new + f", {new_item} {Price}"
            data.pop(-4)
            data.insert(-3,data_new)
            data = ':'.join(data)
            # print(data)

        elif update_food_ch == '2':
            data_new = data[-2]
            data_new = data_new + f", {new_item} {Price}"
            data.pop(-2)
            # print(data)
            data.insert(-1,data_new)
            # print(data)
            data = ':'.join(data)
            # print(data)
        with open("theater_schedule.txt","w") as file:
            file.write(data)
            self.add_new_food_flag = True

        return self.add_new_food_flag


    def delete_food(self,update_food_ch,item_sr_no):
        with open("theater_schedule.txt","r") as file:
            data = file.read()
            data = data.split(':')
            # print(data)
        if update_food_ch == '3':
            data_new = data[-4]
            data_new = data_new.split(',')
            # print(data_new)
            data_new.pop(int(item_sr_no) - 1)
            data.pop(-4)
            data_new = ','.join(data_new)
            data.insert(-3,data_new)
            data = ':'.join(data)
            # print(data)

        elif update_food_ch == '4':
            data_new = data[-2]
            data_new = data_new.split(',')
            # print(data_new)
            data_new.pop(int(item_sr_no) - 1)
            data.pop(-2)
            data_new = ','.join(data_new)
            # print(data_new)
            data.insert(-1,data_new)
            data = ':'.join(data)
            # print(data)
        with open("theater_schedule.txt","w") as file:
            file.write(data)
            self.delete_food_flag = True

        return self.delete_food_flag

class Movie_Application(Admin):
    def __init__(self):
        super().__init__()
        try:
            os.mkdir('all_files')
        except:
            pass
        os.chdir("all_files")
        with open("booking_info.txt","a")as file:
            pass
        with open("staff_info.txt","a+")as file:
            file.seek(0)
            data = file.read()
        if data:
            pass
        else:
            with open("staff_info.txt","a") as file:
                file.write("rohan,kamble,25,1234567890,rohan@gmail.com,123456,\n")

        with open("theater_schedule.txt","a+")as file:
            file.seek(0)
            data = file.read()
        if data:
            pass
        else:
            with open("theater_schedule.txt","a") as file:
                file.write("Screen 1 : K.G.F : [ ]:[ ] : Timings - 09:30 AM, 03:00 PM :*250,*250:\nScreen 2 : Dr.Strange Multiverse And Madness : [ ]:[ ] : Timings - 12:30 PM, 04:00 PM :*250,*250:\nScreen 3 : Uncharted : [ ]:[ ] : Timings - 02:00 PM, 08:00 PM :*250,*250:\n\n")
                file.write("Parking Slots :\nBike : [ ] : \nCar : [ ] : \n\n")
                file.write("Food Court : \n")
                file.write("Snacks : Pop Corn 50, Fries 100, KFC Hot Wings 250, Sandwich 60, Pizza 150, Burger 130:\n")
                file.write("Beverages : Appy 40, Coke 40, Fanta 40, Sprite 40, Thumbs up 40, Water 30:\n")
        
        self.seat_available_flag = False
        self.log_in_flag = False
        self.parking_availability_flag = True
        self.valid_ticket_no_flag = False
        self.parking_allowed_as_per_ticket_flag = False
        self.parking_flag = False


    def log_in(self,email_id,password):
        with open("staff_info.txt","r")as file:
            data = file.readlines()
        for staff_info in data :
            if email_id in staff_info and password in staff_info:
                # if email_id in staff_info:
                #     email_ind=data.index(staff_info)
                #     print('email ind',email_ind)
                #     if password in staff_info:
                #         password_ind= data.index(staff_info)
                #         print('passwoed ind',password_ind)
                #         if email_ind == password_ind:
                self.log_in_flag = True
                return self.log_in_flag
            else:
                self.log_in_flag = False
        return self.log_in_flag
        

    def movie_schedule(self):
        with open("theater_schedule.txt","r") as file:
            data = file.read()
        data = data.split(':')
        #print(data)
        schedule = (f'''
*********************************** Movies Screening now ********************************

Movie 1 : {data[1]} {' '*(40-len(data[1]))} {data[4]}:{data[5]}:{data[6]}
Movie 2 : {data[9]} {' '*(40-len(data[9]))} {data[12]}:{data[13]}:{data[14]}
Movie 3 : {data[17]} {' '*(40-len(data[17]))} {data[20]}:{data[21]}:{data[22]}''')
        return schedule

    def screens(self,slot):
        self.sc_1 = '''
        | H-1 | | H-2 | | H-3 | | H-4 |      | H-5 | | H-6 | | H-7 | | H-8 |
        |_____| |_____| |_____| |_____|      |_____| |_____| |_____| |_____|

        | G-1 | | G-2 | | G-3 | | G-4 |      | G-5 | | G-6 | | G-7 | | G-8 |
        |_____| |_____| |_____| |_____|      |_____| |_____| |_____| |_____|
                
        | F-1 | | F-2 | | F-3 | | F-4 |      | F-5 | | F-6 | | F-7 | | F-8 |
        |_____| |_____| |_____| |_____|      |_____| |_____| |_____| |_____|
                
        | E-1 | | E-2 | | E-3 | | E-4 |      | E-5 | | E-6 | | E-7 | | E-8 |
        |_____| |_____| |_____| |_____|      |_____| |_____| |_____| |_____|

        | D-1 | | D-2 | | D-3 | | D-4 |      | D-5 | | D-6 | | D-7 | | D-8 |
        |_____| |_____| |_____| |_____|      |_____| |_____| |_____| |_____|

        | C-1 | | C-2 | | C-3 | | C-4 |      | C-5 | | C-6 | | C-7 | | C-8 |
        |_____| |_____| |_____| |_____|      |_____| |_____| |_____| |_____|

        | B-1 | | B-2 | | B-3 | | B-4 |      | B-5 | | B-6 | | B-7 | | B-8 |
        |_____| |_____| |_____| |_____|      |_____| |_____| |_____| |_____|

        | A-1 | | A-2 | | A-3 | | A-4 |      | A-5 | | A-6 | | A-7 | | A-8 |
        |_____| |_____| |_____| |_____|      |_____| |_____| |_____| |_____|

                                    DISPLAY SCREEN
        ------------------------------------------------------------------------
        ------------------------------------------------------------------------'''

        self.sc_2 = '''
            | H-1 | | H-2 | | H-3 | | H-4 | | H-5 | | H-6 | | H-7 | | H-8 | | H-9 |
            |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|

            | G-1 | | G-2 | | G-3 | | G-4 | | G-5 | | G-6 | | G-7 | | G-8 | | G-9 |
            |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|


        | F-1 | | F-2 |         | F-3 | | F-4 | | F-5 | | F-6 |         | F-7 | | F-8 |
        |_____| |_____|         |_____| |_____| |_____| |_____|         |_____| |_____|
                
        | E-1 | | E-2 |         | E-3 | | E-4 | | E-5 | | E-6 |         | E-7 | | E-8 |
        |_____| |_____|         |_____| |_____| |_____| |_____|         |_____| |_____|

        | D-1 | | D-2 |         | D-3 | | D-4 | | D-5 | | D-6 |         | D-7 | | D-8 |
        |_____| |_____|         |_____| |_____| |_____| |_____|         |_____| |_____|

        | C-1 | | C-2 |         | C-3 | | C-4 | | C-5 | | C-6 |         | C-7 | | C-8 |
        |_____| |_____|         |_____| |_____| |_____| |_____|         |_____| |_____|

        | B-1 | | B-2 |         | B-3 | | B-4 | | B-5 | | B-6 |         | B-7 | | B-8 |
        |_____| |_____|         |_____| |_____| |_____| |_____|         |_____| |_____|

        | A-1 | | A-2 |         | A-3 | | A-4 | | A-5 | | A-6 |         | A-7 | | A-8 |
        |_____| |_____|         |_____| |_____| |_____| |_____|         |_____| |_____|

                                        DISPLAY SCREEN
        -------------------------------------------------------------------------------
        -------------------------------------------------------------------------------'''
        if slot == '1': 
            return(self.sc_1)
        elif slot =='2':
            return(self.sc_2)
        else:
            print("\n************************* Invalid Screen Selection **************************\n")
        
    def screen_allotment_arragement(self,m_ch,select_time_slot):
        def display_seats(screen,position):
                ls = []
                with open("theater_schedule.txt","r")as file:
                    data = file.read()
                data = data.split(':')
                # print(data)
                ls = data[position]
                ls_new = re.findall(r'[a-zA-Z]{1}-[0-9]{1}',ls)
                # print(ls_new)
                # print(ls_new[0])
                screen = self.screens(screen)
                for seat in ls_new:
                    screen = screen.replace(seat,'   ')
                    # print(seat)
                return screen
        if m_ch =='1' and select_time_slot =='1':
            return display_seats(m_ch,2)
        elif m_ch =='1' and select_time_slot =='2':
            return display_seats(m_ch,3)
        elif m_ch =='2' and select_time_slot =='1':
            return display_seats(m_ch,10)
        elif m_ch =='2' and select_time_slot =='2':
            return display_seats(m_ch,11)
        elif m_ch =='3' and select_time_slot =='1':
            return display_seats('2',18)
        elif m_ch =='3' and select_time_slot =='2':
            return display_seats('2',19)

    def seats_availability(self,m_ch,select_time_slot,s_check):
        def no_of_seats_available(position):
            ls = []
            with open("theater_schedule.txt","r")as file:
                data = file.read()
            data = data.split(':')
            #print(data)
            ls = data[position]
            ls_new = re.findall(r'[a-zA-Z]{1}-[0-9]{1}',ls)
            # print(ls_new)
            no_of_seats = len(ls_new)
            if m_ch == '1' and no_of_seats + s_check > 64:
                return self.seat_available_flag
            elif (m_ch == '2' or m_ch == '3') and no_of_seats + s_check > 66:
                return self.seat_available_flag
            else:
                self.seat_available_flag = True
                return self.seat_available_flag
        
        if m_ch =='1'and select_time_slot =='1':
            return no_of_seats_available(2)
        elif m_ch =='1'and select_time_slot =='2':
            return no_of_seats_available(3)
        elif m_ch =='2' and select_time_slot =='1':
            return no_of_seats_available(10)
        elif m_ch =='2' and select_time_slot =='2':
            return no_of_seats_available(11)
        elif m_ch =='3' and select_time_slot =='1':
            return no_of_seats_available(18)
        elif m_ch =='3' and select_time_slot =='2':
            return no_of_seats_available(19)

    def ticket_prizing(self,m_ch,time_slot,no_of_tickets):
        with open("theater_schedule.txt","r")as file:
            data = file.read()
        prices = re.findall(r'\*\d+',data)
        prices = ','.join(prices)
        prices = prices.replace('*','')
        prices = prices.split(',')
        self.movie_price = prices

        if m_ch =='1'and time_slot =='1':
            one_price = int(prices[0])
            total_price = no_of_tickets * one_price
            return [one_price,total_price]
        elif m_ch =='1'and time_slot =='2':
            one_price = int(prices[1])
            total_price = no_of_tickets * one_price
            return [one_price,total_price]
        elif m_ch =='2'and time_slot =='1':
            one_price = int(prices[2])
            total_price = no_of_tickets * one_price
            return [one_price,total_price]
        elif m_ch =='2'and time_slot =='2':
            one_price = int(prices[3])
            total_price = no_of_tickets * one_price
            return [one_price,total_price]
        elif m_ch =='3'and time_slot =='1':
            one_price = int(prices[4])
            total_price = no_of_tickets * one_price
            return [one_price,total_price]
        elif m_ch =='3'and time_slot =='2':
            one_price = int(prices[5])
            total_price = no_of_tickets * one_price
            return [one_price,total_price]

    def check_seat_already_used(self,screen,time_slot,seat_numbers1):
        with open("theater_schedule.txt","r")as file:
            data = file.read()
        data1 = data.split(':')  
        # print(data1)
        occupied_seat_no_list = [2,3,10,11,19,20]
        valid = 0
        if screen == 1 and time_slot == 1:
            for i in seat_numbers1:
                if i in data1[occupied_seat_no_list[0]]:
                    valid+=1
            return valid
        elif screen == 1 and time_slot == 2:
            for i in seat_numbers1:
                if i in data1[occupied_seat_no_list[1]]:
                    valid+=1
            return valid
        elif screen == 2 and time_slot == 1:
            for i in seat_numbers1:
                if i in data1[occupied_seat_no_list[2]]:
                    valid+=1
            return valid
        elif screen == 2 and time_slot == 2:
            for i in seat_numbers1:
                if i in data1[occupied_seat_no_list[3]]:
                    valid+=1
            return valid
        elif screen == 3 and time_slot == 1:
            for i in seat_numbers1:
                if i in data1[occupied_seat_no_list[4]]:
                    valid+=1
            return valid
        elif screen == 3 and time_slot == 2:
            for i in seat_numbers1:
                if i in data1[occupied_seat_no_list[5]]:
                    valid+=1
            return valid

    def all_in_one_ticket(self,screen,time_slot,no_of_tickets,seat_numbers):
        unique_no = random.randint(100000,999999)
        def booking_data(screen,no_of_tickets,seat_numbers,name_position,time_position):
            with open("theater_schedule.txt","r")as file:
                data = file.read()
            data1 = data.split(':')   # movie_name
            # print(data1)
            overriding_seat_no_list = [2,3,10,11,18,19]
            data2 = re.findall(r'\d{2}:\d{2} [a-zA-Z]{2}',data)    # movie_timing
            # print(data2)
            write_data = f"\nTICKET ID : {unique_no}\nMovie name : {data1[name_position]}\nTiming : {data2[time_position]}\nSeats Booked : {no_of_tickets}({seat_numbers})\nSCREEN : {screen}\n\n***\n"
                
            existing_seat_no_data = data1[overriding_seat_no_list[time_position]]
            existing_seat_no_data = existing_seat_no_data.replace('[','')
            existing_seat_no_data = existing_seat_no_data.replace(']','')
            existing_seat_no_data = existing_seat_no_data.strip()
            new_seat_no_data = existing_seat_no_data + seat_numbers
            new_seat_no_data = f"[{new_seat_no_data}]"
            data1.pop(overriding_seat_no_list[time_position])
            data1.insert(overriding_seat_no_list[time_position],f'{new_seat_no_data}')
            data1 = ':'.join(data1)
            with open("theater_schedule.txt","w")as file:
                file.write(data1)
                return write_data

        if screen == 1 and time_slot == 1:
            write_data = booking_data(screen,no_of_tickets,seat_numbers,1,0)
            # print(write_data)
            with open("booking_info.txt","a")as file:
                file.write(write_data)
                return unique_no
        elif screen == 1 and time_slot == 2:
            write_data = booking_data(screen,no_of_tickets,seat_numbers,1,1)
            with open("booking_info.txt","a")as file:
                file.write(write_data)
                return unique_no
        elif screen == 2 and time_slot == 1:
            write_data = booking_data(screen,no_of_tickets,seat_numbers,9,2)
            with open("booking_info.txt","a")as file:
                file.write(write_data)
                return unique_no
        elif screen == 2 and time_slot == 2:
            write_data = booking_data(screen,no_of_tickets,seat_numbers,9,3)
            with open("booking_info.txt","a")as file:
                file.write(write_data)
                return unique_no
        elif screen == 3 and time_slot == 1:
            write_data = booking_data(screen,no_of_tickets,seat_numbers,17,4)
            with open("booking_info.txt","a")as file:
                file.write(write_data)
                return unique_no
        elif screen == 3 and time_slot == 2:
            write_data = booking_data(screen,no_of_tickets,seat_numbers,17,5)
            with open("booking_info.txt","a")as file:
                file.write(write_data)
                return unique_no

    def display_ticket(self,unique_no):    
        with open("booking_info.txt","r")as file:
            info = file.readlines()
            # print(info)
            start_ind = info.index(f"TICKET ID : {unique_no}\n")
            # print(start_ind) 
            info = info[start_ind:]
            end_ind = info.index("***\n")
            # print(end_ind)
            info = info[:end_ind+1]
            info = ''.join(info)
            # print(info)
            return info

    def valid_ticket_no(self,ticket_no):
        with open("booking_info.txt","r")as file:
            data = file.read()
        data2 = re.findall(r'\d{6}',data)
        if ticket_no in data2:
            self.valid_ticket_no_flag = True
            return self.valid_ticket_no_flag
        else:
            return self.valid_ticket_no_flag


    def parking_availability(self,bike_slot,car_slot):
        with open("theater_schedule.txt","r")as file:
            data = file.read()
        data1 = data.split(':')
        # print(data1)
        # print(data1.index("\nBike "))
        accuired_slots_bike = data1[26]
        accuired_slots_bike_data = re.findall(r'[a-zA-Z]-\d+',accuired_slots_bike)
        accuired_slots_car = data1[28]
        accuired_slots_car_data = re.findall(r'[a-zA-Z]-\d+',accuired_slots_car)
        if len(accuired_slots_bike_data) + bike_slot > 30 :
            self.parking_availability_flag = False
        if len(accuired_slots_car_data) + car_slot > 20 :
            self.parking_availability_flag = False
        return self.parking_availability_flag

    def parking_allowed_as_per_ticket(self,ticket_no,number_of_p_slots):
        with open("booking_info.txt","r")as file:
            data = file.readlines()
        # print(data)
        data1 = f'TICKET ID : {ticket_no}\n'
        if data1 in data:
            start_ind = data.index(data1)
        # print(start_ind)
        data = data[start_ind:]
        end_ind = data.index('***\n')
        data = data[0:end_ind]
        # print(data)
        req_data = data[3]
        # print(req_data)
        req_data = re.findall(r'[a-zA-Z]-\d{1}',req_data)
        # print(req_data)
        p_slots_allowed = len(req_data)
        # print(p_slots_allowed)
        if p_slots_allowed >= number_of_p_slots:
            self.parking_allowed_as_per_ticket_flag = True
        else:
            pass
        return self.parking_allowed_as_per_ticket_flag


    def parking(self,bike_slot,car_slot):
        if bike_slot != 0 :
            with open("theater_schedule.txt","r")as file:
                data = file.read()
            data1 = data.split(':')
            acquired_slots_bike = data1[26]
            # print(acquired_slots_bike)
            acquired_slots_bike_data =  re.findall(r'T-\d+',acquired_slots_bike)
            # print(acquired_slots_bike_data)
            if acquired_slots_bike_data:
                last_slot_used = acquired_slots_bike_data[-1]
                last_slot_used_number = re.findall(r'\d+',last_slot_used)
                new_slots = ""
                for slot_generator in range(int(last_slot_used_number[0])+1,(int(last_slot_used_number[0])+bike_slot)+1):
                    new_data = f"T-{slot_generator}"
                    new_slots = f"{new_slots} ,{new_data}"
                new_slots = re.findall(r'T-\d+',new_slots)
                # print(new_slots)
                acquired_slots_bike_data = acquired_slots_bike_data + new_slots
                acquired_slots_bike_data = str(acquired_slots_bike_data)
                # print(acquired_slots_bike_data)
                data1.pop(26)
                data1.insert(26,acquired_slots_bike_data)
                data1 = ':'.join(data1)
                # print(data1)
                with open("theater_schedule.txt","w")as file:
                    file.write(data1)
                with open("booking_info.txt","r")as file:
                    b_data = file.readlines()
                # print(b_data)
                add_parking_data = f'\nBooked Bike Parking Slot : {new_slots}\n' 
                b_data.insert(-2,add_parking_data)
                b_data = "".join(b_data)
                # print(b_data)
                with open("booking_info.txt","w")as file:
                    file.write(b_data)

            else:
                new_slots = ""
                for slot_generator in range(1,bike_slot+1):
                    new_data = f"T-{slot_generator}"
                    new_slots = f"{new_slots} ,{new_data}"
                new_slots = re.findall(r'T-\d+',new_slots)
                new_slots = str(new_slots)
                # print(new_slots)
                data1.pop(26)
                data1.insert(26,new_slots)
                data1 = ':'.join(data1)
                # print(data1)
                with open("theater_schedule.txt","w")as file:
                    file.write(data1)
                with open("booking_info.txt","r")as file:
                    b_data = file.readlines()
                # print(b_data)
                add_parking_data = f'\nBooked Bike Parking Slot : {new_slots}\n' 
                b_data.insert(-2,add_parking_data)
                b_data = "".join(b_data)
                # print(b_data)
                with open("booking_info.txt","w")as file:
                    file.write(b_data)

        if car_slot != 0 :
            with open("theater_schedule.txt","r")as file:
                data = file.read()
            data1 = data.split(':')
            acquired_slots_car = data1[28]
            acquired_slots_car_data =  re.findall(r'F-\d+',acquired_slots_car)
            # print(acquired_slots_car_data)
            if acquired_slots_car_data:
                last_slot_used = acquired_slots_car_data[-1]
                last_slot_used_number = re.findall(r'\d+',last_slot_used)
                new_slots = ""
                for slot_generator in range(int(last_slot_used_number[0])+1,(int(last_slot_used_number[0])+car_slot)+1):
                    new_data = f"F-{slot_generator}"
                    new_slots = f"{new_slots} ,{new_data}"
                new_slots = re.findall(r'F-\d+',new_slots)
                # print(new_slots)
                acquired_slots_car_data = acquired_slots_car_data + new_slots
                acquired_slots_car_data = str(acquired_slots_car_data)
                # print(acquired_slots_car_data)
                data1.pop(28)
                data1.insert(28,acquired_slots_car_data)
                # print(data1)
                data1 = ':'.join(data1)
                # print(data2)
                with open("theater_schedule.txt","w")as file:
                    file.write(data1)
                with open("booking_info.txt","r")as file:
                    b_data = file.readlines()
                # print(b_data)
                add_parking_data = f'\nBooked Car Parking Slot : {new_slots}\n' 
                b_data.insert(-2,add_parking_data)
                b_data = "".join(b_data)
                # print(b_data)
                with open("booking_info.txt","w")as file:
                    file.write(b_data)

            else:
                new_slots = ""
                for slot_generator in range(1,car_slot+1):
                    new_data = f"F-{slot_generator}"
                    new_slots = f"{new_slots} ,{new_data}"
                new_slots = re.findall(r'F-\d+',new_slots)
                new_slots = str(new_slots)
                # print(new_slots)
                data1.pop(28)
                data1.insert(28,new_slots)
                data1 = ':'.join(data1)
                # print(data1)
                with open("theater_schedule.txt","w")as file:
                    file.write(data1)
                with open("booking_info.txt","r")as file:
                    b_data = file.readlines()
                # print(b_data)
                add_parking_data = f'\nBooked Car Parking Slot : {new_slots}\n' 
                b_data.insert(-2,add_parking_data)
                b_data = "".join(b_data)
                # print(b_data)
                with open("booking_info.txt","w")as file:
                    file.write(b_data)

        self.parking_flag = True
        return self.parking_flag
        
        
    def display_food(self,choice):
        with open("theater_schedule.txt","r")as file:
            data = file.read()
        data1 = data.split(':')
        # print(data1)
        snacks = data1[-4]
        beverages = data1[-2]
        self.snacks_new = re.findall(r'[a-zA-Z ]+',snacks)
        self.snacks_prices = re.findall(r'\d+',snacks)
        self.beverages_new = re.findall(r'[a-zA-Z ]+',beverages)
        self.beverages_prices = re.findall(r'\d+',beverages)
        if choice == '1':
            for ind in range(len(self.snacks_new)):
                print(f'Press {ind+1} : {self.snacks_new[ind]}',(" "*(20-len(self.snacks_new[ind]))) ,f'Rs.{self.snacks_prices[ind]}')
        elif choice == '2':
            for ind in range(len(self.beverages_new)):
                print(f'Press {ind+1} : {self.beverages_new[ind]}',(" "*(15-len(self.beverages_new[ind]))) ,f'Rs.{self.beverages_prices[ind]}')

    def cart_display(self,cart):
        self.display_food(3)
        cart_length = len(cart)
        cart_new = []
        elements = 0
        while elements < cart_length:
            cart_new.append([cart[elements],cart[elements+1],cart[elements+2]])
            elements += 3
        # print(cart_new)
        sr_no = 0
        total = 0
        self.display = []
        for item in cart_new:
            sr_no+=1
            if item[0] == '1':
                self.display.extend([f"{sr_no}     {self.snacks_new[int(item[1])-1]}",' '*(18 - len(self.snacks_new[int(item[1])-1])),f"Rs.{self.snacks_prices[int(item[1])-1]} X {int(item[2])}",' '*(14-len(f"Rs.{self.snacks_prices[int(item[1])-1]} X {int(item[2])}")),f"{int(self.snacks_prices[int(item[1])-1])*int(item[2])}","\n"])
                total = total + int(self.snacks_prices[int(item[1])-1])*int(item[2]) 
            elif item[0] == '2':
                self.display.extend([f"{sr_no}     {self.beverages_new[int(item[1])-1]}",' '*(18 - len(self.beverages_new[int(item[1])-1])),f"Rs.{self.beverages_prices[int(item[1])-1]} X {int(item[2])}",' '*(15-len(f"Rs.{self.beverages_prices[int(item[1])-1]} X {int(item[2])}")),f"{int(self.beverages_prices[int(item[1])-1])*int(item[2])}","\n"])
                total = total + int(self.beverages_prices[int(item[1])-1])*int(item[2])
        self.display.extend(["\n",' '*24,f"Total    :    {total}","\n"])
        self.display_use = self.display
        self.display_new = ''.join(self.display)
        
        return self.display_new
        # print("\n",' '*26,f"Total    :    {total}")

    def delete_cart(self,cart,sr_no):
        # print(cart)
        index_of_element = (int(sr_no)*2)+(-2 + (int(sr_no) - 1))
        cart.pop(index_of_element)
        cart.pop(index_of_element)
        cart.pop(index_of_element)
        # print("Index Element is : ",index_of_element)
        # print(cart)
        return cart

    def cart_paid(self,ticket_no,cart):
        self.cart_display(cart)
        self.display_use
        with open("booking_info.txt","r") as file:
            data = file.readlines()
        start_ind = data.index(f'TICKET ID : {ticket_no}\n')
        data1=data[start_ind :]
        end_ind = data1.index('***\n')
        data1 = data1[:end_ind + 1]
        for element in range(start_ind,start_ind+len(data1)):
            data.pop(start_ind)
        data1.insert(-2,f"\nFOOD COURT : \n")
        data1.pop()
        data1.extend(self.display_use)
        data1.insert(-1,'\n\n')
        data1.insert(-1,'***\n')
        data.extend(data1)
        data = ''.join(data)
        # print(data)
        with open("booking_info.txt","w") as file:
            file.write(data)


if __name__ =="__main__":
    app = Movie_Application()
    # app.valid_update_food_serial_no()
    # app.display_food("1")
    # app.view_staff()
    # app.remove_staff(103)
    # app.add_new_food('2',"chai",50)
    def entry():
        print('''
  ----------------------------------------------------------------------------------------
 |                                Welcome To TheOne Cinema                                |
  ----------------------------------------------------------------------------------------

--------------------------
| Press 1 : Staff Log In |
--------------------------
-------------------------- 
| Press 2 : Admin Log In |
--------------------------
--------------------------
| Press 3 : Exit         |
--------------------------
        
        ''')
    entry()
    while True:
        e_ch = input("Enter Your Choice : ")
        if e_ch =='1':
            email_id = input("Enter Your Email : ")
            email_id = email_id.strip()
            password = input("Enter Your Password : ")
            password = password.strip()
            log_in_status = app.log_in(email_id,password)
            if log_in_status == False:
                print("\n************************** Incorrect Email Or Password ****************************\n")
                entry()
            else:
                def main():
                    print()
                    print("\n******************** Welcome to the Application ************************\n")
                    print("\nPress 1 : Check Schedule And Seats\nPress 2 : Book Tickets\nPress 3 : Book Parking Slots\nPress 4 : Food Court\nPress 5 : View Ticket\nPress 6 : Exit\n")
                main()
                schedule = app.movie_schedule()
                def movie_no(n):
                    timings = re.findall(r'\d{2}:\d{2} [a-zA-Z]{2}',schedule)
                    # print(timings)
                    print("*************************** Timing Schedule For Selected Show **************************\n")
                    print(f"Press 1 : {timings[n]}")
                    print(f"Press 2 : {timings[n+1]}")
                    #while True:
                    select_time_slot = input("Enter Time Slot Of Your Choice : ")
                    if select_time_slot =='1':
                        print("\n****************************** Seats Availability **************************")
                        arrangement = app.screen_allotment_arragement(m_ch,select_time_slot)
                        return [arrangement,select_time_slot]
                                            
                    elif select_time_slot =='2':
                        print("\n****************************** Seats Availability **************************")
                        arrangement = app.screen_allotment_arragement(m_ch,select_time_slot)
                        return [arrangement,select_time_slot]
                                
                    else:
                        return ["\n********************* Invalid Choice ***********************\n"]
                while True:
                    l_ch = input("Enter Your Choice : ")
                    if l_ch == '1':                
                        while True:
                            print(schedule)
                            print("Press 4 :  Exit\n" )
                            m_ch = input("Enter Movie Number : ")
                            print()
                            if m_ch =="1":
                                details = movie_no(0)
                                print(details[0])
                            elif m_ch =="2":
                                details = movie_no(2)
                                print(details[0])
                            elif m_ch == "3":
                                details = movie_no(4)
                                print(details[0])
                            elif m_ch == '4':
                                main()
                                break
                            else:
                                print("\n******************* Invalid Choice Please Enter valid Choice **********************\n")
                    elif l_ch == '2':
                        def main_process(movie_number):
                            details = movie_no(movie_number)  # returns list [arrangement display, time slot selected]
                            print(details[0])
                            s_check = input("Enter number of tickets : ")
                            if not s_check.isdigit():
                                print("\n************************ Enter Digits only **********************\n")
                            else:
                                check_flag = app.seats_availability(m_ch,details[1],int(s_check))   #movie choice,timeing choice, no of seats to check available or not
                                if check_flag == False:
                                    print("\n***************************** This Much Seats Not Available For The Show ************************\n")
                                else:
                                    seat_numbers = input("Enter the Seat Numbers : ")
                                    seat_numbers = seat_numbers.strip()
                                    seat_numbers = re.findall(r'\b[a-zA-Z]-\d\b',seat_numbers)
                                    seat_numbers1 = []
                                    for cap in seat_numbers:
                                        seat_numbers1.append(cap.capitalize())

                                    check_seats = app.check_seat_already_used(int(m_ch),int(details[1]),seat_numbers1)
                                    if len(seat_numbers1) != int(s_check):
                                        print("\n******************* Enter Proper Seat numbers as per no of tickets you selected ***************\n")
                                    elif check_seats != 0:
                                        print("\n*************************** Selected Seat Is Already Booked **********************\n")
                                    else:
                                        price = app.ticket_prizing(m_ch,details[1],int(s_check))  # movie choice,time slot,no.of tickets
                                        print(f"Price To Be Paid : {price[0]} * {s_check} = {price[1]}")
                                        while True:
                                            transaction = input("Is The Price Paid (Press 1 - Yes , Press 2 - No) : ")
                                            if transaction.isdigit()==True and (int(transaction) > 0 and int(transaction) < 3) :
                                                if transaction == '2':
                                                    print('\n****************** Transaction cancelled *******************\n')
                                                    main()
                                                    break
                                                else:
                                                    seat_numbers1 = ','.join(seat_numbers1)
                                                    # print(seat_numbers1)
                                                    # app.all_in_one_ticket(int(m_ch),int(details[1]),int(s_check),seat_numbers1)
                                                    unique_number = app.all_in_one_ticket(int(m_ch),int(details[1]),int(s_check),seat_numbers1)
                                                    # print(unique_number)
                                                    print()
                                                    print()
                                                    print(app.display_ticket(unique_number))
                                                    break                    
                                            else:
                                                print("\n**************** invalid input **************\n")

                        d = f"{schedule}\nPress 4 :  Exit\n"
                        print(d)
                        while True :
                            m_ch = input("Enter Movie Number : ")
                            print()
                            if m_ch =="1":
                                main_process(0)                                    
                                print(d)
                            elif m_ch =="2":
                                main_process(2)
                                print(d)
                            elif m_ch == "3":
                                main_process(4)
                                print(d)
                            elif m_ch == '4':
                                main()
                                break
                            else:
                                print("\n******************* Invalid Choice Please Enter valid Choice **********************\n")
                    elif l_ch =='3':
                        ticket_no = input("Enter Unique Ticket Number : ")
                        ticket_no = ticket_no.strip()                        
                        if ticket_no.isdigit() == False or len(ticket_no) != 6 :
                            print("\n************************** Enter 6 digit Ticket Number Only *************************\n")
                            main()
                        elif app.valid_ticket_no(ticket_no) == False:
                            print("\n********************* Ticket Number Does Not Exist ********************\n")
                            main()
                        else :
                            no_of_slots = input("Enter Number of Parking Slots required : ")
                            no_of_slots = no_of_slots.strip()
                            if no_of_slots.isdigit() == False :
                                print("\n*************************** Enter digits Ony ************************\n")
                                main()
                            elif (app.parking_allowed_as_per_ticket(ticket_no,int(no_of_slots))) == False :
                                print("\n********************* Only One Slot Per Ticket Is Allowed *******************\n")
                                main()
                            else:
                                while True:
                                    bike_slot = input("Enter Number Of Bike Slots Required : ")
                                    if bike_slot == '':
                                        bike_slot = '0'
                                    car_slot = input("Enter Number Of Car Slots Required : ")
                                    if car_slot =='':
                                        car_slot = '0'
                                    if bike_slot.isdigit() == False or car_slot.isdigit()== False:
                                        print("\n***************** Enter Slots Required In digits Only **************\n")
                                    elif int(bike_slot) + int(car_slot) != int(no_of_slots) :
                                        print("\n********************* Number Of Slots Required And Number of Slots Mentioned Missmatch *****************\n")
                                    else:
                                        result = app.parking_availability(int(bike_slot),int(car_slot))
                                        if result == False:
                                            print("Sorry Parking Slots Are Full Right Now...")
                                            main()
                                            break
                                        else:
                                            parking_flag = app.parking(int(bike_slot),int(car_slot))
                                            if parking_flag == False:
                                                print("\n************************** Something Went Wrong **************\n")
                                            else:
                                                print("\n****************************** Parking Added Succesfully ********************\n")
                                                print("\nNote : Parking is Free Only Till The Time Span of Movie.\n")
                                                print()
                                                print(app.display_ticket(ticket_no))
                                                print()
                                                main()
                                                break
                    elif l_ch =='4':
                        ticket_no = input("Enter Unique Ticket Number : ")
                        ticket_no = ticket_no.strip()                        
                        if ticket_no.isdigit() == False or len(ticket_no) != 6 :
                            print("\n************************** Enter 6 digit Ticket Number Only *************************\n")
                            main()
                        elif app.valid_ticket_no(ticket_no) == False:
                            print("\n********************* Ticket Number Does Not Exist ********************\n")
                            main()
                        else :
                            cart = []
                            snacks = []
                            beverages = []
                            cart_value = 0
                            complete = 0
                            while True:
                                if complete != 0:
                                    break
                                if cart_value != 0:
                                    cart_value = 0
                                    cart=[]
                                    snacks = []
                                    beverages = []
                                food_select = "\n*********************** Food Court **********************\nPress 1 : Snacks\nPress 2 : Beverages\nPress 3 : Cart\nPress 4 : Exit"
                                print(food_select)
                                print()
                                f_ch = input('Enter Your food choice : ')
                                print()
                                if f_ch == '1':
                                    while True:
                                        app.display_food(f_ch)
                                        print(f"Press {(len(app.snacks_new)+1)} :  Exit")
                                        print()
                                        item = input("Please Enter Choice Of Snack : ")
                                        if (item.isdigit() == False) or (int(item) > len(app.snacks_new)+1) :
                                            print("\n****************** Invalid choice **********************\n")
                                        elif item == (str(len(app.snacks_new)+1)) :
                                            break
                                        else:
                                            quantity = input("Please Enter Quantity : ")
                                            print()
                                            if quantity.isdigit() == False:
                                                print("\n****************** Invalid choice **********************\n")
                                            else:
                                                snacks.append(f_ch)
                                                snacks.append(item)
                                                snacks.append(quantity)             
                                elif f_ch == '2':
                                    while True :
                                        app.display_food(f_ch)
                                        print(f"Press {(len(app.beverages_new)+1)} :  Exit")
                                        print()
                                        item1 = input("Please Enter Choice Of Drink : ")
                                        if (item1.isdigit() == False) or (int(item1) > len(app.beverages_new)+1) :
                                            print("\n****************** Invalid choice **********************\n")
                                        elif item1 == (str(len(app.beverages_new)+1)) :
                                            break
                                        else:
                                            quantity1 = input("Please Enter Quantity : ")
                                            print()
                                            if quantity1.isdigit() == False:
                                                print("\n****************** Invalid choice **********************\n")
                                            else:
                                                beverages.append(f_ch)
                                                beverages.append(item1)
                                                beverages.append(quantity1)
                                                
                                elif f_ch == '3':
                                    cart = snacks + beverages
                                    # print(cart)
                                    while True:
                                        cart_menu = "\n****************** Cart Options *****************\n\nPress 1 : Display Cart\nPress 2 : Delete From Cart\nPress 3 : Exit\n"
                                        print(cart_menu)
                                        cart_ch = input("Enter Your Cart Choice  : ")
                                        print()
                                        if cart_ch.isdigit() == False or int(cart_ch) > 3:
                                            print("\n******************** Invalid Input **********************\n")
                                        elif cart_ch == '3':
                                            break
                                        else:
                                            if cart_ch == '1': # display cart and pay
                                                if not cart :
                                                    print("\n******************** Cart Is Empty ****************\n")
                                                else :
                                                    print(app.cart_display(cart))
                                                    print()
                                                    pay_ch = input("Is The Order Paid (Press 1 : Yes , Press 2 : No , Press 3 : Exit ) : ")
                                                    if (pay_ch.isdigit() == False) or (int(pay_ch) > 3) :
                                                        print("\n****************** Invalid choice **********************\n")
                                                    else:
                                                        if pay_ch == '2':
                                                            print("\n********************** Transction Cancelled **************\n")
                                                            cart_value += 1
                                                            break
                                                        elif pay_ch == '3':
                                                            pass
                                                        elif pay_ch == '1':
                                                            app.cart_paid(ticket_no,cart)
                                                            print("\n************** Purches Successful ************\n")
                                                            complete += 1
                                                            main()
                                                            break

                                            elif cart_ch == '2': # delete from cart
                                                if not cart :
                                                    print("\n******************** Cart Is Empty ****************\n")
                                                else :
                                                    print(app.cart_display(cart))
                                                    print()
                                                    sr_no = input("Enter The Sr.No Of Item To Delete : ")
                                                    if (sr_no.isdigit() == False) or (int(sr_no) > len(cart)//3):
                                                        print("\n****************** Invalid choice **********************\n")
                                                    else:
                                                        new_cart = app.delete_cart(cart,sr_no)
                                                        cart = new_cart
                                                        print("\n**************** Item has been removed ************\n")

                                            elif cart_ch == '3' : # exit
                                                pass
                                elif f_ch == '4':
                                    main()
                                    break
                                else:
                                    print("\n******************* Invalid Option *********************\n")

                    elif l_ch == '5':
                        ticket_no = input("Enter Unique Ticket Number : ")
                        ticket_no = ticket_no.strip()                        
                        if ticket_no.isdigit() == False or len(ticket_no) != 6 :
                            print("\n************************** Enter 6 digit Ticket Number Only *************************\n")
                            main()
                        elif app.valid_ticket_no(ticket_no) == False:
                            print("\n********************* Ticket Number Does Not Exist ********************\n")
                            main()
                        else :
                            print()
                            print("*************************************************************************")
                            print(app.display_ticket(ticket_no))
                            print("*************************************************************************")
                            main()   
                    elif l_ch == '6':
                        print("\n********************* Successfully Logged Out From App ************************\n")
                        entry()                    
                        break
                    else:
                        print("\n**************************** Invalid Choice Please Enter Proper Choice ******************************\n")
        elif e_ch =='2':
            admin_Id = input("Enter Admin Id : ")
            adm_password = input("Enter Admin Password : ")
            if admin_Id != 'rohan@gmail.com' or adm_password != '123456':
                print("\n********************* Invalid Email Or Password *********************\n")
                entry()
            else:
                adm = "\n************************ Welcome Admin ***************************\n\nPress 1 : Update Staff\nPress 2 : Check Movies Schedule\nPress 3 : Update Movie Schedule And Pricing\nPress 4 : Update Food Court\nPress 5 : Exit"
                print(adm)
                while True:
                    print()
                    adm_ch = input("Enter Your Choice : ") 
                    if adm_ch.isdigit() == False or int(adm_ch) > 6 :
                        print("\n********************* Invalid Input **********************\n")
                    else:
                        if adm_ch == '1':
                            staff = ("\nPress 1 : View Staff\nPress 2 : Add Staff\nPress 3 : Remove Staff\nPress 4 : Exit\n")
                            print(staff)
                            while True:
                                staff_update_ch = input("Enter Your Choice : ")
                                print()
                                if staff_update_ch == '1':  # View Staff
                                    app.view_staff()
                                    print(staff)
                                elif staff_update_ch == '2':
                                    while True:
                                        f_name = input("Enter Your First Name : ")
                                        f_name = f_name.strip()
                                        valid_name = re.match(r'\b[a-zA-Z *]+\b',f_name)
                                        if valid_name :
                                            break
                                        else:
                                            print("\n************************ Error...Name Must Have Alphabets Only **********************\n")

                                    while True:
                                        l_name = input("Enter Your Last Name : ")
                                        l_name = l_name.strip()
                                        valid_name = re.match(r'\b[a-zA-Z *]+\b',l_name)
                                        if valid_name :
                                            break
                                        else:
                                            print("\n************************ Error...Name Must Have Alphabets Only **********************\n")
                                    
                                    while True:
                                        age = input("Enter Your Age : ")
                                        age = age.strip()
                                        valid_age = re.match(r'\d+',age)
                                        if valid_age:
                                            break
                                        else:
                                            print("\n************************ Error...Age Must Have Digits Only **********************\n")

                                    while True:
                                        contact = input("Enter Your Mobile Number : ")
                                        contact = contact.strip()
                                        valid_contact = re.match(r'\d+',contact)
                                        if contact.isdigit() == True and len(valid_contact.group()) == 10:
                                            break
                                        elif contact.isdigit() == False or len(valid_contact.group()) != 10 :
                                            print("\n************************ Error...Contact Must Be Of 10 Digits Only **********************\n")
                                        else:
                                            print("\n************************ Error...Contact Must Have Digits Only **********************\n")

                                    while True:
                                        email_id = input("Enter Your Email : ")
                                        email_id = email_id.strip()
                                        valid_email = re.match(r'\b[a-zA-Z0-9.*_*-*]+@[a-zA-Z]+\.[a-zA-Z]{2,}\b',email_id)
                                        if valid_email:
                                            break
                                        else:
                                            print("\n************************ Error...Invalid Email **********************\n")
                                    while True:
                                        password = input("Enter Your Password : ")
                                        password = password.strip()
                                        if len(password) < 6:
                                            print("\n************ Password Is Too Short Minimum 6 Character Required *************\n")
                                        elif len(password) > 15:
                                            print("\n************ Password Is Too Short Minimum 6 Character Required *************\n")
                                        else:
                                            
                                            c_password = input("Confirm Your Password : ")
                                            c_password = c_password.strip()
                                            if c_password == password:
                                                break
                                            else:
                                                print("\n*********************** Password Does Not Match *************************\n")    
                                    print("\nAll information Provided Above Is Correct And True.....\n\nPress 1 : Yes\nPress 2 : No\n")
                                    conformation = input("Enter Confirmation Choice : ")
                                    if conformation == '2':
                                        print("\n\n*******************Staff Enrollment Cancelled********************\n")
                                        print(staff)
                                    elif conformation == '1':
                                        registration = app.register(f_name,l_name,age,contact,email_id,password)        
                                        if registration == False:
                                            print("\n****************** Something Went Wrong ********************\n")
                                        else:
                                            print("\n************************ Registered Successfully You Can Log In Now ************************\n")
                                            print(staff)
                                    else: 
                                        print("************************************ Invalid Input **************************")
                                elif staff_update_ch == '3' :   #Remove staff
                                    emp_id = input("Enter Employee ID to be removed : ")
                                    if emp_id.isdigit() == False :
                                        print("\n********************** Enter Proper Id With Only Digits ********************\n ")
                                    else:
                                        r_staff = app.remove_staff(emp_id)
                                        if r_staff == True:
                                            print("\n******************** Employee has been removed ******************\n")
                                        print(staff)
                                elif staff_update_ch == '4':
                                    print(adm)
                                    break        

                        elif adm_ch == '2':
                            # schedule = app.movie_schedule()
                            print(app.movie_schedule())
                            print(adm)
                        elif adm_ch == '3':
                            schedule = app.movie_schedule()
                            print(schedule)
                            while True:
                                print()
                                update_movie_ch = input("Enter The Movie No To update : ")
                                if update_movie_ch.isdigit() == False or int(update_movie_ch) < 0 or int(update_movie_ch) > 3 :
                                    print("\n************************* Invalid Input ***********************\n")
                                else:
                                    timings = re.findall(r'\d{2}:\d{2} [a-zA-Z]{2}',schedule)    # Movie time list
                                    # print(timings)
                                    app.ticket_prizing(1,1,1)
                                    m_price = app.movie_price        # Movie Price list
                                    movie_names = re.findall(r'[a-zA-Z0-9. {0,1}]+',schedule)
                                    movie_names= [movie_names[2],movie_names[7],movie_names[12]]
                                    movie_names_new = [item.replace("Timings","") for item in movie_names]
                                    movie_names_new = [item.strip() for item in movie_names_new]    # movie name list
                                    # print(movie_names_new)

                                    def update_function():
                                        # while True:
                                        print("\n****************************** Movie Update Menu ******************************\n\nPress 1 : Update Movie Name \nPress 2 : Update timing\nPress 3 : Update Ticket Pricing\n")
                                        update_ch = input("Enter Your Choice : ")
                                        if update_ch == '1':
                                            print(f"\nCurrent Screening Movie Name : {movie_names_new[int(update_movie_ch)-1]}\n")
                                            updated_movie_name = input("Enter New Movie name : ")
                                            updated_movie_name = updated_movie_name.strip()
                                            # print(updated_movie_name)
                                            status =  app.movie_update(int(update_movie_ch),updated_movie_name)
                                            return status

                                        elif update_ch == '2':
                                            print(f"\nCurrent Screening Movie Name : {movie_names_new[int(update_movie_ch)-1]}\n")
                                            print(f"\nCurrent Movie Timings : ")
                                            if update_movie_ch == '1':
                                                time1 = timings[int(update_movie_ch)-1]
                                                time2 = timings[int(update_movie_ch)]
                                                print(f"Press 1 : {time1}")
                                                print(f"Press 2 : {time2}")
                                                # print(time1)
                                                # print(time2)
                                            elif update_movie_ch == '2':
                                                time1 = timings[int(update_movie_ch)]
                                                time2 = timings[int(update_movie_ch)+1]
                                                print(f"Press 1 : {time1}")
                                                print(f"Press 2 : {time2}")
                                            elif update_movie_ch == '3':
                                                time1 = timings[int(update_movie_ch)+1]
                                                time2 = timings[int(update_movie_ch)+2]
                                                print(f"Press 1 : {time1}")
                                                print(f"Press 2 : {time2}")
                                                
                                            updated_movie_time = input("Enter Time Schedule To Be Updated : ")
                                            updated_movie_time = updated_movie_time.strip()
                                            if updated_movie_time.isdigit() == False or int(updated_movie_time) < 0 or int(updated_movie_time) > 3 :
                                                print("\n************************** Invalid Input ********************\n")
                                            else:
                                                if updated_movie_time == '1':
                                                    print(f"\nCurrent movie time {time1}\n")
                                                    new_time = input("Enter updated time : ")
                                                    new_time1 = re.findall(r'\d{2}:\d{2} [a-zA-Z]{2}',new_time)
                                                    # print(new_time1)
                                                    if new_time1:
                                                        new_time1 = new_time1[0]
                                                        status = app.movie_update(f"{update_movie_ch}-{updated_movie_time}",new_time1)   # 1-1(movie choice-time slot,new time)
                                                        return status
                                                    else:
                                                        print("\n************** Enter Proper Time With AM or PM (ex. 09:00 AM) *****************")
                                                        print(adm)
                                                elif updated_movie_time == '2':
                                                    print(f"\nCurrent movie time {time2}\n")
                                                    new_time = input(f"\nEnter updated time : ")
                                                    new_time1 = re.findall(r'\d{2}:\d{2} [a-zA-Z]{2}',new_time)
                                                    # print(new_time1)
                                                    if new_time1:
                                                        new_time1 = new_time1[0]
                                                        status = app.movie_update(f"{update_movie_ch}-{updated_movie_time}",new_time1)    # 1-1(movie choice-time slot)
                                                        return status
                                                    else:                   
                                                        print("\n*************** Enter Proper Time With AM or PM (ex. 09:00 AM) *****************")
                                                        print(adm)
                                        elif update_ch =='3':
                                            print(f"\nCurrent Screening Movie Name : {movie_names_new[int(update_movie_ch)-1]}\n")
                                            print(f"\nCurrent Movie Timings And Pricing : ")
                                            if update_movie_ch == '1':
                                                price1 = m_price[int(update_movie_ch)-1]
                                                price2 = m_price[int(update_movie_ch)]
                                                print(f"Press 1 : {timings[int(update_movie_ch)-1]}     {price1}")
                                                print(f"Press 2 : {timings[int(update_movie_ch)]}     {price2}")
                                            elif update_movie_ch == '2':
                                                price1 = m_price[int(update_movie_ch)]
                                                price2 = m_price[int(update_movie_ch)+1]
                                                print(f"Press 1 : {timings[int(update_movie_ch)]}     {price1}")
                                                print(f"Press 2 : {timings[int(update_movie_ch)+1]}     {price2}")
                                            elif update_movie_ch == '3':
                                                price1 = m_price[int(update_movie_ch)+1]
                                                price2 = m_price[int(update_movie_ch)+2]
                                                print(f"Press 1 : {timings[int(update_movie_ch)+1]}     {price1}")
                                                print(f"Press 2 : {timings[int(update_movie_ch)+2]}     {price2}")
                                            
                                            updated_movie_time = input("\nSelect Time Schedule : ")
                                            updated_movie_time = updated_movie_time.strip()
                                            if updated_movie_time.isdigit() == False or int(updated_movie_time) < 0 or int(updated_movie_time) > 3 :
                                                print("\n************************** Invalid Input ********************\n")
                                            else:
                                                if updated_movie_time == '1':
                                                    print(f"\nCurrent Pricing For This Time Schedule : {price1}")
                                                    new_price = input("\nEnter Updated Price : ")
                                                    if new_price.isdigit() == False :
                                                        print("\n*********************** Enter Digits Only ************************\n")
                                                    else:
                                                        status =  app.movie_update(f"{update_movie_ch}({updated_movie_time})",int(new_price))   # 1-1(movie choice-time slot)
                                                        return status

                                                elif updated_movie_time == '2':
                                                    print(f"\nCurrent Pricing For This Time Schedule : {price2}")
                                                    new_price = input("\nEnter Updated Price : ")
                                                    if new_price.isdigit() == False :
                                                        print("\n*********************** Enter Digits Only ************************\n")
                                                    else:
                                                        status =  app.movie_update(f"{update_movie_ch}({updated_movie_time})",int(new_price))   # 1-1(movie choice-time slot)
                                                        return status
                                        else:
                                            print("\n*********************** Invalid Choice *********************\n")

                                    if update_movie_ch == '1':
                                        status = update_function()
                                        # print(status)
                                        if status == False or status == None:
                                            print("\n******************* Something Went Wrong *****************\n")
                                            print(adm)
                                            break
                                        else:
                                            print("\n****************** Movie Updated Successfully *********************\n")
                                            print(adm)
                                            break
                                    elif update_movie_ch == '2':
                                        status = update_function()
                                        # print(status)
                                        if status == False or status == None:
                                            print("\n******************* Something Went Wrong *****************\n")
                                            print(adm)
                                            break
                                        else:
                                            print("\n****************** Movie Updated Successfully *********************\n")
                                            print(adm)
                                            break
                                    elif update_movie_ch == '3':
                                        status = update_function()
                                        # print(status)
                                        if status == False or status == None :
                                            print("\n******************* Something Went Wrong *****************\n")
                                            print(adm)
                                            break
                                        else:
                                            print("\n****************** Movie Updated Successfully *********************\n")
                                            print(adm)
                                            break
                                    else:
                                        print("\n*********************** invalid Choice **************************\n")


                        elif adm_ch == '4':
                            f_change_menu = "\nPress 1 : Add Snack\nPress 2 : Add Beverage\nPress 3 : Delete Snack\nPress 4 : Delete Beverage\nPress 5 : Exit\n"
                            print(f_change_menu)
                            while True :
                                update_food_ch = input("Enter Choice To Update Food : ")
                                if update_food_ch == '1':
                                    print("\n***** Existing Food Items In Snacks Category *****\n")
                                    app.display_food('1')
                                    print()
                                    new_item = input("Enter Name Of New Product : ")
                                    while True:
                                        Price = input("Enter Price Of The Product : ")
                                        if Price.isdigit()==True:
                                            break
                                        else:
                                            print("\n********* Enter Digits Only **********\n")

                                    status = app.add_new_food(update_food_ch,new_item,Price)
                                    # print(status)
                                    if status == False:
                                        print("\n********************** Something Went Wrong ******************\n")
                                        print(f_change_menu)
                                        
                                    else:
                                        print("\n****************** Item Added Succesfully *********************\n")
                                        print(f_change_menu)

                                elif update_food_ch == '2':
                                    print("\n***** Existing Food Items In Beverages Category *****\n")
                                    app.display_food('2')
                                    print()
                                    new_item = input("Enter Name Of New Product : ")
                                    while True:
                                        Price = input("Enter Price Of The Product : ")
                                        if Price.isdigit()==True:
                                            break
                                        else:
                                            print("\n********* Enter Digits Only **********\n")
                                    status = app.add_new_food(update_food_ch,new_item,Price)
                                    if status == False:
                                        print("\n********************** Something Went Wrong ******************\n")
                                        print(f_change_menu)
                                    else:
                                        print("\n****************** Item Added Succesfully *********************\n")
                                        print(f_change_menu)

                                elif update_food_ch =='3': # delete snack
                                    print("\n***** Existing Food Items In Snacks Category *****\n")
                                    app.display_food('1')
                                    print()
                                    item_sr_no = input("Enter Serial Number Of Product To Be Deleted: ")
                                    if (item_sr_no.isdigit() == False) or (int(item_sr_no) > len(app.snacks_new)) :
                                        print("\n********************* Invalid Choice **********************\n")
                                        print(f_change_menu)
                                    else:
                                        status = app.delete_food(update_food_ch,item_sr_no)
                                        if status == False:
                                            print("\n********************** Something Went Wrong ******************\n")
                                            print(f_change_menu)

                                        else:
                                            print("\n****************** Item Deleted Succesfully *********************\n")
                                            print(f_change_menu)

                                elif update_food_ch =='4':  # delete beveage
                                    print("\n***** Existing Food Items In Beverages Category *****\n")
                                    app.display_food('2')
                                    print()
                                    item_sr_no = input("Enter Serial Number Of Product To Be Deleted: ")
                                    if (item_sr_no.isdigit() == False) or (int(item_sr_no) > len(app.beverages_new)) :
                                        print("\n********************* Invalid Choice **********************\n")
                                        print(f_change_menu)
                                    else:
                                        status = app.delete_food(update_food_ch,item_sr_no)
                                        if status == False:
                                            print("\n********************** Something Went Wrong ******************\n")
                                            print(f_change_menu)

                                        else:
                                            print("\n****************** Item Deleted Succesfully *********************\n")
                                            print(f_change_menu)

                                elif update_food_ch =='5':
                                    print(adm)
                                    break
                                else:
                                    print("\n**************** Invalid Option *********************\n") 
                        elif adm_ch == '5':
                            entry()
                            break
        elif e_ch == '3':
            print("\n************************ Thank You For Visiting TheOne Cinema ***********************\n")
            break
        else:
            print("\n******************* Invalid Option......Please Select Valid Option ********************\n")
            
