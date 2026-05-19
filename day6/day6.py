import datetime

def process_patient_batch():
    successful_records = []
    
    print("--- Starting Batch Processor ---")
    
    with open("new_patients.txt", "r") as file:
        for line in file:
            data_parts = line.strip().split(",")
            
            if len(data_parts) != 3:
                continue
                
            name = data_parts[0]
            raw_age = data_parts[1]
            blood_type = data_parts[2]
            
            try:
                clean_age = int(raw_age)
            except ValueError:
                print(f"⚠️ SKIPPED: Record for '{name}' contains an invalid age ('{raw_age}').")
                continue
                
            patient_data = {
                "patient_name": name,
                "age": clean_age,
                "blood_type": blood_type
            }
            
            successful_records.append(patient_data)
            print(f"✅ SUCCESS: {name} added to the system.")
            
    now = datetime.datetime.now().strftime("%I:%M %p")
    return f"Batch Complete at {now}. Successfully processed {len(successful_records)} records."

final_report = process_patient_batch()
print("\n" + final_report)