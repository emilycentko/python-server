EMPLOYEES = [
    {
      "id": 1,
      "name": "Rose Nylund",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Sophia Petrillo",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Dorothy Zbornak",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Blanche Devereaux",
      "locationId": 3
    }
]

def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
    
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee