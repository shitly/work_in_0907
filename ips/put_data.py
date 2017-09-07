
def get_data():
    with open("./data/source.txt") as f:
        lines = f.readlines()
        f.close()
    return lines

def str_to_item(s):
    import re
    partern = "(.*?)\\s+(.*?)\\s+(.*)"
    return re.findall(partern, s)[0]


def set_django():
    import os
    from os.path import join, dirname, abspath
    PROJECT_DIR = dirname(dirname(abspath(__file__)))
    import sys
    sys.path.insert(0, PROJECT_DIR)

    import django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "minicms.settings")
    django.setup()


def create_sourceIp():
    set_django()
    # from ips.models import SourceIps
    data = get_data()
    ip_lists = []
    i = 0
    for x in data:
        try:
            t = str_to_item(x)
            try:
                # SourceIps.objects.get_or_create(start_ip=t[0], end_ip=t[1], location=t[2])
                print("已经插入第 " + str(i) + " 条数据")
                i += 1
            except :
                print(x)
        except :
            print("第一重错误" + x)

    print("已经插入完" + str(i) + "条数据")


def write_csv():
    data = get_data()
    res = []
    for x in data:
        try:
            t = str_to_item(x)
            try:
                res.append(list(t))
            except:
                print(x)
        except:
            print("第一重错误" + x)

    import pandas as pd
    df = pd.DataFrame(res, columns=["start_ip", "end_ip", "location"])
    df.to_csv("data.csv")


if __name__ == "__main__":
    # create_sourceIp()
    # create_index()
    # write_to_txt()
    import pandas as pd
    df = pd.read_csv("data.csv", encoding="gbk")
    print(df)

