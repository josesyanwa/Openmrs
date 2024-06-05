import requests
import json

url = 'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointment'
appointment_data = {
    "timeSlot": "time-slot-uuid",
    "patient": "patient-uuid",
    "status": "SCHEDULED",
    "appointmentType": "appointment-type-uuid",
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, auth=('your-username', 'your-password'), data=json.dumps(appointment_data), headers=headers)
print(response.json())
