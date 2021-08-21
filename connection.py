import os

from dotenv import load_dotenv
import pysftp
from azure.storage.blob import BlobClient

load_dotenv()


CONTAINER_NAME = os.environ["CONTAINER"]
CONNECTION = os.environ["CONNECTION"]
HOST_NAME = os.environ["HOST_NAME"]
USER_NAME = os.environ["USER_NAME"]
PASSWORD = os.environ["PASSWORD"]

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

def read_and_upload():
    with pysftp.Connection(HOST_NAME,
            username=USER_NAME,
            password=PASSWORD,
            cnopts=cnopts) as sftp:

        with sftp.open("readme.txt", "r") as readme:
            # upload blob
            blob_conn = BlobClient.from_connection_string(
                    conn_str=CONNECTION,
                    container_name=CONTAINER_NAME,
                    blob_name="demo-sftp/sftp_readme.txt"
            )

            blob_conn.upload_blob(readme, overwrite=True)


        with sftp.cd('pub/example'):
            for file in sftp.listdir():
                blob_conn = BlobClient.from_connection_string(
                        conn_str=CONNECTION,
                        container_name=CONTAINER_NAME,
                        blob_name=f"demo-sftp-images/{file}"
                )

                with sftp.open(file) as image_file:
                    blob_conn.upload_blob(image_file, overwrite=True)
