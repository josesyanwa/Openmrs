import requests
import json

uuid = 'appointment-request-uuid'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentrequest/{uuid}'
updated_appointment_request = {
    "patient": "patient-uuid",
    "appointmentType": "appointment-type-uuid",
    "requestedOn": "2024-06-01T09:00:00.000+0000",
    "status": "CONFIRMED"
}

response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(updated_appointment_request), auth=('your-username', 'your-password'))
print(response.json())
