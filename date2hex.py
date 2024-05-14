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

        f.write(string_to_sha256_hex(str(date.strftime("%d.%m.%Y"))) + '\n')  # DD.MM.YYYY
        f.write(string_to_sha256_hex(str(date.strftime("%Y.%m.%d"))) + '\n')  # YYYY.MM.DD
        f.write(string_to_sha256_hex(str(date.strftime("%m.%d.%Y"))) + '\n')  # MM.DD.YYYY
        f.write(string_to_sha256_hex(str(date.strftime("%Y-%m-%d"))) + '\n')  # YYYY-MM-DD
        f.write(string_to_sha256_hex(str(date.strftime("%d-%m-%Y"))) + '\n')  # DD-MM-YYYY
        f.write(string_to_sha256_hex(str(date.strftime("%d-%m-%y"))) + '\n')  # DD-MM-YYYY
        f.write(string_to_sha256_hex(str(date.strftime("%m/%d/%y"))) + '\n')  # MM/DD/YY
        f.write(string_to_sha256_hex(str(date.strftime("%d/%m/%y"))) + '\n')  # DD/MM/YY
        f.write(string_to_sha256_hex(str(date.strftime("%d/%m/%Y"))) + '\n')  # DD/MM/YYYY
        f.write(string_to_sha256_hex(str(date.strftime("%m/%d/%Y"))) + '\n')  # MM/DD/YYYY
        f.write(string_to_sha256_hex(str(date.strftime("%A, %B %d, %Y"))) + '\n')  # Monday, January 01, 1900
        f.write(string_to_sha256_hex(str(date.strftime("%B %d, %Y"))) + '\n')  # January 01, 1900

        nextDay = date + timedelta(days=1)
        dateInSeconds= date
        
        while dateInSeconds < nextDay:
            
            f.write(string_to_sha256_hex(str(dateInSeconds)) + '\n')
            # Increment current date by one second
            dateInSeconds += timedelta(seconds=1)
        
        
        # add next day

        date += timedelta(days=1)
