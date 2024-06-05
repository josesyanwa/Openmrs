import requests

base_url = 'http://localhost:8080/openmrs/ws/rest/v1/appointmentscheduling/timeslot'

timeslot_uuid = 'uuid-of-timeslot'

data = {
    'startDate': '2023-06-15T10:00:00.000+0000',
    'endDate': '2023-06-15T11:00:00.000+0000',
    'appointmentBlock': 'uuid-of-appointment-block'
}

response = requests.put(f'{base_url}/{timeslot_uuid}', json=data)

if response.status_code == 200:
    timeslot = response.json()
    print(timeslot)
else:
    print(f'Error: {response.status_code} - {response.text}')