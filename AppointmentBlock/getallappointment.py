import requests

url = 'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentblock'
response = requests.get(url, auth=('your-username', 'your-password'))
print(response.json())
