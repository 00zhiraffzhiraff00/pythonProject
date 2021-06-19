# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# Time set up in seconds
seconds_in_minute = 60
seconds_in_hour = 3600
seconds_in_day = 86400

duration = (int(input("Enter duration in seconds")))

days = duration // seconds_in_day
duration -= days * seconds_in_day

hours = duration // seconds_in_hour
duration -= hours * seconds_in_hour

minutes = duration // seconds_in_minute
duration -= minutes * seconds_in_minute

seconds = duration % seconds_in_minute
duration -= seconds * seconds_in_minute

print(days, 'дн', hours, 'ч', minutes, 'мин', seconds, 'сек')

