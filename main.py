from application.db.people import get_employess
from application.salary import calculare_salary
from datetime import datetime





if __name__ == '__main__':
    print(f'Сегодня: {datetime.today().strftime("%d-%m-%y")}')
    get_employess()
    calculare_salary()