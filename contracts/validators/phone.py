import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException


def is_valid_international_phone(value: str) -> bool:
    """
    Validates if a numeric-only international phone is valid by injecting '+' temporarily.
    Expects values like '5511987654321' (no symbols, spaces, or plus).
    """
    try:
        if not value.isdigit():
            return False

        parsed_number = phonenumbers.parse(f"+{value}", None)

        return phonenumbers.is_possible_number(parsed_number) and phonenumbers.is_valid_number(parsed_number)

    except NumberParseException:
        return False