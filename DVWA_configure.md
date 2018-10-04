# DVWA

1.下载dvwa

http://www.dvwa.co.uk

2.配置apache，目录`/etc/apache2/httpd.conf`添加

```
<VirtualHost *:80>
DocumentRoot "/Users/liurenwan/Downloads/DVWA"
ServerName dvwa.localhost
    <Directory "/Users/liurenwan/Downloads/DVWA">
     Options Indexes FollowSymLinks
     AllowOverride All
     allow from all
     Require all granted
     </Directory>
</VirtualHost>
```

</Directory>标签下 `Require all granted`



2.修改 `/etc/hosts`,添加

```
127.0.0.1 dvwa.localhost
```

3.出错的话，error_log目录

```
/var/log/apache2
```

注：`because search permissions are missing on a component of the path,`可以通过修改dvwa安装目录路径上的权限解决

4.`DVWA/config/config.inc.php.dist`复制一份，将文件名修改为`DVWA/config/config.inc.php`

5.修改`DVWA/config/config.inc.php`

```php
$_DVWA[ 'db_server' ]   = '127.0.0.1';
$_DVWA[ 'db_database' ] = 'dvwa';
$_DVWA[ 'db_user' ]     = 'root';
$_DVWA[ 'db_password' ] = '';

# Only used with PostgreSQL/PGSQL database selection.
$_DVWA[ 'db_port '] = '3306';
```



6.重启apache

```
apachectl restart
```

7.检查配置文件语法

```
apachectl configtest
```



成功 

```
ping dvwa.localhost
```

web中

```
dvwa.localhost
```

