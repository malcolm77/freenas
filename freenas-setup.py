import argparse
import json
import sys

import requests


class Startup(object):

    def __init__(self, hostname, user, secret):
        self._hostname = hostname
        self._user = user
        self._secret = secret

        self._ep = 'http://%s/api/v1.0' % hostname

    def request(self, resource, method='GET', data=None):
        if data is None:
            data = ''
        r = requests.request(
            method,
            '%s/%s/' % (self._ep, resource),
            data=json.dumps(data),
            headers={'Content-Type': "application/json"},
            auth=(self._user, self._secret),
        )
        if r.ok:
            try:
                return r.json()
            except:
                return r.text

        raise ValueError(r)

    def create_pool(self,poolname,disks):
        self.request('storage/volume', method='POST', data={
            'volume_name': poolname,
            'layout': [
                {'vdevtype': 'stripe', 'disks': disks}, 
            ],
        })

    def create_dataset(self, poolname, datasetname):
        self.request('storage/volume/' + poolname + '/datasets', method='POST', data={
            'name': datasetname,
        })

    def create_cifs_share(self,poolname,datasetname,sharename):
        self.request('sharing/cifs', method='POST', data={
            'cifs_name': sharename,
            'cifs_path': '/mnt/'+poolname+'/'+datasetname,
            'cifs_guestonly': True
        })

    def service_start(self, name):
        self.request('services/services/%s' % name, method='PUT', data={
            'srv_enable': True,
        })

    def create_group(self, groupname):
       self.request('account/groups', method='POST', data=
        {
          "bsdgrp_gid": 1200,
          "bsdgrp_group": groupname
        })

    def create_user(self, username):
        self.request('account/users',method='POST',data=
        {
          "bsdusr_username": username,
          "bsdusr_creategroup": True,
          "bsdusr_full_name": "full name",
          "bsdusr_password": "P@ssw0rd",
          "bsdusr_uid": 1111,
          "bsdusr_group": 1200
        })

    def create_and_share_dataset(self, poolname, dataname):
        self.create_dataset(poolname,dataname)
        self.create_cifs_share(poolname,dataname,dataname)

    def run(self):
        diskset = ["ada0","ada1","ada2","ada4","ada4","ada5"]
        newpool = "wildemount"
        newdataset = "mightynein"
        newshare = "MyData"
        
        # create a new pool called newpool using the disks in diskset
        self.create_pool(newpool,diskset)

        # Create a dataset named newdataset in pool newpool
        # self.create_dataset(newpool,newdataset)

        # Create a CIFS share called newshare that points to the dataset newdataset in pool newpool
        # self.create_cifs_share(newpool,newdataset,newshare)

        # Create a dataset called newdataset in pool newpool and share it with the same name
        self.create_and_share_dataset(newpool, newdataset)

        # Start the CIFS/SMB service
        #self.service_start('cifs')
        
        # Create a new group
        #self.create_group('family')

        # Create a new user
        #self.create_user('emily')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--hostname', required=True, type=str)
    parser.add_argument('-u', '--user', required=True, type=str)
    parser.add_argument('-p', '--passwd', required=True, type=str)

    args = parser.parse_args(sys.argv[1:])

    startup = Startup(args.hostname, args.user, args.passwd)
    startup.run()

if __name__ == '__main__':
    main()
