import requests

url = 'http://your-openmrs-server/ws/rest/v1/appointmentscheduling/appointmentblock'
params = {
    'q': 'search-query'
}
response = requests.get(url, params=params, auth=('your-username', 'your-password'))
print(response.json())
