# https请求安全性，验证证书


- 启动 mitmproxy
    - 测试 
        - curl -k -x 127.0.0.1:8080 https://httpbin.org/ip
        - -k 表示 不检查https证书，不添加则请求失败

- Python
```
import requests
url='https://httpbin.org/ip'
proxy='http://127.0.0.1:8080'
proxies = {
    'http': proxy,
    'https': proxy,
}
rs = requests.get(url, proxies=proxies)
#报错 certificate verify failed

rs = requests.get(url)
rs.text
#正常

#取消证书验证
rs = requests.get(url, proxies=proxies,verify=False)
rs.text
#只会报警
InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
```
