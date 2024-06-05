import requests

uuid = 'appointment-block-uuid'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentblock/{uuid}'
response = requests.delete(url, auth=('your-username', 'your-password'))
print(response.status_code)
