import re
from datetime import datetime


def get_days_from_today(date):
    """Повертає різницю в днях між сьогодні та датою у форматі YYYY-MM-DD."""
    if not isinstance(date, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", date):
        raise ValueError("Вкажіть дату у форматі YYYY-MM-DD.")

    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as error:
        raise ValueError("Вкажіть дійсну календарну дату.") from error

    return (datetime.today().date() - given_date).days
