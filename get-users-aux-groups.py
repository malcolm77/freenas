import json
import requests

users = ['0','1','2','3','4','5','6','7','8','9','14','22','25','26','53','62','64','65','66','68','78','79','80','200','201','389','469','472','473','666','845','1000','1111','65534','8675309']

for user in users:
    r = requests.get(
    'http://192.168.1.177/api/v1.0/account/users/'+user+'/groups/',
    auth=('root', 'zen67ume'),
    headers={'Content-Type': 'application/json'},
    verify=False)
    print (user + ": " + r.text)

