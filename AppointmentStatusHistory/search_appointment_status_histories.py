import requests

appointment_uuid = 'appointment-uuid-here'
url = 'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentstatushistory'
params = {
    "appointment": appointment_uuid
}
response = requests.get(url, params=params, auth=('your-username', 'your-password'))
print(response.json())
