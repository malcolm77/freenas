
import json
import requests
r = requests.post(
  'https://172.16.35.129/api/v1.0/account/users/',
  auth=('root', 'zen67ume'),
  headers={'Content-Type': 'application/json'},
  verify=False,
  data=json.dumps({
   # "id": "6841f242-840a-11e6-a437-00e04d680384",
    "msg": "method",
    "method": "pool.dataset.create",
    "params": [{
        "name": "loch/myuser",
        "comments": "Dataset for myuser"
    }]
})
 )

print (r.text)
