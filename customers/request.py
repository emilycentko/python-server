import sqlite3
import json
from models import Customer

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
   
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email
        FROM customer c
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            customer = Customer(row['id'], row['name'], row['address'],
                            row['email'])

            customers.append(customer.__dict__)

    return json.dumps(customers)

def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'])

        return json.dumps(customer.__dict__)

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

