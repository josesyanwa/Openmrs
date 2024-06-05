import requests

uuid = 'appointment-type-uuid'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmenttype/{uuid}'
response = requests.delete(url, auth=('your-username', 'your-password'))
print(response.text)
