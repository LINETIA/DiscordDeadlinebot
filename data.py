from datetime import datetime

class Deadline(object):

    def __init__(self, name, year, month, day, hour, minute):

        self.name = name
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.timestamp = datetime(year, month, day, hour, minute).timestamp()

def read_data():
    global kadai

    def inpl(): return list(map(str, f.readline().split()))

    f = open('data.txt', 'r')

    kadai = []

    while True:

        tem = inpl()

        if not tem:
            break

        kadai.append(Deadline(tem[0], int(tem[1]), int(tem[2]), int(tem[3]), int(tem[4]), int(tem[5])))

    f.close()

def sort_kadai():
    global kadai
    kadai.sort(key=lambda kadai: kadai.timestamp, reverse=False)

def save_data():
    global kadai

    sort_kadai()

    f = open('data.txt', 'w')
    for data in kadai:
        f.write(str(data.name) + ' ' + str(data.year) + ' ' + str(data.month)
                + ' ' + str(data.day) + ' ' + str(data.hour) + ' ' + str(data.minute)
                + ' ' + str(data.timestamp) + '\n')
    f.close()

def add(tem):
    global kadai

    kadai.append(Deadline(tem[0], int(tem[1]), int(tem[2]), int(tem[3]), int(tem[4]), int(tem[5])))
    save_data()

def delete(target):
    for i in kadai:
        if i.name == target:
            kadai.remove(i)
            save_data()
            return 1
    return 0

def append_zero(num):
    num = int(num)
    if num >= 0 and num <= 9:
        return '0' + str(num)
    else:
        return str(num)

kadai = []
