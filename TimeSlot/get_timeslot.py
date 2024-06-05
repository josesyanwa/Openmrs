import requests

base_url = 'http://localhost:8080/openmrs/ws/rest/v1/appointmentscheduling/timeslot'

timeslot_uuid = 'uuid-of-timeslot'

response = requests.get(f'{base_url}/{timeslot_uuid}')

if response.status_code == 200:
    timeslot = response.json()
    print(timeslot)
else:
    print(f'Error: {response.status_code} - {response.text}')