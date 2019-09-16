# Mariadb installation notes

## Completely uninstall mysql related components and install mariadb
Mysql to mariadb migration has apparmor issues. So completely uninstall local mysql and install mariadb.
```Bash
# stop apparmor before purging mysql files
sudo systemctl stop apparmor.service
sudo update-rc.d -f apparmor remove

sudo apt-get remove --purge mysql-server mysql-client mysql-common
sudo apt-get autoremove
sudo apt-get autoclean
```

## Install mariadb
```Bash
sudo apt-get install mariadb-server

# start appramor if stopped
sudo systemctl start apparmor.service
sudo update-rc.d apparmor defaults
```

## Uninstall complete mariadb 
```Bash
sudo apt-get remove mariadb-server
sudo apt-get remove --auto-remove mariadb-server
sudo apt-get purge mariadb-server
sudo apt-get purge --auto-remove mariadb-server
```

## Checking mariadb version using mariadb CLI client
```Bash
#  below command will prompt for root user password (configured at the time of installation)
#  below command opens the mariadb CLI client
mysql -u root -p

# within the terminal, use the bewlo sql command to check the mariadb version.
select VERSION();
```

## Status, Start, Stop, restart mariadb service
Might need to run these as sudo
```Bash
#  status check
sudo systemctl status mariadb.service

#  start
sudo systemctl start mariadb.service

#  stop
sudo systemctl stop mariadb.service

# restart
sudo systemctl restart mariadb.service
```

## Checking mariadb logs for service startup failures
```Bash
# After starting/restarting with systemctl commands, if there are any failures, to look at the logs issue any of the below commands

# this command is more useful
dmesg | tail -30

# or 
journalctl -xe
```

## [Disabling apparmor for mariadb](https://www.cyberciti.biz/faq/ubuntu-linux-howto-disable-apparmor-commands/)
```Bash
# verify apparmor enabled for mysqld
# outputs like **/usr/sbin/mysqld** if apparmor is enabled
sudo apparmor_status | grep -i 'mysqld'

# below command can also be used for checking if apparmor is enabled.
cat /sys/kernel/security/apparmor/profiles | grep -i 'mysqld'

sudo echo "/usr/sbin/mysqld { }" > /etc/apparmor.d/usr.sbin.mysqld
ln -s /etc/apparmor.d/usr.sbin.mysqld /etc/apparmor.d/disable

sudo apparmor_parser -v -R /etc/apparmor.d/usr.sbin.mysqld

# verify disable using below command
sudo apparmor_status | grep -i 'mysqld'
```



## Resolving issues with apparmor
From the logs, if the issue is associated with apparmor service, follow the below steps.
```Bash
sudo echo "/usr/sbin/mysqld { }" > /etc/apparmor.d/usr.sbin.mysqld

cat /etc/apparmor.d/usr.sbin.mysqld

sudo apparmor_parser -v -R /etc/apparmor.d/usr.sbin.mysqld

sudo systemctl restart mariadb.service
```

> If you previously had MySQL installed, it activated an **AppArmor** profile which is incompatible with MariaDB. apt-get remove --purge only removes the profile, but does not deactivate/unload it. Only manually unloading it lets MariaDB work unhindered by AppArmor

## Settings required for Frappe/ERPNext development
Add below settings to **`/etc/mysql/my.cnf`** and restart the mariadb service.
```
[mysqld]
innodb-file-format=barracuda
innodb-file-per-table=1
innodb-large-prefix=1
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4
```

## Reference:
* [MariaDB uninstallation](https://gist.github.com/clonn/248570e787e487472619eeea0dde4df2)
* [Mariadb installation](https://linuxize.com/post/how-to-install-mariadb-on-ubuntu-18-04/)
* [MariaDB timeout issue](https://stackoverflow.com/questions/40997257/mysql-service-fails-to-start-hangs-up-timeout-ubuntu-mariadb)