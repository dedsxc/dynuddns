# dynuddns

Tool to update automatically ipv4 address linked to dynu ddns hostname (https://www.dynu.com/)

## Install

https://github.com/dedsxc/dynuddns

Modify variable
```py
self.dynu_id = your_hostname_id
self.dynu_hostname = "your_hostname"
self.api_key = "your_dynu_api_key" 
```

### Change access right
chmod 744 dynuddns.py

### Open cron
```sh
crontab -e
```
Launch the script every first day of the month at 1am
```sh
00 01 01 * * /path/to/dynuddns.py > dynuddns.log
```

## More information to use dynu API
https://www.dynu.com/Support/API
