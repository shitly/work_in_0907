import sys
from os.path import dirname, abspath
import pymysql
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='112233..',
    db='ip4',
    charset='gbk',
)

## 二分查找, 当找不到的时候就返回 前面一个值的
def BinnaySerach(ls, m):
    low_index = 0
    high_index = len(ls) - 1

    while (low_index <= high_index):
        mid_index = int(low_index + 0.5 * (high_index - low_index))
        midval = ls[mid_index]

        if midval < m:
            low_index = mid_index + 1
        elif midval > m:
            high_index = mid_index - 1
        else:
            return ls[mid_index]

    return ls[high_index]

def trans_int_index(s):
    t = [int(x) for x in s.split(".")]
    return (10 ** 6) * t[0] + (10 ** 3) * t[1] + t[2]

def main(get):
    get_index = trans_int_index(get)
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='112233..',
        db='ip4',
        charset='gbk',
    )

    corsor = conn.cursor()
    corsor.execute('''select start_ip from ips;''')
    indexs = []
    temp_dic = {}
    for ip in corsor.fetchall():
        index = trans_int_index(ip[0])
        indexs.append(index)
        temp_dic.setdefault(index, ip[0])

    # indexs = np.sort(indexs)
    gaim_index = BinnaySerach(indexs, get_index)
    corsor.execute('''select location from ips where start_ip = '%s';''' % temp_dic[gaim_index])
    res = corsor.fetchall()[0][0]
    corsor.close()
    conn.close()
    return {
        "ip": get,
        "location": res,
    }
