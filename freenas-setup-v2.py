import json
import requests

hostname='192.168.1.131'
adminusername='root'
adminpassword='zen67ume'

##########################################################################################################################

def get_users_ids():
    r = requests.get('http://192.168.1.177/api/v2.0/user/',auth=('root', 'zen67ume'),headers={'Content-Type': 'application/json'},verify=False)
    users = json.loads(r.text)
    numusers = len(users)
    for x in range(1, numusers):
        print (users[:numusers][x]["id"])


def get_groups():
    r = requests.get('http://'+hostname+'/api/v2.0/group/',auth=(adminusername, adminpassword),headers={'Content-Type': 'application/json'},verify=False)
    groups = json.loads(r.text)
    for group in groups:
        print ( group["group"] + "(" + str(group["id"]) + ")")

def create_group(groupname):
    r = requests.post('http://'+hostname+'/api/v2.0/group/',auth=(adminusername, adminpassword),headers={'Content-Type': 'application/json'},verify=False,data=json.dumps(
    {
      "name": groupname,
      "sudo": False,
      "allow_duplicate_gid": False,
    }))
    print (r.text)

def get_groupid(groupname):
    r = requests.get('http://'+hostname+'/api/v2.0/group/',auth=(adminusername, adminpassword),headers={'Content-Type': 'application/json'},verify=False)
    groups = json.loads(r.text)
    for group in groups:
        if (group["group"] == groupname):
            return str(group["id"])
        # print ( group["group"] + "(" + str(group["id"]) + ")")    

def create_user(username,fullname,password,group):
    r = requests.post('http://'+hostname+'/api/v2.0/user',auth=(adminusername, adminpassword),headers={'Content-Type': 'application/json'},verify=False,data=json.dumps(
    {                 
    # "userid": "1002",
    "username": username,
    # "group": username,
    "group_create": True,
    #"home": "string",
    #"home_mode": "string",
    #"shell": "string",
    "full_name": fullname,
    # "email": "string",
    "password": password,
    # "password_disabled": True,
    # "locked": True,
    # "microsoft_account": False,
    # "smb": True,
    # "sudo": True,
    # "sshpubkey": "string",
    "groups": [get_groupid(group)],
    # "attributes": {
    #     "additionalProp1": {}
    # }
    }))
    print (r.text)

def add_user_to_group(user,group):
    print (user + ":" + group)

def create_dataset(pool, datasetname):
    r = requests.post('http://'+hostname+'/api/v2.0/pool/dataset/',auth=(adminusername, adminpassword),headers={'Content-Type': 'application/json'},verify=False,data=json.dumps(
    {
    "name": pool+"/"+datasetname,
    "type": "FILESYSTEM",
    # "volsize": 5120,
    # "volblocksize": "512",
    # "sparse": true,
    # "force_size": true,
    # "comments": "string",
    # "sync": "STANDARD",
    # "compression": "OFF",
    # "atime": "ON",
    # "exec": "ON",
    # "managedby": "string",
    # "quota": 0,
    # "quota_warning": 0,
    # "quota_critical": 0,
    # "refquota": 0,
    # "refquota_warning": 0,
    # "refquota_critical": 0,
    # "reservation": 0,
    # "refreservation": 0,
    # "special_small_block_size": 0,
    # "copies": 0,
    # "snapdir": "VISIBLE",
    # "deduplication": "ON",
    # "readonly": "ON",
    # "recordsize": "512",
    # "casesensitivity": "SENSITIVE",
    # "aclmode": "PASSTHROUGH",
    # "share_type": "GENERIC",
    # "xattr": "ON",
    # "encryption_options": {
    #     "generate_key": true,
    #     "pbkdf2iters": 0,
    #     "algorithm": "AES-128-CCM",
    #     "passphrase": "string",
    #     "key": "string"
    # },
    # "encryption": true,
    # "inherit_encryption": true
    }))
    print (r.text)

# get_groups()
# create_group("mightynein")
# create_user("beau","Beauregard Lionett","P@ssw0rd")
# create_user("emily","emily chalmers","P@ssw0rd","family")

create_dataset("tank","campaign2")
