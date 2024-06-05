import requests

uuid = 'appointment-uuid-here'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointment/{uuid}'
response = requests.get(url, auth=('your-username', 'your-password'))
print(response.json())
