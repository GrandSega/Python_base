print("Укажите количество секунд которое хотите конвертироовать :")
time_to_convert = int(input())
def convert_time(sec):
    if sec >= 60:
        min = int(sec / 60)
        secunds = sec - (min * 60)
        print(str(secunds) + " сек")
        print(str(min) + " мин ")
    else:
        print(str(sec) + " сек")
    hours = int(min / 60)
    if hours > 0:
        print(str(hours) + " час")
        day = int(hours / 24)
        if day > 0:
            print(str(day) + " дня")
    else:
        print("Часы не найдены")
    week = int( day / 7)
    if week > 0:
        print(str(week) + " нед")
    else:
        print("Недель не найдено")
convert_time(time_to_convert)