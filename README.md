# IP Address Management REST API

Create a simple IP Address Management REST API on top of any data store. It will include the ability to add IP Addresses by CIDR block and then either acquire or release IP addresses individually. Each IP address will have a status associated with it that is either “available” or “acquired”.

The REST API must support four endpoint:

- **Create IP addresses** - take in a CIDR block (e.g. 10.0.0.1/24) and add all IP addresses within that block to the data store with status “available”
- **List IP addresses** - return all IP addresses in the system with their current status
- **Acquire an IP** - set the status of a certain IP to “acquired”
- **Release an IP** - set the status of a certain IP to “available”

# Quick Start Guid by Alem T. Getu

Requirements

pipenv
`install pipenv by following guide -> https://pypi.org/project/pipenv/`

Clone This Repo

Cd To Project Dir and Install all pakcages with pipenv

`$ pipenv install`

Run Migrations

`$ python manage.py migrate`

Run Server (default port 8000)

`$ python manage.py runserver`

Go to http://localhost:8000 -> Using the browseable API you can perform CRUD operations

** Routes **

cidrs: "http://localhost:8000/cidrs/" list, add (adding cidr block will also create all the IPs), update, delete
ips: "http://localhost:8000/ips/" list, update, delete
