import requests

AZKABAN_URL = "Your_azkaban_URL" #http://15.223.192.1209:1279/
USERNAME = "username"  
PASSWORD = "password"  
PROJECT_NAME = "PROJECT_NAME"  #The Azkaban Flow you want to run  
FLOW_NAME = "FLOW_NAME"    #the name of flow in you azkaban project  


CRON_EXPRESSION = "YOUR_CRON_JOB" #Cron job: you can schedule a job manually and find how your expression should look  

def login_to_azkaban():
    
    login_url = f"{AZKABAN_URL}/"
    payload = {
        "action": "login",
        "username": USERNAME,
        "password": PASSWORD,
    }
    response = requests.post(login_url, data=payload)
    response.raise_for_status()
    session_id = response.json().get("session.id")
    if not session_id:
        raise Exception("Failed to obtain session ID.")
    return session_id

def create_cron_schedule(session_id, cron_expression):
    
    schedule_url = f"{AZKABAN_URL}schedule"
    params = {
        "session.id": session_id,
        "ajax": "scheduleCronFlow",
        "projectName": PROJECT_NAME,
        "flow": FLOW_NAME,
        "cronExpression": CRON_EXPRESSION,
        "is_recurring": "true",
    }
    response = requests.get(schedule_url, params=params)
    response.raise_for_status()
    response_data = response.json()
    if response_data.get("status") != "success":
        raise Exception(f"Failed to create schedule: {response.text}")
    print(f"Cron schedule created successfully with expression: {cron_expression}")

def main():
    try:

        session_id = login_to_azkaban()
        print("Logged in to Azkaban successfully.")

        create_cron_schedule(session_id, CRON_EXPRESSION)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

