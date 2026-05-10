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


registration_attempts=3
final_patient=[]

while registration_attempts>0:
    if registration_attempts==0:
        break
    name=input("Please enter the patient name :")
    patient_age=int(input("Enter patient age :"))
    is_emergency=input("is patient is in ememrgency ")

    if is_emergency.lower()=="yes" or is_emergency.lower()=="y":
        final_emergency=True
    else:
        final_emergency=False
    if final_emergency==True:
        print("Alert ! emergency need to go to the operation now.")
        status ="Emergency alert !"
        final_patient.append(name+"----"+status)
        break
    elif patient_age<=18 and final_emergency==False:
        print("Please fill the form and need the signature of the guardian/parents. ")
        signature=input("Are you willing to admit you child for the treatment.")
        if signature.lower()=="yes" or signature.lower()=="y":
            temp=True
        else:
            temp=False
        if temp==True:
            status="Minor Case(Approved)"
            final_patient.append(name+"----"+status)
        else:
            print("please accept the guidliness and accept the conditons for the operation.")
        registration_attempts=registration_attempts-1
    elif patient_age>=18 and final_emergency==False:
        print("patient is registered for standard consultation.")
        status="Minor case"
        final_patient.append(name+"----"+status)
        break
    else:
        print("Thank You !")


print(final_patient)


