import requests

url = 'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointment'
params = {
    "fromDate": "2023-01-01",
    "toDate": "2023-12-31",
    "patient": "patient-uuid",
    "status": "SCHEDULED",
}
response = requests.get(url, params=params, auth=('your-username', 'your-password'))
print(response.json())
