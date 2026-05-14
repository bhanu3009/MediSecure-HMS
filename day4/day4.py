hospital_database = [
    {"name":"Aarav","age":12,"needs_urgent_care":True},
    {"name":"Bhanu","age":21,"needs_urgent_care":False},
    {"name":"Joy","age":16,"needs_urgent_care":False},
    {"name":"Durga","age":8,"needs_urgent_care":True}
]

def  get_urgent_pediatric_cases(patient_list):
    urgent_minors=[]

    for i in patient_list: 

        if i["age"] < 18 and i["needs_urgent_care"] == True:
            urgent_minors.append(i["name"])
    return urgent_minors

result=get_urgent_pediatric_cases(hospital_database)
print(result)