# high

## 分析源码

源码在`/DVWA/vulnerabilities/exec/source/high.php`中

![high_source_code](image/high_source_code.png)

可以从源码中看出，高级别模式进一步完善了黑名单，看似过滤了所有的非法字符，但注意到是把`'| '`(|后有一个空格)替换成空字符，那么`|`依然有用



## 命令注入

![high0](image/high0.png)

