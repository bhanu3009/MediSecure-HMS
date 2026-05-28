# no_count=int(input("hi enter the no of u came : "))
# if no_count < 0:
#     print("you are not eligible for ride")
# else:
#     print("you are for the ride !")

#     for no_count in range(no_count):
#         print('hiooo')

# name1="bhanu"
# name2="prakash"
# final=name1+"   "+name2
# print(final)

# name="bhanu prakash"
# age=10
# print("you age and name is : "+str(age)+" "+name)

# name="BHANU PRAKASH"
# age=10+1
# height=5.9
# hand_cap=False
# print("Welcome "+name+" and you age is :"+str(age) + "and the type of the age is :"+ type(name))

# name=input("Enter the name : ")
# age=int(input("Enter the age :"))
# height=float(input("Enter the height :"))
# patient=True
# gender=input("Enter you gender :")

# print("hello :"+name+" you age is :"+str(age)+"and your height is :"+str(height)+"and your gender is :"+gender)

# name=input("ENTER YOU NAME :")
# age=int(input("ENTER YOUR AGE :"))
# card=input("Do you have card ? y/n :")
# temp=False
# if card=="y":
#     temp=True
# if age<=18:
#     print("hello " +name+ " You are eligible because your are is :" +str(age))
# elif temp==True:
#     print("you are eleigible because you have card ....")
# else:
#     print("you are not eleigble because you dont have anything !")

# no_patients=int(input("Enter the no of members that are admitied :"))
# name_pat=[]
# for i in range (no_patients):
#    temp=input("Enter you "+str(i)+" patient name :")
#    name_pat.append(temp)

#    print(name_pat)


# no_patients=int(input("How many patients are been arrived now ? "))
# name_patients=[]
# age_patients=[]
# status_patients=[]

# for i in range(no_patients):
#    name=input("Enter you name :")
#    age=int(input("Enter you age :"))
#    name_patients.append(name)
#    age_patients.append(age)
#    if age<18:
#     status_patients.append("not eligible ")
#    elif age>=18 and age <=60:
#     status_patients.append(" eligible ")
#    else:
#     status_patients.append("not eligible. ")

# print("---Final report---")
# for i in range(no_patients):
#   print("Name :"+name_patients[i]+" is "+status_patients[i]+" because his/her age is :"+str(age_patients[i])+".")

# no=int(input("Eneter how many members that are there :"))
# final_name=[]
# final_pro=[]
# final_age=[]

# for i in range (no):
#     name=input("Enter your name :")
#     age=input("Enter your age :")
#     problem=input("Enter your problem :")
#     final_name.append(name)
#     final_age.append(age)
#     final_pro.append(problem)

# for i in range (no):
#     if final_age[i]>=60:
#         print("you are old onecs who had an problem of "+final_pro[i])
#     elif final_age[i]<=18:
#         print("You age is too short for the treatment to this "+final_pro+" problem.")
#     else:
#         print("You are eligible for the opertaion :")


# registration_attempts=3
# final_patient=[]

# while registration_attempts>0:
#     if registration_attempts==0:
#         break
#     name=input("Please enter the patient name :")
#     patient_age=int(input("Enter patient age :"))
#     is_emergency=input("is patient is in ememrgency ")

#     if is_emergency.lower()=="yes" or is_emergency.lower()=="y":
#         final_emergency=True
#     else:
#         final_emergency=False
#     if final_emergency==True:
#         print("Alert ! emergency need to go to the operation now.")
#         status ="Emergency alert !"
#         final_patient.append(name+"----"+status)
#         break
#     elif patient_age<=18 and final_emergency==False:
#         print("Please fill the form and need the signature of the guardian/parents. ")
#         signature=input("Are you willing to admit you child for the treatment.")
#         if signature.lower()=="yes" or signature.lower()=="y":
#             temp=True
#         else:
#             temp=False
#         if temp==True:
#             status="Minor Case(Approved)"
#             final_patient.append(name+"----"+status)
#         else:
#             print("please accept the guidliness and accept the conditons for the operation.")
#         registration_attempts=registration_attempts-1
#     elif patient_age>=18 and final_emergency==False:
#         print("patient is registered for standard consultation.")
#         status="Minor case"
#         final_patient.append(name+"----"+status)
#         break
#     else:
#         print("Thank You !")
# print(final_patient)


# def trial(name, age):
#     result="Welcome to the hosptail me :"+name+" and your age is :"+str(age)+"."
#     return result

# fin_1=trial("bhanu",20)
# print(fin_1)

# height=float(input("Enter you hight :"))
# weight=float(input("Enter you weight :"))

# def logic(height,weight):
#     bmi=weight/(height*height )
#     return bmi

# result=logic(height,weight)
# if result<=18:
#     print("you are undder risk which is not goood for your health due to you weight is :"+str(result))
# elif result>=18.5 and result<=24.5:
#     print ("Your health is good. ")
# elif result>=25.0:
#         print("you are over weighted.")

# print(result)


# donar_blood=input("What is the blood group of your blood :")
# reciver_blood="o+"
# def check(donar_blood,reciver_blood="o+"):
#     if reciver_blood.lower==donar_blood.lower:
#         return True
#     else:
#         return False
    
# result=check(donar_blood,reciver_blood)
# if result==True:
#     print("We found the donar")
# else:
#     print("sorry we dint found the donar.")


# def screen_patient(name, age, height,weight):
#     bmi=weight/(height*height)
#     if bmi<18.0:
#         empty="under weight"
#     elif bmi>=18.5 and bmi<24.5:
#         empty="normal"
#     else:
#         empty="Over weight"

#     report_string="patient "+name+" as an bmi "+str(bmi)+" which is "+str(empty)+"."
#     return report_string

# final_reports=[]
# no=int(input("How many patients are there for the bmi :"))
# for i in range (no):
#     print("Enter the "+str(i+1)+" detials.")
#     name=input("Enter your name :")
#     age=int(input("Enter your age :"))
#     weight=float(input("Enter you weight :"))
#     height=float(input("Enter you height :"))
#     result=screen_patient(name,age,height,weight)
#     final_reports.append(result)

# for i in range (no):
#     print(""+str(i+1)+". "+str(final_reports[i]))

 

# hi=[
#     {
#         "name":"bhanu",
#         "age":21,
#         "height":5.9,
#         "patient":False,
#         },{
#         "name":"jhanu",
#         "age":21,
#         "height":5.9,
#         "patient":False,
#     },]
# print("yoiuoy"+str(hi[1]))

# name="bhanu prakash"
# age=10
# height=5.8
# rich=False
# print(f"Welcome {name}. Your age is {age} and your height is {height}. with these qulfiactions you will be {rich}")
# print(f"{name.capitalize()} welcome to bank of borada in the age of :{age} you are been ")


# raw_name = "   bHAnu pRAkaSh   "
# account_balance = 15450.75
# clean_name = raw_name.strip().title()
# receipt_text = f"""
# ================================
#        SECUREBANK RECEIPT
# ================================
# Account Holder: {clean_name}
# Current Balance: Rs {account_balance}
# Status: Active
# ================================
# """
# file_name = "bhanu_statement.txt"
# with open(file_name, "w") as file:
#     file.write(receipt_text)
    
# # print(f"Success! I just generated '{file_name}' and saved it to your folder.")

# password=input("Enter the password :")
# with open("password.txt","w") as file:
#     file.write(password+"\n")
#     print("success")

# update=input("Enter the phone no that you want to change :")
# with open("password.txt","a") as file:
#     file.write(update+"\n")
#     print("Successfully appended ")

# with open ("password.txt","r") as file:
#     result=file.read()
#     print("Scuucessfully opened.")

# print(result)

# name==input("Enter the name :")
# age=input("Enter the age :")
# height=input("Enter the height :")
# rich=False

# with open("new.txt","w")as file:
#     file.write()

# test="   jOhN dOe, bLooD tYpE o+   "
# print("plain text :"+test)
# print("after removing the spaces :"+test.strip())
# print("after adding captails :"+test.capitalize())
# print("after making them to lower :"+test.lower())
# print("after making them to upper :"+test.upper())
# print("after making them to split :",test.split())


# name=input("Enter the name :")
# age=input("Enter the age :")
# height=input("Enter the height :")
# rich=False
# with open("new.txt","w")as file:
#     file.write(name+"\n")
#     file.write(age+"\n")
#     print("Succesfully wrote the file.")

# # with open("new.txt","a") as file:
# #     file.write(height+"\n")
# #     print("Appended sucessuffuly.")

# # with open("new.txt","r") as file:
# #     result=file.read()

# # print(result)

# # hi=[
# #     {
# #         "patient_name":" bHaHu  ",
# #         "heart_rate":"bad",
# #         "oxygen_level":" 7758  ",
# #     },{
# #         "patient_name":" jHbHu  ",
# #         "heart_rate":"good",
# #         "oxygen_level":" 7078  ",
# #     },{
# #         "patient_name":" HaHu  ",
# #         "heart_rate":"good",
# #         "oxygen_level":" 9778  ",
# #     }
# # ]

# # def generate_shift_report(patients){
# #     test=patients
# #     text="night_shift_alert.txt"
# # for i in patients:
# #     if i["oxygen_level"]<"92" or i["oxygen_level"]>"100":
# #         result=i.["patient_name"]
# #         fin=result.strip().upper().split()
# #         print(f"[fin] requires immediate monitoring. Vitals: HR [], O2 [oxygen_level].")
# # }

# # hello=generate_shift_report(hi)
# # print(hello)



# hi=[
#     {
#         "patient_name":" bHaHu  ",
#         "heart_rate":"bad",
#         "oxygen_level":" 7758  ",
#     },{
#         "patient_name":" jHbHu  ",
#         "heart_rate":"good",
#         "oxygen_level":" 7078  ",
#     },{
#         "patient_name":" HaHu  ",
#         "heart_rate":"good",
#         "oxygen_level":" 9778  ",
#     }
# ]

# byee=[
#     {
#         "patient_name":" poiubHaHu  ",
#         "heart_rate":"bad",
#         "oxygen_level":" 7758  ",
#     },{
#         "patient_name":" jHbHu  ",
#         "heart_rate":"good",
#         "oxygen_level":" 7078  ",
#     },{
#         "patient_name":" HaHu  ",
#         "heart_rate":"good",
#         "oxygen_level":" 9778  ",
#     }
# ]

# for i in hi:
#    result=i["patient_name"]
#    print(result)

# print(hi[1]["patient_name"])

# print(tam)




# hi=[
#     {
#         "patient_name":"  BhanU ",
#         "heart_rate": 78,
#         "oxygen_level":66,
#     },{
#         "patient_name":"  rhanU ",
#         "heart_rate":99,
#         "oxygen_level":33,
#     },{
#         "patient_name":"  hhanU ",
#         "heart_rate":55,
#         "oxygen_level":88,
#     },{
#         "patient_name":"  phanU ",
#         "heart_rate":66,
#         "oxygen_level":80,
#     },
# ]

# def generate_shift_report(list_of_patients):
#     with open("night_shift_alert.txt","w") as file:
#         for i in list_of_patients:
#             if i["oxygen_level"] < 92 or i["heart_rate"] > 100:
#                 clean=i["patient_name"].strip().title()
#                 alert=f"{clean} needs imediate mointiing because the heartrate is:{i['heart_rate']} and the oxygen_level is:{i['oxygen_level']}.\n" 
#                 file.write(alert)
    
#     print("Success: night_shift_alert.txt has been generated!")
# generate_shift_report(hi)

# print("try catch error :")
# try:
#     no=int(input("Enter the no that you want to div :"))
#     div=int(input("Enter the no that you want to diviable with :"))
#     result=no/div
#     print(result)
# except ZeroDivisionError:
#     print("you are getting an error :")
# finally:
#     print("You have successfully divided.")

# import datetime
# now=datetime.datetimenow()
# print(now)
# reult=now.strftime()

# import os
# import random
# import datetime
# print("otp generator !")
# otp=random.randint(10000,99999)
# print(f"your otp is {otp}")
# result=int(input("Enter the otp :"))
# if result!=otp:
#     print("Your otp is invalied !")
# else:
#     print("your otp is correct.")
#     print("the transaction is been done at ",datetime.datetime.now())


# name=input("Enter the name :")
# age=input("Enter the age :")
# height=input("Enter the height :")
# rich=False
# with open("new.txt","w")as file:
#     file.write(name+"\n")
#     file.write(age+"\n")
#     print("Succesfully wrote the file.")

# # with open("new.txt","a") as file:
# #     file.write(height+"\n")
# #     print("Appended sucessuffuly.")

# # with open("new.txt","r") as file:
# #     result=file.read()

# # print(result)


# import datetime
# name=input("Enter the name :")
# age=input("Enter the age :")
# blood_type=input("Enter the blood type :")
# rich=False
# with open("new_patients.txt","w")as file:
#     file.write(name+"\n")
#     file.write(age+"\n")
#     file.write(blood_type+"\n")
#     print("Succesfully wrote in the file. ")

# def process_patient_batch(x):
#     successful_records=[]
#     with open("new_patients.txt","r") as file:
#         for i in x:
#             last_name=name.capitalize().split().title()
#             last_age=age.capitalize().split().title()
#             last_blood=blood_type.capitalize().split().title()
#             try:
                

# import datetime

# def process_patient_batch():
#     successful_records = []
    
#     print("--- Starting Batch Processor ---")
    
#     with open("new_patients.txt", "r") as file:
#         for line in file:
#             data_parts = line.strip().split(",")
            
#             if len(data_parts) != 3:
#                 continue
                
#             name = data_parts[0]
#             raw_age = data_parts[1]
#             blood_type = data_parts[2]
            
#             try:
#                 clean_age = int(raw_age)
#             except ValueError:
#                 print(f"⚠️ SKIPPED: Record for '{name}' contains an invalid age ('{raw_age}').")
#                 continue
                
#             patient_data = {
#                 "patient_name": name,
#                 "age": clean_age,
#                 "blood_type": blood_type
#             }
            
#             successful_records.append(patient_data)
#             print(f"✅ SUCCESS: {name} added to the system.")
            
#     now = datetime.datetime.now().strftime("%I:%M %p")
#     return f"Batch Complete at {now}. Successfully processed {len(successful_records)} records."

# final_report = process_patient_batch()
# print("\n" + final_report)



# hi=[
#     {
#         "name":"jhanu", 
#         "age":70, 
#         "blood_group":"o+",
#         "is_active":True,
#     },{
#         "name":"bhanu", 
#         "age":80, 
#         "blood_group":"a+",
#         "is_active":True,
#     },{
#         "name":"phanu", 
#         "age":50, 
#         "blood_group":"o-",
#         "is_active":True,
#     },{
#         "name":"thanu", 
#         "age":60, 
#         "blood_group":"ab-",
#         "is_active":True,
#     },{
#         "name":"mhanu", 
#         "age":30, 
#         "blood_group":"b+",
#         "is_active":True,
#     },
# ]

# def process_senior_admissions(patient_list):
#     try:
#         for i in patient_list:
#             raw_age=i["age"]
#             raw_status=i["is_active"]
#             try:
#                 clean_age=int(raw_age)
#                 if clean_age >60 and raw_status==True:
#                     result=f"the addmited patient name is :{i['name']} and the age is {i['age']}."
#                     with open ("senior_patients.txt","a")as file:
#                         file.write(result+"\n")
#                         print("succesfully appended")
#             except ValueError:
#                 print("you got an error !")
#     except Exception as e:
#         print("critical error !{e}")
    
# process_senior_admissions(hi)


# class book:
#     def __init__(self,tittle,author,page_count):
#         self.tittle=tittle
#         self.author=author
#         self.page_count=page_count

#     def info(self):
#         print(f"The name of the book is {self.tittle}. The authour is {self.author} and the no of pages is :{self.page_count}.")

#     def byee():
#         print("im from the byee :")


# one=book("bahubail","rajamouli",100000)
# one.info()
# two=book("raka","atteli",10000000)
# two.info()

# class patient:
#     def __init__(self,name,age,blood_group,issue):
#         self.name=name
#         self.age=age
#         self.blood_group=blood_group
#         self.issue=issue

# class doctor:
#     def __init__(self,name,specialization,consultation_fee):
#         self.name=name
#         self.specialization=specialization
#         self.consultation_fee=consultation_fee

#     def tretment(self,target_patient):
#         print(f"🩺 Dr. {self.name} is treating patient {target_patient.name} for {target_patient.issue}.")

# pat_no=int(input("Enter how many patients are there for the treatment :"))
# doc_no=int(input("Enter how many doctors are there for the service :"))
# final_patient_list=[]
# for i in range(pat_no):
#     pat_name=input("Enter your name :")
#     age=int(input("Enter your age :"))
#     blood_group=input("Enter your blood_group :")
#     issue=input("Enter the isseues that you are facing :")
#     pat=patient(pat_name,age,blood_group,issue)
#     final_patient_list.append(pat)

# final_doc_list=[]
# for i in range(doc_no):
#     doc_name=input("Enter your name :")
#     specialization=input("Enter your specialization :")
#     consultation_fee=input("Enter your consultation_fee :")
#     doc=doctor(doc_name,specialization,consultation_fee)
#     final_doc_list.append(doc)


# print(f"\nThe final patients are: {final_patient_list}")
# print(f"The final doctors are: {final_doc_list}\n")

# attending_doctor = final_doc_list[0]

# for i in final_patient_list:
#     attending_doctor.tretment(i)

# import json
# hi ={
#         "name":"Bhanu",
#         "age":21,
#         "height":3.1,
#         "Weight":55,
#         "employee":None
#     }
# bye='{"name":"jhanu","age":61, "height":6.1,"Weight":5.5,"employee":null,"income":false}'
# result=json.loads(bye)
# print(type(result))
# # hi=json.dumps(hi)
# print(type(hi))


# import json
# import requests
# final=requests.get('https://jsonplaceholder.typicode.com/users')
# temp=final.json()
# print(temp)


# import requests
# import json
# class patient:
#     def __init__(self,name,email,city):
#         self.name=name
#         self.email=email
#         self.city=city

# def sync_external_patients():
#     try:
#         temp=requests.get('jsonplaceholder.typicode.com/users')
#         temp3=temp.json()
#         print("successfuly imported the things ")

#         successfully_imported=[];
#         for i in temp3:
#             try:
#                 raw_name=i["name"]
#                 raw_email=i["email"].lower()
#                 raw_city=i["city"]["address"]
        
#                 if " " in raw_name:
#                     new_patient=patient(raw_name,raw_email,raw_city)
#                     successfully_imported.append(new_patient)
#             except Exception as e:
#                 print(f"Skipping a user due to missing data: {e}")

#         temp_1=[0]
#         for i in successfully_imported:
#             strcutured={
#                 "patient_name":i.name,
#                 "contact":i.email,
#                 "location":i.city
#                 }
#             temp_1.append(strcutured)

#             temp2=json.dump(temp_1,index=3)

#             with open("good_json_file.json","w") as file:
#                 file.write(temp2)
#                 print("Successfully appended the file .")

#     except requests.exceptions.RequestException as e:
#                 print(f"Network Error: Could not connect to the API. {e}")
#     except Exception as e:
#                 print(f"Critical System Error: {e}")

# sync_external_patients()

# import time 
# print("start.")
# def test(name):
#     print(name)
#     time.sleep(1)
#     print("-------")

# test("Bhanu")
# test("jhanu")
# test("hhanu")
# test("phanu")
# test("thanu")
# test("mhanu")

# import asyncio
# async def kfc():
#     print("Your kfc is getting ready.")
#     await asyncio.sleep(10)
#     print("on the way.")
#     return "kfc ready!"

# async def biryan():
#     print("Your brirayan is getting ready.")
#     await asyncio.sleep(5)
#     print("on the way.")
#     return "biriyan ready!"

# async def cold_drinks():
#     print("Your drink is getting ready.")
#     await asyncio.sleep(2)
#     print("on the way.")
#     return "drink ready!"

# async def main():
#     print("foo ordering !")
#     result=await asyncio.gather(cold_drinks(),kfc(),biryan())
#     return result

# async def dining():
#     print("dining as been started.")
#     order=await main()
#     print(f"Here is your oreder menu :{order}")

# asyncio.run(dining())
  

# import asyncio
# import json
# class Patient():
#     def __init__(self,patient_id, name, insurance_status):
#         self.patient_id=patient_id
#         self.name=name 
#         self.insurance_status=insurance_status

# async def fetch_internal_db():
#     print(f"The process has been started.")
#     await asyncio.sleep(3)
#     return[
#         {
#             "patient_id":1001,
#             "name":"bhanu",
#             "insurance_status":True,
#         },{
#             "patient_id":2001,
#             "name":"priya",
#             "insurance_status":False,
#         },{
#             "patient_id":3001,
#             "name":"Sathish",
#             "insurance_status":True,
#         },
#     ]

# async def fetch_insurance_api():
#     print(f"Another process started.")
#     await asyncio.sleep(3)
#     raw_json='[{"patient_id":4001,"name":"durga","insurance_status":false},{"patient_id":5001,"name":"jhanu","insurance_status":true}]'
#     result=json.loads(raw_json)
#     return result

# async def compile_hospital_records():

#     db_results,api_results=await asyncio.gather(fetch_internal_db(),fetch_insurance_api())
#     comibined_list=db_results+api_results

#     verified_patients=[]
#     for i in comibined_list:
#         try:
#             if i["insurance_status"]==True:
#                 new_pat=Patient(i["patient_id"],i["name"],i["insurance_status"])
#                 verified_patients.append(new_pat)
#         except Exception as e:
#             print(f"you got an error {e}")


#     final_list=[]
#     for obj in verified_patients:
#         standard_dict={
#             "patient_id":obj.patient_id,
#             "name":obj.name,
#             "insurance_status":obj.insurance_status
#         }
#         final_list.append(standard_dict)

#     formatted_json_string=json.dumps(final_list,indent=4)
#     with open("verified_admissions.json","w")as file:
#         file.write(formatted_json_string+"\n")
#         print("\n✅ Successfully saved verified_admissions.json!")

# asyncio.run(compile_hospital_records())

# import requests

# URL="https://jsonplaceholder.typicode.com"
# def get():
#     print("step 1:---------")
#     print("Fetching data...........")
#     responce=requests.get(f"{URL}/users/1")
#     if responce.status_code==200:
#         data=responce.json()
#         print(f"Successfully converted the data into dictornary.")
#     else:
#         print(f"you got an error :{responce.status_code}")

# def post():
#     print("Step 2:-------------")
#     print("creating data_---------")
#     data_patient={
#         "name":"Bhanu",
#         "age":44,
#         "height":4.3,
#         "status":True
#     }
#     responce=requests.post(f"{URL}/users/1",json=data_patient)
#     if responce.status_code==201:
#         data=responce.json()
#         print(f"✅ Success! Record updated. New Name: {data['name']}")
#     else:
#         print(f"Got an error in {responce.status_code}")

# def put():
#     print("Step 3:-------------")
#     print("Updating data_---------")
#     updated_data={
#         "name":"Bhanu Prakash (Updated)",
#         "status":"Ready for Discharge"
#     }
#     responce=requests.put(f"{URL}/users/1",updated_data)
#     if responce.status_code == 201:
#         data=responce.json()
#         print(f"Success! Record updated. New Name: {data['name']}")
#     else:
#         print(f"Failed. Kitchen sent Error Code: {responce.status_code}")

# def delete():
#     print("Step 4:-------------")
#     print("Delete data_---------")
#     responce=requests.delete(f"{URL}/users/1")
#     if responce.status_code in [200,204]:
#         print(f"Success! Patient record completely erased from database.")
#     else:
#         print(f"Failed. Kitchen sent Error Code: {responce.status_code}")

# if __name__ == "__main__":
#     print("🚀 Booting up API Network Pipeline...")
#     get()
#     post()
#     put()
#     delete()
#     print("\n🏁 All network operations completed safely!")



# import requests
# URL="https://jsonplaceholder.typicode.com/posts"

# responce=requests.get(URL)

# if requests.status_codes==200:
#     data=responce.json()
#     print(f"You data is :{data}")
# else:
#     print(f"u got an error !{responce.status_code}")

# class LabTechnician ():
#     def __init__(self,tech_id,name,hospital_base):
#         self.tech_id=tech_id
#         self.name=name
#         self.hospital_base=hospital_base

# def sync_lab_technicians():
#     try:
#         responce=requests.get("https://jsonplaceholder.typicode.com/users")
#         if responce==200:
#             data=responce.json()
#             authorized_techs=[]
#             for i in data:
#                 technician_id=i.get("id")
#                 name=i.get("name")
#                 cleaned_name=name.strip().title()
#                 hospital_base = user.get("company",{}).get("name","Unknown Base")

#         elif responce==404:
#             print("Registry API Offline.")
#         else:
#             print(f"Critical warining !")
#             return "Error !"
#     except as except (e):
#         print(f"Critical error in the process !{e}")



# import requests
# from datetime import datetime
# class LabTechnician:
#     def __init__(self,tech_id,name,hospital_base):
#         self.tech_id=tech_id
#         self.name=name
#         self.hospital_base=hospital_base

# def sync_lab_technicians():
#     try:
#         response=requests.get("https://jsonplaceholder.typicode.com/users")
        
#         if response.status_code==200:
#             data=response.json()
#             authorized_techs=[]
            
#             for i in data:
#                 technician_id=i.get("id")
#                 name=i.get("name","Unknown")
#                 cleaned_name=name.strip().title()
#                 hospital_base=i.get("company",{}).get("name","Unknown Base")
#                 new_tech=LabTechnician(technician_id,cleaned_name,hospital_base)
#                 authorized_techs.append(new_tech)
#                 print(f"Registered Tech #{new_tech.tech_id}:{new_tech.name}(Base:{new_tech.hospital_base})")
            
#             with open("registry_sync_log.txt", "a") as file:
#                 timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 file.write(f"[{timestamp}]-HTTP 200 OK-Successfully synced{len(authorized_techs)}technicians.\n")
            
#             print(f"\nSync Complete! Loaded {len(authorized_techs)} technicians into the system.")
#             return authorized_techs
            
#         elif response.status_code == 404:
#             print("\033[91m🚨 Registry API Offline.\033[0m")
            
#         else:
#             print(f"Critical warning! Unhandled status code:{response.status_code}")
#             return "Error !"
            
#     except Exception as e:
#         print(f"Critical error in the process! {e}")

# if __name__ == "__main__":
#     active_tech_roster = sync_lab_technicians()



    