[TOC]

# 暴力破解2

这一级别对用户输入进行了检查，一定程度上修复了部分sql注入漏洞，并且添加了

```php
// Login failed
		sleep( 2 );
		$html .= "<pre><br />Username and/or password incorrect.</pre>";
```

依然可以暴力破解，只是时间比较慢，按照low的方式破解即可



## 拦截报文

![medium_proxy_to_intruder](image/medium_proxy_to_intruder.png)

## 发送至intruder

![medium_intruder0](image/medium_intruder0.png)



## sniper

将密码设置为payload

![medium_sniper0](image/medium_sniper0.png)

设置字典

![medium_sniper1](image/medium_sniper1.png)

开始攻击，由于有了输入次数限制，攻击相对较慢，依然可以根据消息长度来判断正确的密码

![medium_sniper2](image/medium_sniper2.png)



## cluster bomb

攻击过称跟sniper一样，不再赘述