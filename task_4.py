from calendar import isleap
from datetime import datetime, timedelta


def _birthday_in_year(birthday, year):
    if birthday.month == 2 and birthday.day == 29 and not isleap(year):
        return birthday.replace(year=year, day=28)
    return birthday.replace(year=year)


def get_upcoming_birthdays(users):
    """Повертає дати привітань для днів народження в найближчі сім днів."""
    today = datetime.today().date()
    last_day = today + timedelta(days=6)
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        next_birthday = _birthday_in_year(birthday, today.year)
        if next_birthday < today:
            next_birthday = _birthday_in_year(birthday, today.year + 1)
        if next_birthday > last_day:
            continue

        weekday = next_birthday.weekday()
        congratulation_date = next_birthday
        if weekday >= 5:
            congratulation_date += timedelta(days=7 - weekday)

        upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
        })

    return upcoming_birthdays
