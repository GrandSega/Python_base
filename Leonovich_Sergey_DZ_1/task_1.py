def convert_time(sec):
    if sec >= 60:
        min = int(sec / 60)
        secunds = sec - (min * 60)
        print(str(min) + " Minuts ", str(secunds) + " Secunds")
    else:
        print(str(sec) + " Seconds")
    hours = int(sec / 3600)
    if hours > 0:
        print("Hours exist -> " + str(hours))
        day = int(hours / 24)
        if day > 0:
            print("Day exist -> "+ str(day))
    else:
        print("Hours not exist")
    week = int( day * 7)
    if week > 0:
        print("Week exist -> " + str(week) )
    else:
        print("Week not exist")
convert_time(150000)