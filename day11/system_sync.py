# import asyncio
# import json
# raw_json="""[
# {
#         "name": "bhanu",
#         "heart_rate": 72,
#         "status": "Stable"
#     },
#     {
#         "name": "priya",
#         "status": "Critical"
#     },
#     {
#         "name": "Sathish",
#         "heart_rate": 98,
#         "status": "In Treatment"
#     }]"""
# temp1=json.dumps(raw_json)
# with open("local_ward_data.json","w")as file:
#     file.write(temp1+"\n")
#     print("successfully done the written !")

# class PatientRecord():
#     def __init__(self,name,heart_rate,status):
#         self.name:name
#         self.heart_rate=heart_rate
#         self.status=status

# async def fetch_local_ward():
#     await asyncio.sleep(1)
#     with open("local_ward_data.json", "r") as file:
#         file_content=file.read()
#     patient_list=json.loads(file_content)
#     print("📁 Local ward data successfully loaded!")

# async def fetch_icu_api():
#     await asyncio.sleep(2)
#     hardcoded_list=[
#         {
#             "name": "durga",
#             "heart_rate": 130,  
#             "status": "Critical"
#         },
#         {
#             "name": "jhanu",
#             "heart_rate": 78,
#             "status": "Stable"
#         }
#     ]
#     return hardcoded_list

# master_list=[]
# async def compile_hospital_state():
#     local_results,icu_results=await asyncio.gather(fetch_local_ward(),fetch_icu_api())
#     master_list=local_results+icu_results
#     for i in master_patient_list:
#         print(f"Processing raw data for: {i.get('name')}")
#         try:
#             new_record=PatientRecord(
#                 name=i["name"],
#                 heart_rate=i["heart_rate"],
#                 status=i["status"]
#             )
#             cleaned_name=new_record.name.strip()
#             master_list.append(cleaned_name)
#             print(f"Successfully processed record for: {new_record.name}")
#             if new_record.heart_rate>120 or new_record.heart_rate<60:
#                 print(Fore.RED+Style.BRIGHT+f"CRITICAL ALERT: {cleaned_name} requires immediate intervention! (BPM: {new_record.heart_rate})")
#             else:
#                 corrupted_name=patient_data.get('name', 'Unknown').strip()
#                 print(Fore.YELLOW + Style.BRIGHT + f"WARNING: Skipping corrupted record for '{corrupted_name}' due to missing key: {e}")
#             continue
#         except KeyError as e:
#             print(f"WARNING: Skipping corrupted record for '{patient_data.get('name', 'Unknown')}' due to missing key:{e}")
#             continue

#     print(f"\nProcessing complete. Valid objects instantiated: {len(master_list)}")
#     return master_list

# if __name__ == "__main__":
#     asyncio.run(compile_hospital_state())




# ----------------------  AI DID THIS CODE -------------------

import asyncio
import json
import colorama
from colorama import Fore, Style

# Initialize colorama auto-reset
colorama.init(autoreset=True)

raw_json = """[
{
        "name": "bhanu",
        "heart_rate": 72,
        "status": "Stable"
    },
    {
        "name": "priya",
        "status": "Critical"
    },
    {
        "name": "Sathish",
        "heart_rate": 98,
        "status": "In Treatment"
    }]"""

# FIX 1: Use json.loads() here to parse the text before dumping into a file
temp1 = json.loads(raw_json)
with open("local_ward_data.json", "w") as file:
    json.dump(temp1, file, indent=4)
    print("successfully done the written !")


class PatientRecord:
    def __init__(self, name, heart_rate, status):
        # FIX 2: Fixed assignment operator (= instead of :)
        self.name = name
        self.heart_rate = heart_rate
        self.status = status


async def fetch_local_ward():
    await asyncio.sleep(1)
    with open("local_ward_data.json", "r") as file:
        file_content = file.read()
    patient_list = json.loads(file_content)
    print("📁 Local ward data successfully loaded!")
    return patient_list  # FIX 3: Added missing return statement


async def fetch_icu_api():
    await asyncio.sleep(2)
    hardcoded_list = [
        {
            "name": "durga",
            "heart_rate": 130,  
            "status": "Critical"
        },
        {
            "name": "jhanu",
            "heart_rate": 78,
            "status": "Stable"
        }
    ]
    return hardcoded_list

async def compile_hospital_state():
    print("🚀 Running compilation sequence...\n")
    local_results, icu_results = await asyncio.gather(fetch_local_ward(), fetch_icu_api())
    
    # Combined cleanly
    master_list = local_results + icu_results
    
    # FIX 5: Separate list to cleanly store our valid objects
    valid_records = []
    
    # FIX 4: Looping through the correct master_list variable
    for i in master_list:
        try:
            new_record = PatientRecord(
                name=i["name"],
                heart_rate=i["heart_rate"],
                status=i["status"]
            )
            
            cleaned_name = new_record.name.strip()
            valid_records.append(new_record) # Saving the Object structure
            print(f"Processing raw data for: {cleaned_name}")
            
            if new_record.heart_rate > 120 or new_record.heart_rate < 60:
                print(Fore.RED + Style.BRIGHT + f"🚨 CRITICAL ALERT: {cleaned_name} requires immediate intervention! (BPM: {new_record.heart_rate})")
            else:
                # FIX 6: Print standard healthy tracker message instead of corruption text
                print(Fore.GREEN + f"✅ Normal Track: {cleaned_name} is stable. (BPM: {new_record.heart_rate})")
                
        except KeyError as e:
            # FIX 7: Used variable 'i' instead of undefined 'patient_data'
            corrupted_name = i.get('name', 'Unknown').strip()
            print(Fore.YELLOW + Style.BRIGHT + f"⚠️  WARNING: Skipping corrupted record for '{corrupted_name}' due to missing key: {e}")
            continue

    print(f"\nProcessing complete. Valid objects instantiated: {len(valid_records)}")
    return valid_records


if __name__ == "__main__":
    asyncio.run(compile_hospital_state())