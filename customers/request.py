CUSTOMERS = [
     {
      "id": 1,
      "name": "Jean-Luc Picard",
      "address": "1701 Enterprise Ct.",
      "email": "jlp@enterprise.co"
    },
    {
      "id": 2,
      "name": "Dana Scully",
      "address": "100 Believe Way",
      "email": "d.scully@skeptic.com"
    },
    {
      "id": 3,
      "name": "Peter Parker",
      "address": "200 Chicago St.",
      "email": "peter.parker@imnotspiderman.com"
    },
    {
      "id": 4,
      "name": "Mina Harker",
      "address": "190 Transylvania Ave.",
      "email": "mina.harker@dracula.com"
    },
    {
      "id": 5,
      "name": "Han Solo",
      "address": "77 Millennium Way",
      "email": "han@rebels.org"
    },
    {
      "email": "f.mulder@believer.com",
      "name": "Fox Mulder",
      "address": "360 Aliens Drive",
      "id": 6
    }
]

def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
    
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer