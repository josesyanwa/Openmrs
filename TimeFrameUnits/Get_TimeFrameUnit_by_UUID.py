import requests

uuid = 'timeframeunit-uuid'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/timeframeunits/{uuid}'
response = requests.get(url, auth=('your-username', 'your-password'))
print(response.json())
