import random
import string


def generate_code(length: int = 20, number: bool = True, character: bool = True):
    allowed_chars = ""
    if number:
        allowed_chars += string.digits
    if character:
        allowed_chars += string.ascii_letters

    if not allowed_chars:
        assert ValueError(
            'Set at least one of the flags(number,character) to True')

    generated_code = ''.join(random.choice(allowed_chars)
                             for _ in range(length))
    return generated_code
