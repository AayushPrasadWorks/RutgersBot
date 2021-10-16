import sqlite3
import time
import timeit
import requests


def get_all_subjects():
    l = 'https://sis.rutgers.edu/soc/subjects.json?semester=92016&campus=NB&level=U'
    r = requests.get(l).json()
    subjects = []

    for c in r:
        subjects.append(c['code'])

    return subjects