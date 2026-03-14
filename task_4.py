class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        money = self.hours * self.hourly_payment
        return money
 
employee_1 = EmployeeSalary('Леша', 5, 3, 'lubimka@mail.ru')
print(employee_1.salary())


employee_2 = EmployeeSalary.get_hours('Леша', 3, 'lubimka@mail.ru')
print(employee_2.__dict__)

employee_3 = EmployeeSalary.get_email('Леша', 3, 1)
print(employee_3.__dict__)

employee_1 = EmployeeSalary.set_hourly_payment(600)
employee_1 = EmployeeSalary('Леша', 5, 3, 'lubimka@mail.ru')
print(employee_1.salary())