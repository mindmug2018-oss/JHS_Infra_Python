
import re


if __name__ == '__main__':
    user_id = input('Enter ID (Letter, numbers possible):')
    pattern = r'^[a-zA-Z0-9]+$'

if re.search(pattern, user_id):
    print('Entered well')
else:
    print("Invalid Entry")