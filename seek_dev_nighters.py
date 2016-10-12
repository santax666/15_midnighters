import requests
import datetime
from pytz import timezone


def send_get_request(url):
    response = requests.get(url)
    return response.json()


def create_attempts_list():
    first_page = 1
    second_page = 2
    url = 'https://devman.org/api/challenges/solution_attempts/?page={0}'
    attempts_list = []
    solution_attempts = send_get_request(url.format(first_page))
    attempts_list = solution_attempts['records'].copy()
    pages_num = solution_attempts['number_of_pages']
    if pages_num > first_page:
        for page in range(second_page, pages_num+1):
            solution_attempts = send_get_request(url.format(int(page)))
            attempts_list.extend(solution_attempts['records'].copy())
    return attempts_list


def check_user_in_midnighters(user, midnighters_list):
    return user in midnighters_list


def get_hour_from_timestamp(time_stamp, time_zone):
    if time_stamp is not None:
        date_time = datetime.datetime.fromtimestamp(time_stamp, time_zone)
        return int(date_time.strftime('%H'))


def is_night_time(hour):
    night_start = 0
    night_stop = 4
    return night_start <= hour < night_stop


def get_midnighters(attempts_list):
    midnighters = []
    for attempt in attempts_list:
        hour = get_hour_from_timestamp(attempt.get('timestamp'),
                                       timezone(attempt.get('timezone')))
        if hour is not None:
            if is_night_time(hour):
                user = attempt.get('username')
                if not check_user_in_midnighters(user, midnighters):
                    midnighters.append(user)
    return midnighters


def output_midnighters(users):
    print('Список пользователей, отправлявших задачи на проверку после 24:00:')
    for user_num, user in enumerate(users, 1):
        print('{0}) {1}'.format(user_num, user))


if __name__ == '__main__':
    attempts_list = create_attempts_list()
    users = get_midnighters(attempts_list)
    output_midnighters(users)
