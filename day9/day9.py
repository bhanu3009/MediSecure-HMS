import requests
import json
class patient:
    def __init__(self,name,email,city):
        self.name=name
        self.email=email
        self.city=city

def sync_external_patients():
    try:
        temp=requests.get('jsonplaceholder.typicode.com/users')
        temp3=temp.json()
        print("successfuly imported the things ")

        successfully_imported=[];
        for i in temp3:
            try:
                raw_name=i["name"]
                raw_email=i["email"].lower()
                raw_city=i["city"]["address"]
        
                if " " in raw_name:
                    new_patient=patient(raw_name,raw_email,raw_city)
                    successfully_imported.append(new_patient)
            except Exception as e:
                print(f"Skipping a user due to missing data:{e}")

        temp_1=[0]
        for i in successfully_imported:
            strcutured={
                "patient_name":i.name,
                "contact":i.email,
                "location":i.city
                }
            temp_1.append(strcutured)

            temp2=json.dump(temp_1,index=3)

            with open("good_json_file.json","w") as file:
                file.write(temp2)
                print("Successfully appended the file .")

    except requests.exceptions.RequestException as e:
                print(f"Network Error: Could not connect to the API. {e}")
    except Exception as e:
                print(f"Critical System Error: {e}")

sync_external_patients()
