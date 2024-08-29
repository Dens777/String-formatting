# Использование %:
team1 = 'Мастера кода'
team2 = 'Волшебники данных'

def num(team1_num=0, team2_num=0):  # количество участников команды
    print('В команде %s участников: %s !' % (team1, team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# Использование format:
score_1 = 0
score_2 = 0

def time(team_1_time=0, team_2_time=0, tasks_total=0):  # количество решенных задач
    time1 = team_1_time
    time2 = team_2_time

    print('Команда {} решила задач: {}!'.format(team2, score_2))
    print('{} решили задачи за {} cек. !'.format(team2, time2))

# Использование f-строк:
def challenge_result(tasks_total=0, time_avg=0, team_1_time=0, team_2_time=0):
    print(f'Команды решили {score_1} и {score_2} задач')
    if score_1 > score_2 or score_1==score_2 and team_1_time > team_2_time:
        result=(f'Результат битвы: победа команды {team1} !')
    elif score_1 < score_2 or score_1==score_2 and team_1_time < team_2_time:
        result=(f'Результат битвы: победа команды {team2} !')
    else:
        result=('Ничья!')
    print(result)

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')


num(team1_num=5, team2_num=6)
score_1 = 40
score_2 = 42
time(team_1_time=1552.512, team_2_time=2153.31451)
challenge_result(tasks_total=82, time_avg=45.2)

