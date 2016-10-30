
# Midnighters in DEVMAN.ORG

Данный скрипт выводит список тех пользователей, кто отправлял задачи на проверку после 24:00.

## Запуск

Введите в терминале:

    python3.5 seek_dev_nighters.py

## Зависимости

Скрипт написан на языке Python 3, поэтому требует его наличия.

Для выполнения HTTP-запросов должен быть установлен модуль [requests][].

Для получения временной зоны и часа отправки задания на проверку должны быть установлены модули [pytz][] и [datetime][].

## Поддержка

Если у вас возникли сложности или вопросы по использованию скрипта, создайте 
[обсуждение][] в данном репозитории или напишите на электронную почту 
<IvanovVI87@gmail.com>.

## Документация

Документацию к модулю requests можно получить по [ссылке1][].

Документацию к модулю pytz можно получить по [ссылке2][].

Документацию к модулю datetime можно получить по [ссылке3][].


[Github'а]: https://github.com
[requests]: https://pypi.python.org/pypi/requests/2.11.1
[pytz]: https://pypi.python.org/pypi/pytz/
[datetime]: https://pypi.python.org/pypi/DateTime/4.1.1
[обсуждение]: https://github.com/santax666/15_midnighters/issues
[ссылке1]: http://docs.python-requests.org/en/master/
[ссылке2]: http://pythonhosted.org/pytz/
[ссылке3]: https://docs.python.org/3/library/datetime.html
