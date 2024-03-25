from application.db.people import *
from application.salary import *
from datetime import *





if __name__ == '__main__':
    print(f'Сегодня: {datetime.today().strftime("%d-%m-%y")}')
    get_employess()
    calculare_salary()