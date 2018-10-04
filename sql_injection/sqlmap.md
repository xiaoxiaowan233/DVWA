# sqlmap

1.查看帮助

```
python2.7 sqlmap.py -h
```

2.测试url



```
python2.7 sqlmap.py -u "http://dvwa.localhost/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="PHPSESSID=sm4ui6j4hros62n7vie2c845m3; security=low" 
```



保存请求头到`test.txt`，依然可以测试url

```
python2.7 sqlmap.py -r test.txt  
```

