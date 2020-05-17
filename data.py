from datetime import datetime
import os

class KADAI(object):

    def __init__(self, name, year, month, day, hour, minute):

        self.name = name
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.timestamp = datetime(year, month, day, hour, minute).timestamp()

# 读取数据的函数，参数是文件地址
def read_data(address):
    global kadai

    def inpl(): return list(map(str, f.readline().split()))

    # 没有的话创建一个
    try:
        f = open(address, 'r')
    except IOError:
        f = open(address, 'w')
        f.close()
        f = open(address, 'r')

    kadai = []

    while True:

        tem = inpl()

        # 如果读取到末尾
        if not tem:
            break

        kadai.append(KADAI(tem[0], int(tem[1]), int(tem[2]), int(tem[3]), int(tem[4]), int(tem[5])))

    f.close()

# 按时间顺序从近到远排序
def sort_kadai():
    global kadai
    kadai.sort(key=lambda kadai: kadai.timestamp, reverse=False)

# 保存数据的函数，参数是文件地址
def save_data(address):
    global kadai

    sort_kadai()

    f = open(address, 'w')
    for data in kadai:
        f.write(str(data.name) + ' ' + str(data.year) + ' ' + str(data.month)
                + ' ' + str(data.day) + ' ' + str(data.hour) + ' ' + str(data.minute)
                + ' ' + str(data.timestamp) + '\n')
    f.close()

# 向库里添加某项
def add(args, address):
    global kadai

    read_data(address)
    def inpl(): return list(map(str, args.split()))
    tem = inpl()
    kadai.append(KADAI(tem[0], int(tem[1]), int(tem[2]), int(tem[3]), int(tem[4]), int(tem[5])))
    save_data(address)

# 在库里删除某项
def delete(target, address):
    global kadai

    read_data(address)
    for i in kadai:
        if i.name == target:
            kadai.remove(i)
            save_data(address)
            return 1
    return 0

# 全部清除
def clear(target, address):
    pass

# 个位数的分秒左加零
def append_zero(num):
    num = int(num)
    if num >= 0 and num <= 9:
        return '0' + str(num)
    else:
        return str(num)

# 对象KADAI的list, 用于数据中转
kadai = []
