# !! Admin's username and password start as 'admin' but can be altered.

import random
import getpass
from check_authorization import check_authorization
from decoration import decorator

admin_username = 'admin'
admin_password = 'admin'


def admin_update():
    global admin_username
    global admin_password

    admin_username = input('New Username: ')
    admin_password = input('New Password: ')
    hospital_1.username_list[0] = admin_username
    hospital_1.password_list[0] = admin_password


class Hospital():
    patient_list = []
    employee_list = []
    patient_id_list = []
    username_list = ['admin']
    password_list = ['admin']

    def __init__(self, name):
        self.name = name

    # Creating a new Patient object and storing it in patient_list.
    def add_patient(self):
        new_id = random.randint(1000, 9999)
        while new_id in self.patient_id_list:
            new_id = random.randint(1000, 9999)
        self.patient_id_list.append(new_id)
        name = input('Patient name: ')
        age = input('Patient age: ')
        new_patient = Patient(name, age, new_id, self.name)
        self.patient_list.append(new_patient)
        print(f"\n Added patient's details.\n{new_patient}")

    # Removing patient object from patient_list.
    def remove_patient(self):
        id = int(input('patient ID: '))
        for i, patient in enumerate(self.patient_list):
            if id == patient.id:
                self.patient_list.pop(i)

    @decorator
    def print_patient_list(self):
        for patient in self.patient_list:
            print(patient)

    def add_patient_record(self):
        id = int(input('patient ID:'))
        if id in self.patient_id_list:
            index = self.patient_id_list.index(id)
            self.patient_list[index].add_records()
        else:
            print('No such ID, mate')

    @decorator
    def view_record(self):
        id = int(input('patient ID:'))
        if id in self.patient_id_list:
            index = self.patient_id_list.index(id)
            self.patient_list[index].view()
        else:
            print('no such id.')

    def add_employee(self):
        print('\nEmployee details.')
        name = input('Name: ')
        age = input('Age: ')
        job = ''
        while job not in ['doctor', 'nurse', 'janitor']:
            job = input(
                'Type ONE of the following (Doctor, Nurse, Janitor): ').lower()
        new_employee = Employee(name, age, job)
        new_employee.login_deets()
        self.employee_list.append(new_employee)
        self.username_list.append(new_employee.username)
        self.password_list.append(new_employee.password)

    def remove_employee(self):
        rem_name = input("Employee's name: ")
        rem_job = input("Employee's job: ")
        for i, employee in enumerate(self.employee_list):
            if employee.name == rem_name:
                if rem_job == employee.job:
                    self.employee_list.pop(i)
                    self.username_list.pop(i-1)
                    self.password_list.pop(i-1)
                    return
            print('No match found.')

    @decorator
    def print_employee_list(self):
        for employee in self.employee_list:
            print(employee)


class Patient():
    records = []

    def __init__(self, name, age, id, hospital):
        self.name = name
        self.age = age
        self.id = id
        self.hospital = hospital

    def add_records(self):
        new_rec = input('Things to add: ')
        self.records.append(new_rec)

    def view(self):
        for record in self.records:
            print(f'\n{record}')

    def __str__(self):
        return f'\nPatient ID: {self.id} in {self.hospital} \nName:{self.name}   Age:{self.age}'


class Employee():
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f'\n{self.name}, {self.age}, {self.job}'

    def login_deets(self):
        print('Enter the username and password you (the employee) would like to use.')
        self.username = input('Username: ')
        self.password = input('Password: ')


hospital_1 = Hospital('Hospital 1')

username, password = '', ''


def logged_in_interface(user):
    global username
    global password
    while user != '':
        if user == 'admin':
            print('Type the corresponding number to carry out that action\n 1. List patients\n 2. Add patient \n 3. Remove patient\n 4. Add patient record \n 5. View patient record\n 6. List employees\n 7. Add employee\n 8. Remove employee\n 9. Change username & password\n 10. Log Out')

        elif user == 'doctor' or user == 'nurse':
            print(f'\nWelcome {username} \nType the corresponding number to carry out that action\n 1. List patients\n 2. Add patient \n 3. Remove patient \n 4. Add patient record.\n 5. View patient record. \n 10. Log Out ')

        else:
            print(
                f'Welcome {username}! Unfortunately we do not have any orders for you to execute :( \n 10. Log out')

        action = input('').lower()

        if user == 'admin':
            if action == '7':
                hospital_1.add_employee()
            elif action == '6':
                hospital_1.print_employee_list()
            elif action == '8':
                hospital_1.remove_employee()
            elif action == '9':
                admin_update()

        if user in ['admin', 'doctor', 'nurse']:
            if action == '1':
                hospital_1.print_patient_list()
            elif action == '2':
                hospital_1.add_patient()
            elif action == '3':
                hospital_1.remove_patient()
            elif action == '4':
                hospital_1.add_patient_record()
            elif action == '5':
                hospital_1.view_record()

        if action == '10':
            user = ''
            continue_ = input('Would you like to continue?(y/n)')
            if continue_ == 'y':
                username = ''
                password = ''
                logging_in()
            else:
                break


def logging_in():
    global username
    global password
    while username not in hospital_1.username_list:
        username = input('Username:\n')
        password = getpass.getpass(prompt='Password:\n')

        x = hospital_1.username_list.index(username)
        if hospital_1.password_list[x] != password:
            print('Wrong password!')
            username, password = '', ''

    if username == admin_username and password == admin_password:
        print('Welcome MAIN ADMIN')
        logged_in_interface('admin')
    else:
        logged_in_interface(check_authorization(
            hospital_1.employee_list, username))


logging_in()
