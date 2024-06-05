import requests

base_url = 'http://localhost:8080/openmrs/ws/rest/v1/appointmentscheduling/timeslot'

timeslot_uuid = 'uuid-of-timeslot'

response = requests.delete(f'{base_url}/{timeslot_uuid}', params={'purge': 'true'})

if response.status_code == 204:
    print('TimeSlot purged successfully')
else:
    print(f'Error: {response.status_code} - {response.text}')