import requests
import json

uuid = 'appointment-uuid-here'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointment/{uuid}'
update_data = {
    "status": "COMPLETED",
    "reason": "Reason for update",
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, auth=('your-username', 'your-password'), data=json.dumps(update_data), headers=headers)
print(response.json())
