import datetime
import logging

import azure.functions as func
from connection import read_and_upload


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    read_and_upload()