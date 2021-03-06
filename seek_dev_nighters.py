import requests
import datetime
from pytz import timezone


def get_records(page):
    url = 'https://devman.org/api/challenges/solution_attempts/'
    payload = {'page': page}
    attempts = requests.get(url, params=payload).json()
    return attempts['records'], attempts['number_of_pages']


def create_attempts_list():
    attempts_list = []
    page = 1
    while True:
        json_data, pages_num = get_records(page)
        attempts_list.extend(json_data)
        page += 1
        if page > pages_num:
            break
    return attempts_list


def check_user_in_midnighters(user, midnighters_list):
    return user in midnighters_list


def get_hour_from_timestamp(time_stamp, time_zone):
    if time_stamp is not None:
        date_time = datetime.datetime.fromtimestamp(time_stamp, time_zone)
        return int(date_time.strftime('%H'))


def is_night_time(hour):
    NIGHT_START_HOUR = 0
    NIGHT_STOP_HOUR = 4
    return NIGHT_START_HOUR <= hour < NIGHT_STOP_HOUR


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
