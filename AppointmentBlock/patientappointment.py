import requests

openmrs_base_url = "http://localhost:8082/openmrs-standalone"
endpoint = "/ws/rest/v1/appointmentscheduling/appointmentallowingoverbook"
url = openmrs_base_url + endpoint

appointment_data = {
    # Populate the appointment data here
    # Example: 
    "appointmentType": "UUID of appointment type",
    "patient": "UUID of patient",
    "startDateTime": "2023-06-04T10:00:00.000+0000",
    "endDateTime": "2023-06-04T11:00:00.000+0000"
}

headers = {
    "Content-Type": "application/json"
    # Add any additional headers required, such as authentication
}

response = requests.post(url, json=appointment_data, headers=headers)

if response.status_code == 200:
    print("Appointment saved successfully")
else:
    print(f"Error saving appointment: {response.text}")