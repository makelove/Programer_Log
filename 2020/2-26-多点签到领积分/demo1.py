# -*- encoding: utf-8 -*-
'''
@File    :   demo1.py
@Time    :   2020/02/26 15:57:31
@Desc    :   
'''
import requests


def main():
    rs = requests.get("https://appapis.dmall.com/static/userIsCheckIn.jsonp?callback=jQuery22304504064425163671_1582705578650&venderId=1&_=1582705578651",
                      headers={
                          "Accept": "*/*",
                          "Accept-Language": "zh-cn",
                          "Host": "appapis.dmall.com",
                          "Referer": "https://act.dmall.com/dac/signIn/index.html?dmShowTitleBar=false&dmfrom=wx&bounces=false&dmTransStatusBar=true",
                          "User-Agent": "Mozilla/5.0 (iPod touch; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148Dmall/4.4.7"
                      },
                      cookies={
                          "_utm_id": "42631642",
                          "addr": "%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E4%B8%89%E7%BB%93%E4%B9%89%E9%BA%BB%E8%BE%A3%E9%BE%99%E8%99%BE%E9%94%A1%E7%BA%B8%E7%83%A7%E7%83%A4",
                          "addrId": "",
                          "appMode": "online",
                          "appVersion": "4.4.7",
                          "areaId": "110108",
                          "bigdata": "",
                          "businessCode": "2",
                          "community": "%E4%B8%89%E7%BB%93%E4%B9%89%E9%BA%BB%E8%BE%A3%E9%BE%99%E8%99%BE%E9%94%A1%E7%BA%B8%E7%83%A7%E7%83%A4",
                          "console_mode": "0",
                          "data_seq": "4",
                          "env": "app",
                          "first_session_time": "1574310210261",
                          "grayStoreId": "11480",
                          "inited": "true",
                          "lat": "40.043306",
                          "lng": "116.185492",
                          "platform": "IOS",
                          "session_id": "66509D2F16AC414399D5FBF955E31E78",
                          "storeGroupV4": "1-11480-1,2-11480-1,1-12672-86",
                          "store_id": "11480",
                          "tdc": "",
                          "tempid": "C8AF4E0FA1D00002B22A17C019BDDDD0",
                          "ticketName": "4484988D798A580F36FBF8455694C40250224A91CB8226F4B464582A6ADE8352947EA08F0657D8645D6D3041216E08E8E78F004AB9A14CAAC4BEACBC5C04C8990EF1D08CCA0B8B55295C1C8D938B8443377C2EECF18F2EC1A9871D44BBB01CA12135F3AC155D0B0E85A8F0C31A8FDAEFA297180361FBAEC03B90BE4AB177D191",
                          "token": "12b731cd-27df-4ab5-b9c4-70bcf628b5fc",
                          "updateTime": "1581561484000",
                          "uuid": "ad5335126ca7762dd08ed9fafc49634de7834f51",
                          "vender_id": "1",
                          "web_session_count": "32"
                      },
                      )
    print(rs)
    print(rs.headers)
    print('-'*30)
    print("Text",rs.text)
    pass


if __name__ == "__main__":
    main()
    pass
