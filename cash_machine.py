import psycopg2 as db
from datetime import datetime

"""
you should write code below for Sql:
create table sms(
    id bigserial primary key,
    phone_number varchar(20) not null,
    card_number bigint not null
);

create table users(
    id bigserial primary key,
    full_name varchar(40) not null,
    card_number bigint not null unique,
    expiry_date text not null,
    balance bigint not null,
    password varchar(30) not null unique,
    phone_number varchar(20) not null unique,
    sms_id int references sms(id)
);
"""
class Database:
    @staticmethod
    def select_query(query):
        database = db.connect(
            database="bankomat",
            host="localhost",
            user="postgres",
            password="Burxoniddin12345"
        )
        cursor = database.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    @staticmethod
    def insert_query(query):
        database = db.connect(
            database="bankomat",
            host="localhost",
            user="postgres",
            password="Burxoniddin12345"
        )
        cursor = database.cursor()
        cursor.execute(query)
        database.commit()


def register_menu():
    full_name = input("Enter your full name: ")
    card_number = input("Enter your card number: ")
    if len(card_number) == 15:
        print("Card number must be 16 digits long.")
        return ghost_menu()
    expiry_date = input("Enter your expire date(mm/yy): ")
    try:
        expiry_date = datetime.strptime(expiry_date, "%m/%y")
        current_date = datetime.now()
        if expiry_date < current_date:
            print("Card has expired.")
    except ValueError:
        print("Invalid date format. Please provide expiry date in mm/yy format.")
    balance = input("Enter your balance: ")
    password = input("Enter your password: ")
    phone_number = input("Enter your phone number: ")
    query = f"insert into users(full_name, card_number, expiry_date, balance, password, phone_number) values('{full_name}', '{card_number}', '{expiry_date}', '{balance}', '{password}', '{phone_number}')"
    Database.insert_query(query)
    print("Registered Successfully.")
    return ghost_menu()

def login_menu():
    card_number = input("Enter your card number: ")
    if len(card_number) == 15:
        print("Card number must be 16 digits long.")
        return ghost_menu()
    password = input("Enter your password: ")
    query = f"select * from users where card_number = '{card_number}'"
    query1 = f"select * from users where password = '{password}'"
    result1 = Database.select_query(query1)
    result = Database.select_query(query)
    if result and result1:
        print("Login successful.")
        return main_menu()
    else:
        print("Invalid card number or password.")
        return login_menu()

def sms():
    card_number = input("Enter your card number: ")
    if len(card_number) == 15:
        print("Card number must be 16 digits long.")
        return main_menu()
    phone_number = input("Enter your phone number: ")
    query = f"select * from sms where phone_number = '{phone_number}' or card_number='{card_number}'"
    result = Database.select_query(query)
    if result:
        print("This phone has already been connected a card number")
        return main_menu()
    else:
        query1 = f"insert into sms(phone_number, card_number) values('{phone_number}', '{card_number}')"
        result = Database.insert_query(query1)
        print("Card number has been connected to a phone successfully.")


def show_balance():
    card_number = input("Enter your card number: ")
    if len(card_number) == 15:
        print("Card number must be 16 digits long.")
        return main_menu()
    query = f"select balance from users where card_number = '{card_number}'"
    result = Database.select_query(query)
    if result:
        balance = result[0][0]
        print(f"Your current balance is {balance}")
    else:
        print("Invalid card number.")

def take_money():
    card_number = input("Enter your card number: ")
    if len(card_number) == 15:
        print("Card number must be 16 digits long.")
        return main_menu()
    balance = int(input("Enter how much money you would like to take: "))
    query = f"select balance from users where card_number = '{card_number}'"
    result = Database.select_query(query)
    if not result:
        print("Card number not found or invalid.")
        return main_menu()
    balance1 = result[0][0]
    if balance > balance1:
        print(f"You do not have enough money.")
        return main_menu()
    else:
        new_balance = balance1 - balance
        query1 = f"update users set balance = {new_balance} where card_number = '{card_number}'"
        Database.insert_query(query1)
        print(f"Money taken successfully. Your new balance is {new_balance}.")
        return main_menu()



def main_menu():
    while True:
        print("1. Connect to phone with SMS")
        print("2. Show Balance")
        print("3. Take money")
        print("4. Log out")
        choice = input("Enter your choice: ")
        if choice == "1":
            sms()
        elif choice == "2":
            show_balance()
        elif choice == "3":
            take_money()
        elif choice == "4":
            print("Exiting...")
            return ghost_menu()
        else:
            print("Invalid choice.")

def ghost_menu():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_menu()
        elif choice == "2":
            login_menu()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    ghost_menu()
