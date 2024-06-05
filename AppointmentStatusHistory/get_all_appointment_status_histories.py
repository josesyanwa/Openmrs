import requests

url = 'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentstatushistory'
response = requests.get(url, auth=('your-username', 'your-password'))
print(response.json())
