import requests
from datetime import datetime
class LabTechnician:
    def __init__(self,tech_id,name,hospital_base):
        self.tech_id=tech_id
        self.name=name
        self.hospital_base=hospital_base

def sync_lab_technicians():
    try:
        response=requests.get("https://jsonplaceholder.typicode.com/users")
        
        if response.status_code==200:
            data=response.json()
            authorized_techs=[]
            
            for i in data:
                technician_id=i.get("id")
                name=i.get("name","Unknown")
                cleaned_name=name.strip().title()
                hospital_base=i.get("company",{}).get("name","Unknown Base")
                new_tech=LabTechnician(technician_id,cleaned_name,hospital_base)
                authorized_techs.append(new_tech)
                print(f"Registered Tech #{new_tech.tech_id}:{new_tech.name}(Base:{new_tech.hospital_base})")
            
            with open("registry_sync_log.txt", "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}]-HTTP 200 OK-Successfully synced{len(authorized_techs)}technicians.\n")
            
            print(f"\nSync Complete! Loaded {len(authorized_techs)} technicians into the system.")
            return authorized_techs
            
        elif response.status_code==404:
            print("\033[91m Registry API Offline.\033[0m")
            
        else:
            print(f"Critical warning! Unhandled status code:{response.status_code}")
            return "Error !"
            
    except Exception as e:
        print(f"Critical error in the process! {e}")

if __name__ == "__main__":
    active_tech_roster = sync_lab_technicians()



    