hi=[
    {
        "patient_name":"  BhanU ",
        "heart_rate": 78,
        "oxygen_level":66,
    },{
        "patient_name":"  rhanU ",
        "heart_rate":99,
        "oxygen_level":33,
    },{
        "patient_name":"  hhanU ",
        "heart_rate":55,
        "oxygen_level":88,
    },{
        "patient_name":"  phanU ",
        "heart_rate":66,
        "oxygen_level":80,
    },
]

def generate_shift_report(list_of_patients):
    with open("night_shift_alert.txt","w") as file:
        for i in list_of_patients:
            if i["oxygen_level"] < 92 or i["heart_rate"] > 100:
                clean=i["patient_name"].strip().title()
                alert=f"{clean} needs imediate mointiing because the heartrate is:{i['heart_rate']} and the oxygen_level is:{i['oxygen_level']}.\n" 
                file.write(alert)
    
    print("Success: night_shift_alert.txt has been generated!")

generate_shift_report(hi)