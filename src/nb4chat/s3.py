from enum import StrEnum, auto

import boto3

from nb4chat.settings import settings


class Bucket(StrEnum):
    RAW = auto()
    OCRED = auto()


s3_client = boto3.client(
    "s3",
    endpoint_url=settings.endpoint_url,
    aws_access_key_id=settings.key_id,
    aws_secret_access_key=settings.secret_key,
    region_name="garage",
)
