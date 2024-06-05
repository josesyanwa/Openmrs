import requests

uuid = 'provider-schedule-uuid'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/providerschedule/{uuid}'
data = {
    'startDate': '2024-06-06',
    'endDate': '2024-06-10',
    'startTime': '09:00',
    'endTime': '18:00',
    'location': 'location-uuid',
    'types': ['type-uuid1', 'type-uuid2'],
    'provider': 'provider-uuid'
}
response = requests.post(url, json=data, auth=('your-username', 'your-password'))
print(response.json())
