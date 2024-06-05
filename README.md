# Openmrs

# 1. TIMESLOT

- GET /openmrs/ws/rest/v1/appointmentscheduling/timeslot

This endpoint retrieves a list of TimeSlot resources based on various filters.

- GET /openmrs/ws/rest/v1/appointmentscheduling/timeslot/{uuid}

This endpoint retrieves a specific TimeSlot resource by its UUID.
It uses the getByUniqueId method to fetch the TimeSlot with the given UUID.

- POST /openmrs/ws/rest/v1/appointmentscheduling/timeslot

This endpoint creates a new TimeSlot resource.

- PUT /openmrs/ws/rest/v1/appointmentscheduling/timeslot/{uuid}

This endpoint updates an existing TimeSlot resource.

- DELETE /openmrs/ws/rest/v1/appointmentscheduling/timeslot/{uuid}

This endpoint deletes (voids) an existing TimeSlot resource.

- DELETE /openmrs/ws/rest/v1/appointmentscheduling/timeslot/{uuid}?purge=true

This endpoint purges (permanently removes) an existing TimeSlot resource.


# 2. AppointmentBlock

Get all appointment blocks: 
- GET /ws/rest/v1/appointmentscheduling/appointmentblock

Create a new appointment block: 
- POST /ws/rest/v1/appointmentscheduling/appointmentblock

Get an appointment block by UUID: 
- GET /ws/rest/v1/appointmentscheduling/appointmentblock/{uuid}

Update an appointment block:
- POST /ws/rest/v1/appointmentscheduling/appointmentblock/{uuid}

Delete (void) an appointment block: 
- DELETE /ws/rest/v1/appointmentscheduling/appointmentblock/{uuid}

Purge an appointment block: 
- DELETE /ws/rest/v1/appointmentscheduling/appointmentblock/{uuid}?purge=true

Search for appointment blocks: 
- GET /ws/rest/v1/appointmentscheduling/appointmentblock?q={query}


# 3. AppointmentRequest

Get all appointment requests: 
- GET /ws/rest/v1/appointmentscheduling/appointmentrequest

Create a new appointment request: 
- POST /ws/rest/v1/appointmentscheduling/appointmentrequest

Get an appointment request by UUID: 
- GET /ws/rest/v1/appointmentscheduling/appointmentrequest/{uuid}

Update an appointment request: 
- POST /ws/rest/v1/appointmentscheduling/appointmentrequest/{uuid}

Delete (void) an appointment request: 
- DELETE /ws/rest/v1/appointmentscheduling/appointmentrequest/{uuid}

Purge an appointment request: 
- DELETE /ws/rest/v1/appointmentscheduling/appointmentrequest/{uuid}?purge=true

Search for appointment requests: 
- GET /ws/rest/v1/appointmentscheduling/appointmentrequest?q={query}


# 4 . AppointmentRequestStatus

Get all appointment request statuses: 
- GET /ws/rest/v1/appointmentscheduling/appointmentrequeststatus

# 5. PatientAppointment

Get All Appointments: 
- GET /ws/rest/v1/appointmentscheduling/appointment

Get Appointment by UUID: 
- GET /ws/rest/v1/appointmentscheduling/appointment/{uuid}

Create Appointment: 
- POST /ws/rest/v1/appointmentscheduling/appointment

Update Appointment: 
- POST /ws/rest/v1/appointmentscheduling/appointment/{uuid}

Delete Appointment: 
- DELETE /ws/rest/v1/appointmentscheduling/appointment/{uuid}

Search Appointments: 
- GET /ws/rest/v1/appointmentscheduling/appointment?q={query_parameters}


# 6.AppointmentStatusHistory

Get All Appointment Status Histories: 
- GET /ws/rest/v1/appointmentscheduling/appointmentstatushistory

Search Appointment Status Histories by Appointment: 
- GET /ws/rest/v1/appointmentscheduling/appointmentstatushistory?q={appointment_uuid}

# 7. AppointmentStatus

Get All Appointment Status Values: 
- GET /ws/rest/v1/appointmentscheduling/appointmentstatus

# 8.AppointmentStatusType

Get All Appointment Status Type Values: 
- GET /ws/rest/v1/appointmentscheduling/appointmentstatustype

# 9. AppointmentType

Get All Appointment Types: 
- GET /ws/rest/v1/appointmentscheduling/appointmenttype

Get Appointment Type by UUID: 
- GET /ws/rest/v1/appointmentscheduling/appointmenttype/{uuid}

Create Appointment Type: 
- POST /ws/rest/v1/appointmentscheduling/appointmenttype

Update Appointment Type: 
- POST /ws/rest/v1/appointmentscheduling/appointmenttype/{uuid}

Delete Appointment Type: 
- DELETE /ws/rest/v1/appointmentscheduling/appointmenttype/{uuid}

