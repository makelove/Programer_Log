# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 11:56
# @File    : add-host-ip.py


"""
add-host-ip.py:
自动添加/etc/hosts 域名绑定IP
"""

import requests


def 查询全球DNS(host):
    import requests


    headers = {
        'authority': 'www.gdnspc.com',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'dnt': '1',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.gdnspc.com/',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': '__cfduid=d7f182d3c5a68e71c2a9902c472e8a3631608433922; _ga=GA1.2.1900327867.1608433937; _gid=GA1.2.337357370.1608433937; __gads=ID=6af39aca34d98035-22caac9a43c50018:T=1608433936:RT=1608433936:S=ALNI_MaE5H6FI7G_xbl_V_rJex291IiUkw; PHPSESSID=468b4c4c7f252da4308788b995996134',
    }


    params = (
            ('s', '162'),
            ('t', 'A'),
            ('q', 'raw.githubusercontent.com'),
            ('k', 'AyaEUoRPnk5yximSDQFBow2FGoM91qP1'),
            ('r', '1608534545-CFbFIYp4MCn78Beb'),
        )

    response = requests.get('https://www.gdnspc.com/api/checker', headers=headers, params=params)
    js = response.json()
    return js['result'][0]['record']

    pass
def 查询全球DNS2(host):
    headers = {
        'authority': 'www.whatsmydns.net',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'accept': 'application/json, text/plain, */*',
        'dnt': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.whatsmydns.net/',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': '__cfduid=dd845ca2c0dae8ef04fade64da42aa53d1608433918; _ga=GA1.2.864067538.1608433921; _gid=GA1.2.1694506165.1608433921; __gads=ID=7c02c0ed2adccebb:T=1608527151:S=ALNI_MYn8MpuX26lqec-GtWHF_fWoSR1qA; _gat=1',
    }

    params = (
        ('server', '343'),
        ('type', 'A'),
        ('query', host,),  # 'hide.me'
    )

    response = requests.get('https://www.whatsmydns.net/api/details', headers=headers, params=params)
    js = response.json()
    return js['data'][0]['response'][0] #js['result'][0]['record']

    pass


import socket


def 检查本地能否连接该IP(ip, host):  # OK
    from requests.exceptions import ConnectTimeout,ConnectionError
    from requests_toolbelt.adapters import host_header_ssl
    s = requests.Session()
    s.mount('https://', host_header_ssl.HostHeaderSSLAdapter())

    headers = {
        "Host": host,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }
    # rs = s.get("https://"+ip, headers={"Host": host})
    try:
        rs = s.get(f"https://{ip}/", headers=headers, timeout=4, verify=False,allow_redirects=False)
        print(rs.status_code, rs.headers)

    except ConnectTimeout as e:
        return False
    except Exception as e:
        print(e)


    return True

    pass


def 检查本地能否连接该IP1(ip):
    # import socket
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # try:
    #     s.connect((ip, 80))
    #     print("Port 80 reachable")
    # except socket.error as e:
    #     print("Error on connect: %s" % e)
    # s.close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((ip, 80))
            print("Port 80 reachable")
            return True
        except socket.error as e:
            print("Error on connect: %s" % e)
            return False


def 检查本地能否连接该IP2(ip):
    try:
        socket.gethostbyaddr(ip)
    except socket.herror:
        print(u"Unknown host 连接不上")
        return False
    return True
    pass


def main(url):
    # 查询 全球DNS
    # 获取 服务器IP
    from urllib.parse import urlparse
    host = urlparse(url).netloc
    print('host:',host)
    ip = 查询全球DNS(host)
    # 检查本地能否连接该IP
    print('检查本地能否连接该IP')
    print('-'*40)
    tf = 检查本地能否连接该IP(ip, host)
    print('-'*40)
    # ip='151.101.124.133'
    # tf=True

    # 写入/etc/hosts
    if tf:
        print('写入/etc/hosts')
        # Root 用户
        from python_hosts import Hosts, HostsEntry
        hosts = Hosts(path='/etc/hosts')
        new_entry = HostsEntry(entry_type='ipv4', address=ip, names=[host])
        hosts.add([new_entry])
        hosts.write()
        pass
    else:
        print('该IP不能连接', ip)
    pass


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        url = sys.argv[1]
        main(url)
    else:
        print('添加url')

    # 检查本地能否连接该IP('8.7.198.46', 'google.com')
    # 检查本地能否连接该IP('174.138.52.82', 'hide.me')
    # 检查本地能否连接该IP('151.101.52.133', 'raw.githubusercontent.com')
