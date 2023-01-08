import re

l = [1,2,3,4,5,6,7,8,9]
a=[]
# for i in range (len(l)//3):
#     a.append([l[i],l[i+1],l[i+2]])
#     i=i+3

# print(a)

# i=0
# while i < len(l):
#     a.append([l[i],l[i+1],l[i+2]])
#     # print(a)
#     i=i+3
# print(a)

# a = "apple"
# d = ["a is ",' '*20,a]
# print(d)
# c = "".join(d)
# print(c)

# d = ['1','1','1','2','2','2','3','3','3','4','4','4','5','5','5']
# print(d)
# element_no = input("Enter The Element Number : ")
# index_of_element = (int(element_no)*2)+(-2 + (int(element_no) - 1))
# d.pop(index_of_element)
# d.pop(index_of_element)
# d.pop(index_of_element)
# print("Index Element is : ",index_of_element)
# print(d)

# d=[]
# if not d:
#     print("False")
#     print("There is nothing in d")
# else:
#     print("True")
#     print("There is something in d")


# i = [1,2,3,4,5,6,7,8,9]
# i.extend([1,2,3,4,5,6,7,8,9])
# i.extend([9,8,7,6,5,4,3,2,1])
# print(i)

# a= 'rohan is good'
# b = a.replace("rohan","sagar")
# print(b)


                # adm = "\n************************ Welcome Admin ***************************\n\nPress 1 : Update Staff\nPress 2 : Update Movie And Schedule\nPress 3 : Update Food Court\nPress 4 : Exit"
                # print(adm)
                # while True:
                #     print()
                #     adm_ch = input("Enter Your Choice : ") 
                #     if adm_ch.isdigit() == False or int(adm_ch) > 6 :
                #         print("\n********************* Invalid Input **********************\n")
                #     else:
                #         if adm_ch == '1':     # Update Staff
                #             print("\nPress 1 : View Staff Members\nPress 2 : Search Staff Member\nPress 3 : Add Staff Member\nPress 4 : Remove Staff Member\nPress 5 : Exit\n")
                            
                #         elif adm_ch == '2' :     # Update Movie And Schedule 
                #             print("\nPress 1 : Check Movie Schedule\nPress 2: Update Movie Schedule And Pricing\nPress 3 : Exit\n")
                #         elif adm_ch == '3' :     # Update Food Court
                #             print("\nPress 1 : Add Snack\nPress 2 : Delete Snack\nPress 3 : Add Beverage\nPress 4 : Delete Beverage\nPress 5 : Exit\n")
                #         elif adm_ch == '4':
                #             break
                #         else:
                #             print("\n****************** Invalid Option ********************\n")
                        
'''
with open(r"all_files\staff_info.txt","r")as file:
    data = file.readlines()
print(len(data))
id = 100
if len(data) == 1 :
    id = id + 1
else:
    last_emp = data[-1]
    last_emp_id = re.findall(r'\b\d{3,5}\b',''.join(data))
    print(last_emp_id)
    id = int(last_emp_id[0])
    id = id + 1
print(id)
'''















