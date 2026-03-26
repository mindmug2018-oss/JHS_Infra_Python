import re

if __name__ == '__main__':
    
    input_id = input('(Please Enter Your ID, Put Letters within 5-10, no special characters):')

    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,9}$'

    if re.search(pattern, input_id):
        print('Entered well')

    else:
        print("Invalid Entry")