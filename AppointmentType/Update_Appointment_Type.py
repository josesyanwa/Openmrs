import requests

uuid = 'appointment-type-uuid'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmenttype/{uuid}'
data = {
    'name': 'Updated Appointment Type Name',
    'description': 'Updated description of the appointment type',
    'duration': 45,  # Updated duration in minutes
    'confidential': True,  # Updated confidentiality status
    'visitType': 'new-visit-type-uuid'  # Updated UUID of the associated visit type
}
response = requests.post(url, json=data, auth=('your-username', 'your-password'))
print(response.json())
