import requests

base_url = 'http://localhost:8080/openmrs/ws/rest/v1/appointmentscheduling/timeslot'

params = {
    'appointmentType': 'uuid-of-appointment-type',
    'fromDate': '2023-06-01',
    'toDate': '2023-06-30',
    'provider': 'uuid-of-provider',
    'location': 'uuid-of-location',
    'includeFull': 'true',
    'excludeTimeSlotsPatientAlreadyBookedFor': 'uuid-of-patient'
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    timeslots = response.json()
    print(timeslots)
else:
    print(f'Error: {response.status_code} - {response.text}')