# impossible

## 源码分析

源码在`/DVWA/vulnerabilities/exec/source/impossible.php`中

![impossible_source_code](image/impossible_source_code.png)

源码中有防止CSRF攻击的token，同时将输入ip分为4个部分，对输入进行了严格的检查，只有`数字.数字.数字.数字`的命令才会被接受，不存在命令注入攻击