from random import sample


def get_numbers_ticket(min, max, quantity):
    """Повертає відсортовану випадкову вибірку унікальних чисел."""
    if not all(type(value) is int for value in (min, max, quantity)):
        return []
    if not 1 <= min <= max <= 1000 or not min <= quantity <= max:
        return []

    numbers = range(min, max + 1)
    if quantity > len(numbers):
        return []

    return sorted(sample(numbers, quantity))
