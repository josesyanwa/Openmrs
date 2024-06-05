import requests

uuid = 'appointment-request-uuid'
url = f'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentrequest/{uuid}?purge=true'
response = requests.delete(url, auth=('your-username', 'your-password'))
print(response.status_code)

