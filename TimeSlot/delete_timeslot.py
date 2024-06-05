import requests

base_url = 'http://localhost:8080/openmrs/ws/rest/v1/appointmentscheduling/timeslot'

timeslot_uuid = 'uuid-of-timeslot'
reason = 'Reason for voiding the timeslot'

response = requests.delete(f'{base_url}/{timeslot_uuid}', params={'reason': reason})

if response.status_code == 204:
    print('TimeSlot deleted successfully')
else:
    print(f'Error: {response.status_code} - {response.text}')