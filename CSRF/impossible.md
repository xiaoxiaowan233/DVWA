# impossible

在安全级别为impossible中，修改密码需要输入当前的密码，因此如果攻击者不知道原密码，也就无法完成CSRF攻击

![impossible0](image/impossible0.png)

观察正常用户修改的报文：请求行包括原密码 + 新密码 + 确认新密码 + 防止CSRF攻击的token

![impossible1](image/impossible1.png)