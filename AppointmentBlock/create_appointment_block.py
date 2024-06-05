import requests
import json

url = 'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentblock'
appointment_block = {
    "startDate": "2024-06-01T08:00:00.000+0000",
    "endDate": "2024-06-01T12:00:00.000+0000",
    "location": "location-uuid",
    "types": ["type-uuid"],
    "provider": "provider-uuid"
}

response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(appointment_block), auth=('your-username', 'your-password'))
print(response.json())
