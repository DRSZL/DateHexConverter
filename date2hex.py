from datetime import datetime, timedelta
import hashlib

def string_to_sha256_hex(string):
    return hashlib.sha256(string.encode()).hexdigest()

# Constants
START_DATE = datetime(1900, 1, 1)
END_DATE = datetime.now()
TEXT_FILE_NAME = "allDates2hex.txt"
DATE_FORMATS = [
    "%d.%m.%Y",  # DD.MM.YYYY
    "%Y.%m.%d",  # YYYY.MM.DD
    "%m.%d.%Y",  # MM.DD.YYYY
    "%Y-%m-%d",  # YYYY-MM-DD
    "%d-%m-%Y",  # DD-MM-YYYY
    "%d-%m-%y",  # DD-MM-YY
    "%m/%d/%y",  # MM/DD/YY
    "%d/%m/%y",  # DD/MM/YY
    "%d/%m/%Y",  # DD/MM/YYYY
    "%m/%d/%Y",  # MM/DD/YYYY
    "%A, %B %d, %Y",  # Monday, January 01, 1900
    "%B %d, %Y"  # January 01, 1900
]

def generate_hashes_for_date(date):
    return [string_to_sha256_hex(date.strftime(fmt)) for fmt in DATE_FORMATS]

def generate_hashes_for_seconds(date):
    next_day = date + timedelta(days=1)
    hashes = []
    while date < next_day:
        hashes.append(string_to_sha256_hex(str(date)))
        date += timedelta(seconds=1)
    return hashes

with open(TEXT_FILE_NAME, 'w') as f:
    current_date = START_DATE
    while current_date <= END_DATE:
        date_hashes = generate_hashes_for_date(current_date)
        f.write('\n'.join(date_hashes) + '\n')
        
        second_hashes = generate_hashes_for_seconds(current_date)
        f.write('\n'.join(second_hashes) + '\n')
        
        current_date += timedelta(days=1)
