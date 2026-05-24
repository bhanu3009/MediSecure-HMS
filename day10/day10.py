import asyncio
import json
class Patient():
    def __init__(self,patient_id, name, insurance_status):
        self.patient_id=patient_id
        self.name=name 
        self.insurance_status=insurance_status

async def fetch_internal_db():
    print(f"The process has been started.")
    await asyncio.sleep(3)
    return[
        {
            "patient_id":1001,
            "name":"bhanu",
            "insurance_status":True,
        },{
            "patient_id":2001,
            "name":"priya",
            "insurance_status":False,
        },{
            "patient_id":3001,
            "name":"Sathish",
            "insurance_status":True,
        },
    ]

async def fetch_insurance_api():
    print(f"Another process started.")
    await asyncio.sleep(3)
    raw_json='[{"patient_id":4001,"name":"durga","insurance_status":false},{"patient_id":5001,"name":"jhanu","insurance_status":true}]'
    result=json.loads(raw_json)
    return result

async def compile_hospital_records():

    db_results,api_results=await asyncio.gather(fetch_internal_db(),fetch_insurance_api())
    comibined_list=db_results+api_results

    verified_patients=[]
    for i in comibined_list:
        try:
            if i["insurance_status"]==True:
                new_pat=Patient(i["patient_id"],i["name"],i["insurance_status"])
                verified_patients.append(new_pat)
        except Exception as e:
            print(f"you got an error {e}")


    final_list=[]
    for obj in verified_patients:
        standard_dict={
            "patient_id":obj.patient_id,
            "name":obj.name,
            "insurance_status":obj.insurance_status
        }
        final_list.append(standard_dict)

    formatted_json_string=json.dumps(final_list,indent=4)
    with open("verified_admissions.json","w")as file:
        file.write(formatted_json_string+"\n")
        print("\n✅ Successfully saved verified_admissions.json!")

asyncio.run(compile_hospital_records())

