def check_authorization(listy, user):
    for employee in listy:
        if employee.username == user:
            return employee.job
