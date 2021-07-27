def add_time(start, duration, day = None):
    
    start = start.split()
    startTime = start[0].split(":")
    duration = duration.split(":")

    hour = int(startTime[0]) + int(duration[0])
    mins = int(startTime[1]) + int(duration[1])

    addHour = 0
    while mins > 60:
        mins = mins - 60
        addHour = addHour + 1

    hour = hour + addHour
    brrr = start[1]
    dayPassed = 0
    while hour >= 12:
        hour = hour - 12
        if brrr == "AM":
            brrr = "PM"
        elif brrr == "PM":
            brrr = "AM"
            dayPassed = dayPassed + 1

    if hour == 0:
       hour = 12 

    if len(str(mins)) == 1:
        mins = "0" + str(mins)

    daysOfTheWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    hehe = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day != None:
        dayIndex = daysOfTheWeek.index(day.lower())
        day = hehe[(dayIndex + dayPassed) % 7]
        newTime = str(hour) + ":" + str(mins) + " " + brrr + ", " + day
    else:
        newTime = str(hour) + ":" + str(mins) + " " + brrr
    
    if dayPassed == 1:
        newTime = newTime + " (next day)"
    elif dayPassed > 1:
        newTime = newTime + " (" + str(dayPassed) + " days later)"
    return newTime
