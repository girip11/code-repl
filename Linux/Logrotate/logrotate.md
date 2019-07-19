# Logrotate basics
Logrotate utility in linux is used to rotate log files. This utility has the following features like 
* log rotation based on size or time criteria or both. 
* old logs can be configured to be stored in a compressed way,
* logs that are about to be removed can also be mailed.
* custom periodic log rotation by integrating with cron

> Normally, logrotate is run as a daily cron job. It will not modify a log multiple times in one day unless the criterion for that log is based on the log's size and logrotate is being run multiple times each day, or unless the -f or --force option is used. 

logrotate usually stores the state either at **/var/lib/logrotate.status** or at **/var/lib/logrotate/status**

We can create our own cron entries to run the logrotate with custom period, for instance every hour and forcing rotation.
In that case, we can tend to store the state of the logrotate in a different state

## Installation
```Bash
apt install logrotate -y
```

## logrotate commonly used options
```Bash
# Help for options supported by logrotate
logrotate --help

# version
logrotate --version

# debug a logrotate with new configuration
# This command doesn't do the actual logrotate but
# can be used to simulate with verbose logs what would happen
# if logrotate was run with this configuration
logrotate -d <logrotate_config_file>

# running a manual logrotate
logrotate --force --verbose <logrotate_config_file>
# shorthand command
logrotate -vf <logrotate_config_file>

# run logrotate with custom state file
# used in cases where logrotate is run as different user who doesnot belong to root
# Default state file location is /var/lib/logrotate.status or /var/lib/logrotate/status 
# which has write permissions only to root user
# or users belonging to root group. 
logrotate -vf -s <path_to_state_file> <logrotate_conf_file>
```


## Directory structure
Directories relevant to logrotate are (unless logrotate is installed to custom location)
* logrotate location - **/usr/sbin/logrotate**
* Configuration file - **/etc/logrotate.conf**
* Configuration directory - **/etc/logrotate.d/**
* Default status file - **/var/lib/logrotate.status or /var/lib/logrotate/status**

## Configuring log rotate
Usually custom logrotate configuration files are placed at **/etc/logrotate.d**.
```Bash
# Sample logrotate configuration file.
# global options for all below mentioned configuration go here

/var/log/web_server/* {
  # logrotate options
}

/var/log/rails_server/* {
  # logrotate options
}
```
Some of the important logrotate configuration options are
* log rotate period values are **daily, weekly, monthly and yearly**
* **size <size>** - Default unit is bytes. K - KB, M- MB and G - GB. Size and timeperiod are mutually exclusive. Either size or timeperiod will be honoured.
* **minsize and maxsize** - introduced from 3.8.1, considers size and timeperiod for log rotation.
* **compress** - compress rotated files
* **delaycompress** - dont compress the just rotated log file.
* **rotate <n>** - recent n rotated files will be kept. Old files are deleted.
* **prerotate .. endscript** - block containing shell(/bin/sh) script. Executed before each log file to be rotated. **sharedscript** option makes the script execute once for all log files to be rotated. This script recieves log file absolute path or pattern as argument.
* **postrotate .. endscript** - similar to prerotate, except executed after the log file rotation
* **firstaction .. endscript** - Executed before prerotate script only once irrespective of number of log files rotated.
* **lastaction ..endscript** - Executed after postrotate script only once irrespective of number of log files rotated.
* **copy** - This option makes **create** option useless. copy the log file without changing original log file, thus snapshotting the log file.
* **copytruncate** - copy current log file to another file and truncate the current file. Helps in cases where file handle cannot be closed by the program. This option makes **create** option useless.
* **create mode user group** - new log file created just after rotation with the same name.
* **dateext** - add date to rotated logs files
* **dateformat format_string** - when **dateext** is enabled, dateformat option helps to specify in the desired date format added to the rotated file name. Default format is "-%Y%m%d". %s adds seconds in epoch.
* **ifempty** - rotate log file even if its empty. Use  **notifempty** to avoid rotation on empty log files.
* **missingok** - gracefully proceed in the absence of log files.
* **extension <ext>** - makes the log file rotated as **logfile.i.ext.gz** (i is either number or dateformat, gz if compression is enabled)
* **start <n>** - log rotation file index starting value. Usually have it as 0. Becomes useless when **dateext** is mentioned.

Other useful options like **mailing**, **maxage** can be referred in the man page.

## Configuration examples
```Bash
# size based log rotate
/var/log/postgresql.log {
  compress
  size 100K
  rotate 5
  start 0
  missingok
  notifempty
  create 644 user user
  extension .log
}

# uses copy truncate. Useful in cases where script logs STDOUT redirected to file
/var/log/postgresql.log {
  compress
  daily
  rotate 5
  dateext
  dateformat -%Y-%m-%d
  missingok
  notifempty
  copytruncate
  # file get names as xyz-YYYY-MM-DD.log.gz
  extension .log
}
```

## Reference:
* [Logrotate man](https://linux.die.net/man/8/logrotate)
* [Manage log rotation](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/)