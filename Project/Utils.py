import os

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 'Something Wrong'


def Screen_cleaner():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
