# 1 TASK
import random
import json


def file_creation(path_str):
    summary = {}
    for i in range(65, 91):
        some_int = random.randint(1, 100)
        with open(path_str + chr(i) + '.txt', 'w') as file:
            file.write(str(some_int))
        summary[chr(i) + '.txt'] = some_int
    with open(path_str + 'summary.txt', 'w') as summ:
        summ.writelines(json.dumps(summary, indent=4))

path_str = "\some_path\"
file_creation(path_str)


# 2nd TASK

def copy_content(path_str):
    with open(path_str + 'orig_file.txt', 'r') as origin:
        some_text = origin.read()
    with open(path_str + 'copy_file.txt', 'w') as copy:
        copy.write(some_text.upper())


path_str = "\some_path\"
copy_content(path_str)


# 3rd TASK


import csv
import random

players = ['Anton', 'Antonio', 'Antonidze', 'Anthony', 'Tony']


def get_scores():
    score = []
    for i in range(1, 101):
        for player in players:
            score.append([player, random.randint(1, 1000)])
    return score


def gen_csv(path_str, score):
    with open(path_str + 'score.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player name', 'Score'])
        writer.writerows(score)
        # for row in score:
        #     writer.writerow(row)


path_str = "\some_path\"
score_list = get_scores()
create_csv = gen_csv(path_str, score_list)


# 4th TASK

def read_csv(path_str):
    high_score = {}
    with open(path_str + 'score.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] in high_score:
                if row[1] > high_score[row[0]]:
                    high_score[row[0]] = row[1]
            else:
                high_score[row[0]] = row[1] 
    high_score = sorted([[name, score] for name, score in high_score.items()], key=lambda x: x[-1], reverse=True)
    return high_score


def gen_high(path_str, high_score):
    with open(path_str + 'high_score.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player name', 'Highest score'])
        writer.writerows(high_score)


path_str = '\\some_path\\'
highscore = read_csv(path_str)
gen_high(path_str, highscore)