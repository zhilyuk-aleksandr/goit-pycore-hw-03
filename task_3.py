import re


def normalize_phone(phone_number):
    """Повертає номер у міжнародному форматі без розділювачів."""
    cleaned_number = re.sub(r"[^0-9+]", "", phone_number)
    digits = cleaned_number.replace("+", "")
    if cleaned_number.startswith("+") or digits.startswith("380"):
        return "+" + digits
    return "+38" + digits
