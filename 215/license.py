import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    if re.match(r'(PB-)([A-Z0-9]{8}[-]){3}[A-Z0-9]{8}$', key):
        return True
    else:
        return False
