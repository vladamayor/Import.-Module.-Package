from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date as dt
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Имя сотрудника', 'Зарплата']
table.add_row([get_employees('Сева'), calculate_salary(100)])


if __name__ == '__main__':
    print(dt.today())
    print(table)