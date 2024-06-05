import requests
import json

uuid = 'appointment-block-uuid'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentblock/{uuid}'
updated_appointment_block = {
    "startDate": "2024-06-01T09:00:00.000+0000",
    "endDate": "2024-06-01T13:00:00.000+0000",
    "location": "location-uuid",
    "types": ["type-uuid"],
    "provider": "provider-uuid"
}

response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(updated_appointment_block), auth=('your-username', 'your-password'))
print(response.json())
