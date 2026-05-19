
hi=[
    {
        "name":"jhanu", 
        "age":70, 
        "blood_group":"o+",
        "is_active":True,
    },{
        "name":"bhanu", 
        "age":80, 
        "blood_group":"a+",
        "is_active":True,
    },{
        "name":"phanu", 
        "age":50, 
        "blood_group":"o-",
        "is_active":True,
    },{
        "name":"thanu", 
        "age":60, 
        "blood_group":"ab-",
        "is_active":True,
    },{
        "name":"mhanu", 
        "age":30, 
        "blood_group":"b+",
        "is_active":True,
    },
]

def process_senior_admissions(patient_list):
    try:
        for i in patient_list:
            raw_age=i["age"]
            raw_status=i["is_active"]
            try:
                clean_age=int(raw_age)
                if clean_age >60 and raw_status==True:
                    result=f"the addmited patient name is :{i['name']} and the age is {i['age']}."
                    with open ("senior_patients.txt","a")as file:
                        file.write(result+"\n")
                        print("succesfully appended")
            except ValueError:
                print("you got an error !")
    except Exception as e:
        print("critical error !{e}")
    
process_senior_admissions(hi)