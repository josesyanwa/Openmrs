import requests

base_url = 'http://localhost:8080/openmrs/ws/rest/v1/appointmentscheduling/timeslot'

data = {
    'startDate': '2023-06-15T09:00:00.000+0000',
    'endDate': '2023-06-15T10:00:00.000+0000',
    'appointmentBlock': 'uuid-of-appointment-block'
}

response = requests.post(base_url, json=data)

if response.status_code == 201:
    timeslot = response.json()
    print(timeslot)
else:
    print(f'Error: {response.status_code} - {response.text}')