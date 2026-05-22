
class patient:
    def __init__(self,name,age,blood_group,issue):
        self.name=name
        self.age=age
        self.blood_group=blood_group
        self.issue=issue

class doctor:
    def __init__(self,name,specialization,consultation_fee):
        self.name=name
        self.specialization=specialization
        self.consultation_fee=consultation_fee

    def tretment(self,target_patient):
        print(f"🩺 Dr. {self.name} is treating patient {target_patient.name} for {target_patient.issue}.")

pat_no=int(input("Enter how many patients are there for the treatment :"))
doc_no=int(input("Enter how many doctors are there for the service :"))
final_patient_list=[]
for i in range(pat_no):
    pat_name=input("Enter your name :")
    age=int(input("Enter your age :"))
    blood_group=input("Enter your blood_group :")
    issue=input("Enter the isseues that you are facing :")
    pat=patient(pat_name,age,blood_group,issue)
    final_patient_list.append(pat)

final_doc_list=[]
for i in range(doc_no):
    doc_name=input("Enter your name :")
    specialization=input("Enter your specialization :")
    consultation_fee=input("Enter your consultation_fee :")
    doc=doctor(doc_name,specialization,consultation_fee)
    final_doc_list.append(doc)


print(f"\nThe final patients are: {final_patient_list}")
print(f"The final doctors are: {final_doc_list}\n")

attending_doctor = final_doc_list[0]

for i in final_patient_list:
    attending_doctor.tretment(i)