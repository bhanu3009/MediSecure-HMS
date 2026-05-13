no=int(input("Eneter how many members that are there :"))
final_name=[]
final_pro=[]
final_age=[]

for i in range (no):
    name=input("Enter your name :")
    age=input("Enter your age :")
    problem=input("Enter your problem :")
    final_name.append(name)
    final_age.append(age)
    final_pro.append(problem)

for i in range (no):
    if final_age[i]>=60:
        print("you are old onecs who had an problem of "+final_pro[i])
    elif final_age[i]<=18:
        print("You age is too short for the treatment to this "+final_pro+" problem.")
    else:
        print("You are eligible for the opertaion :")


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



