import requests

url = 'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmenttype'
data = {
    'name': 'New Appointment Type',
    'description': 'Description of the new appointment type',
    'duration': 30,  # Duration in minutes
    'confidential': False,  # Whether the appointment type is confidential
    'visitType': 'visit-type-uuid'  # UUID of the associated visit type
}
response = requests.post(url, json=data, auth=('your-username', 'your-password'))
print(response.json())
