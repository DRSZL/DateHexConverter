from datetime import datetime, timedelta
import hashlib

def string_to_sha256_hex(string):
    sha_signature = hashlib.sha256(string.encode()).hexdigest()
    return sha_signature

# start time 1. Januar 1900.
date = datetime(1900, 1, 1)

# open textfile
textFileName = f"{'allDates2hex'}.txt"

with open(textFileName, 'w') as f:

    # loop until now

    while date <= datetime.now():

        # different formats

        f.write(string_to_sha256_hex(str(date.strftime("%d.%m.%Y"))))  # DD.MM.YYYY
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%Y.%m.%d"))))  # YYYY.MM.DD
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%m.%d.%Y"))))  # MM.DD.YYYY
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%Y-%m-%d"))))  # YYYY-MM-DD
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%d-%m-%Y"))))  # DD-MM-YYYY
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%d-%m-%y"))))  # DD-MM-YYYY
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%m/%d/%y"))))  # MM/DD/YY
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%d/%m/%y"))))  # DD/MM/YY
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%d/%m/%Y"))))  # DD/MM/YYYY
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%m/%d/%Y"))))  # MM/DD/YYYY
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%A, %B %d, %Y"))))  # Monday, January 01, 1900
        f.write('\n')
        f.write(string_to_sha256_hex(str(date.strftime("%B %d, %Y"))))  # January 01, 1900
        f.write('\n')

        nextDay = date + timedelta(days=1)
        dateInSeconds= date
        
        while dateInSeconds < nextDay:
            
            f.write(string_to_sha256_hex(str(dateInSeconds)))
            f.write('\n')
            # Increment current date by one second
            dateInSeconds += timedelta(seconds=1)
        
        
        # add next day

        date += timedelta(days=1)