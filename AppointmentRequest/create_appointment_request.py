import requests
import json

url = 'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentrequest'
appointment_request = {
    "patient": "patient-uuid",
    "appointmentType": "appointment-type-uuid",
    "requestedOn": "2024-06-01T08:00:00.000+0000",
    "status": "PENDING"
}

response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(appointment_request), auth=('your-username', 'your-password'))
print(response.json())
