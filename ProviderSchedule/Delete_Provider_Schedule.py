import requests

uuid = 'provider-schedule-uuid'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/providerschedule/{uuid}'
response = requests.delete(url, auth=('your-username', 'your-password'))
print(response.text)
