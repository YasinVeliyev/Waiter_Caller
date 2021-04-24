import os
import requests
data = {
  "domain": "bit.ly",  
  "title": "Bitly API Documentation",  
  "group_guid": "Ba1bc23dE4F",  
  "long_url": "https://dev.bitly.com"  
}
ROOT_URL = "https://api-ssl.bitly.com/v4/shorten"
print( os.environ.get('bitly'))
headers = {
    'Authorization': 'Bearer {d16600ae06108d9be87c8400f0cce98744427371}',
    'Content-Type': 'application/json',
}
class BitlyHelper:
    def shorten_url(self, long_url):
        data = {"domain": "bit.ly",  
            "group_guid": "o_34r1bt4jc9",  
            "long_url": long_url  }
        try:
            res = requests.post(ROOT_URL, headers=headers, data = data)
            print(res.json())
        except Exception as e:
            print(e)

bit = BitlyHelper()
bit.shorten_url('yasinv.site/hello')