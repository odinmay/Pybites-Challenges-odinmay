import base64
import csv
from typing import List  # will remove with 3.9


def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    # Decode string
    out = base64.b64decode(data)
    decoded_data = str(out, 'utf-8')
    # Split csv file and build list
    csv_lines = decoded_data.splitlines()
    info = [item.split(',')[2] for item in csv_lines[1:]]

    return info
