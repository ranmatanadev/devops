from Utils import BAD_RETURN_CODE, SCORES_FILE_NAME


def add_score(level):
    try:
        score = (level * 3) + 5
        my_file = open(SCORES_FILE_NAME, "a")
        my_file.close()
        my_file = open(SCORES_FILE_NAME, "r")
        lines = my_file.readline()
        if len(lines) > 0:
            my_file = open(SCORES_FILE_NAME, "w")
            my_file.write(str(int(lines) + score))
        else:
            my_file = open(SCORES_FILE_NAME, "w")
            my_file.write(str(score))
        my_file.close()

    except:
        print(BAD_RETURN_CODE)
