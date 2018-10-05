# impossible

分析这一级别的源码

## 输入强检查

源码对输入进行强检查，这里采用了一系列PHP PDO的拓展函数进行了安全性能的提高，使用prepare，bindParam等对查询语句进行预设定和参数绑定，基本上杜绝SQL注入

![impossible0](image/impossible0.png)

![impossible1](image/impossible1.png)



## 防止CSRF攻击

![impossible2](image/impossible2.png)



## 限制错误次数

代码中对错误次数进行限制，错过3次，等待15分钟，基本杜绝暴力破解

![impossible2](image/impossible4.png)

![impossible3](image/impossible3.png)