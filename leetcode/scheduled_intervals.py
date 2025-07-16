from datetime import datetime, timedelta

DAYS = {
        "sun": 0,
    "mon": 1,
    "tue": 2,
    "wed": 3,
    "thu": 4,
    "fri": 5,
    "sat": 6
}

def parseTime(time):
    parts = time.split(" ")
    timeParts = parts[1].split(":")
    hour = int(timeParts[0])
    minute = int(timeParts[1][0:2])
    am_pm = parts[2].lower()

    if am_pm == "pm" and hour != 12:
        hour += 12
    elif am_pm == "am" and hour == 12:
        hour = 0

    return [hour, minute]

def getAllIntervals(start_time, end_time):
    start_day_number = DAYS[start_time.split()[0]]
    end_day_number = DAYS[end_time.split()[0]]

    start = parseTime(start_time)
    end = parseTime(end_time)

    print(f'Start: {start}, End: {end}')
    times = []
    current_hour = start[0]
    current_minute = start[1]
    current_day = start_day_number

    while current_day <= end_day_number or current_hour < end[0] or (current_hour == end[0] and current_minute <= end[1]):
        times.append(f'{current_day} {current_hour}:{current_minute:02d}')

        # increment time by 5 minutes
        current_minute += 5
        if current_minute >= 60:
            current_minute = 0
            current_hour += 1

        if current_hour >= 24:
            current_hour = 0
            current_minute = 0
            current_day += 1
    return times

if __name__ == "__main__":
    start_time = "mon 9:00 am"
    end_time = "wed 5:00 pm"

    print(getAllIntervals(start_time, end_time))

