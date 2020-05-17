
import json
import requests
r = requests.post(
  'https://172.16.35.129/api/v1.0/account/users/',
  auth=('root', 'zen67ume'),
  headers={'Content-Type': 'application/json'},
  verify=False,
  data=json.dumps({
       'bsdusr_uid': '1100',
       'bsdusr_username': 'aamyuser',
       'bsdusr_mode': '755',
       'bsdusr_creategroup': 'True',
       'bsdusr_password': '12345',
       'bsdusr_shell': '/usr/local/bin/bash',
       'bsdusr_full_name': 'Full Name',
       'bsdusr_email': 'name@provider.com',
   })
 )

print (r.text)