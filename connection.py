import os

import dotenv
import pysftp
from azure.storage.blob import BlobClient

CONTAINER_NAME = os.environ["CONTAINER"]
CONNECTION = os.environ["CONNECTION"]
HOST_NAME = os.environ["HOST_NAME"]
USER_NAME = os.environ["USER_NAME"]
PASSWORD = os.environ["PASSWORD"]

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

if __name__ == "__main__":
    with pysftp.Connection(HOST_NAME,
            username=USER_NAME,
            password=PASSWORD,
            cnopts=cnopts) as sftp:

        sftp.get('readme.txt')
        directory = os.listdir()
        if 'public' not in directory:
            os.mkdir('public')


        with sftp.cd('pub'):
            sftp.get_d('example', 'public')

