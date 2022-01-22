print("Укажите количество секунд которое хотите конвертироовать :")
duration = int(input())
def convert_time(duration: int) -> str:
    if duration >= 60:
        min = int(duration / 60)
        secunds = duration - (min * 60)
        print(str(secunds) + " сек")
        print(str(min) + " мин ")
    else:
        print(str(duration) + " сек")
    hours = int(min / 60)
    if hours > 0:
        print(str(hours) + " час")
        day = int(hours / 24)
        if day > 0:
            print(str(day) + " дн")
    else:
        print("Часы не найдены")
    week = int(day / 7)
    if week > 0:
        print(str(week) + " нед")
    else:
        print("Недель не найдено")
result = convert_time(duration)
print(result)