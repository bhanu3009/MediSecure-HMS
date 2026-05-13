
def screen_patient(name, age, height,weight):
    bmi=weight/(height*height)
    if bmi<18.0:
        empty="under weight"
    elif bmi>=18.5 and bmi<24.5:
        empty="normal"
    else:
        empty="Over weight"

    report_string="patient "+name+" as an bmi "+str(bmi)+" which is "+str(empty)+". At this age :"+age
    return report_string

final_reports=[]
no=int(input("How many patients are there for the bmi :"))
for i in range (no):
    print("Enter the "+str(i+1)+" detials.")
    name=input("Enter your name :")
    age=int(input("Enter your age :"))
    weight=float(input("Enter you weight :"))
    height=float(input("Enter you height :"))
    result=screen_patient(name,age,height,weight)
    final_reports.append(result)

for i in range (no):
    print(""+str(i+1)+". "+str(final_reports[i]))