#!/usr/bin/python3
import requests
import datetime

class Dynu:
    def __init__(self) -> None:
        self.now                = datetime.datetime.now()
        self.public_ip          = ""
        self.ifconfig_endpoint  = "http://ifconfig.me"

        self.dynu_ipv4          = ""
        self.dynu_endpoint      = "https://api.dynu.com/v2/dns/"
        self.dynu_id            = 10000
        self.dynu_hostname      = "YOUR_HOSTNAME"
        self.dynu_api_key       = "YOUR_API_KEY"
        
        self.header = {
                        'accept': 'application/json',
                        'Content-Type': 'application/json',
                        'API-Key': self.dynu_api_key
                      }

    def _get_public_ip(self):
        res = requests.get(self.ifconfig_endpoint)
        self.public_ip = res.text

    def _get_data_from_dynu(self):
        res = requests.get(self.dynu_endpoint, headers=self.header)
        data = res.json()
        for domain in data['domains']:
            if domain['id'] == self.dynu_id:
                self.dynu_ipv4 = domain['ipv4Address']

    def _is_different(self):
        if self.dynu_ipv4 == self.public_ip:
            return False
        else:
            return True
    
    def _update(self):
        json_data = {
           "name": self.dynu_hostname,
           "ipv4Address": self.public_ip,
           "ipv6Address": "",
           "ttl": 90,
           "ipv4": "true",
           "ipv6": "false",
           "ipv4WildcardAlias": "true",
           "ipv6WildcardAlias": "false",
           "allowZoneTransfer": "false",
           "dnssec": "false"
        }
        dynu_endpoint = self.dynu_endpoint + str(self.dynu_id)
        res = requests.post(dynu_endpoint, headers=self.header, json=json_data)
        if res.status_code == 200:
            print("{} : [+] Updated from {} -> {} !".format(self.now, self.dynu_ipv4, self.public_ip))

    def process(self):
        self._get_public_ip()
        self._get_data_from_dynu()
        if self._is_different():
            self._update()
        else:
            print("{} : [-] Nothing to change.".format(self.now))

def main():
    ddns = Dynu()
    ddns.process()

if __name__ == "__main__":
    main()
