import requests

uuid = 'appointment-request-uuid'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentrequest/{uuid}'
response = requests.get(url, auth=('your-username', 'your-password'))
print(response.json())
