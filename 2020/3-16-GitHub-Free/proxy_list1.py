# -*- encoding: utf-8 -*-
'''
@File    :   proxy_list1.py
@Time    :   2020/03/16 10:32:51
@Author  :   play4fun
@Desc    :   
'''

import requests
import shelve
from verify_proxy import verify
from time import sleep

dbp = 'proxy_list1'


def main():
    pList = get_proxy()
    # with shelve.open(dbp) as db:
    #     # pList = db.get('pList', get_proxy())
    #     pList = db.get('pList', [])
    print('-' * 40)

    proxy_list = [f'{d["protocol"]}://{d["ip"]}:{d["port"]}' for d in pList]
    rsl = map(verify, proxy_list)
    rsl2 = filter(lambda x: x[0] is True, rsl)
    rsl3 = sorted(rsl2, key=lambda x: x[2])

    print('-' * 40)
    print('合格代理:', len(rsl3))
    print(rsl3)
    with shelve.open(dbp) as db:  # 保存下来
        db['verifyed'] = rsl3
    pass



def get_proxy():
    pList = []
    for i in range(1, 11):
        sleep(2)#并发限制
        url = f'https://www.freeip.top/api/proxy_ips?country=%E4%B8%AD%E5%9B%BD&page={i}&order_by=validated_at&order_rule=DESC'
        try:
            rs = requests.get(url)
            js = rs.json()
        except Exception as e:
            print(e)
            continue

        l1 = [d for d in js['data']['data'] if d['protocol'] == 'https']  # 只需要https代理
        pList += l1

        # break
    with shelve.open(dbp) as db:
        db['pList'] = pList
        print('获取到https代理:', len(pList))
    return pList


if __name__ == "__main__":
    main()
