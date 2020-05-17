import json
import requests

# Get all users
# r = requests.get('http://192.168.1.177/api/v2.0/user/',auth=('root', 'zen67ume'),headers={'Content-Type': 'application/json'},verify=False)

# Get infomation about a specific user
# r = requests.get('http://192.168.1.177/api/v2.0/user/id/36/',auth=('root', 'zen67ume'),headers={'Content-Type': 'application/json'},verify=False)
# print (r.text)

def get_user_info():
    r = requests.get('http://192.168.1.177/api/v2.0/user/id/30/',auth=('root', 'zen67ume'),headers={'Content-Type': 'application/json'},verify=False)
    print (r.text)

def get_users_ids():
    r = requests.get('http://192.168.1.177/api/v2.0/user/',auth=('root', 'zen67ume'),headers={'Content-Type': 'application/json'},verify=False)
    users = json.loads(r.text)
    numusers = len(users)
    for x in range(1, numusers):
        print (users[:numusers][x]["id"])

def get_users_fullname():
    r = requests.get('http://192.168.1.177/api/v2.0/user/',auth=('root', 'zen67ume'),headers={'Content-Type': 'application/json'},verify=False)
    users = json.loads(r.text)
    numusers = len(users)
    for x in range(0, numusers):
        print (users[:numusers][x]["full_name"])

def get_username(userid):
    r = requests.get('http://192.168.1.177/api/v2.0/user/id/' + userid + '/',auth=('root', 'zen67ume'),headers={'Content-Type': 'application/json'},verify=False)
    user = json.loads(r.text)
    print (user["username"])
    # print( type(user) )
    # thisdict["year"] = 2018

# get_users_ids()
# get_user_info()
# get_users_fullname()

get_username("30")
